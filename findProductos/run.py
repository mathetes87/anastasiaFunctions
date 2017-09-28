#!/usr/bin/env python
# coding: utf-8
import json, csv, os, re

# inputs y outputs
try:
    import requests
    from tabulate import tabulate
    query = "donde encuentro hotdogs?"

    url ='https://language.googleapis.com/v1beta2/documents:analyzeSyntax?fields=language%2Ctokens&key=AIzaSyCeC5Dnx1qOfNKgUY6PUnl8IcCcx53nLwQ'
    params = {
        "document": 
            {
                "content": query,
                "language": "es",
                "type": "PLAIN_TEXT"
            }
    }

    r = requests.post(url, data=json.dumps(params))
    post_data = {
        "response": json.loads(r.text)
    }
except:
    post_data = json.loads(open(os.environ['req']).read())

# datos obtenidos de llamada
tokens = post_data['response']['tokens']
tags_list = [token['partOfSpeech']['tag'] for token in tokens]

try:
    response = open(os.environ['res'], 'w')
except:
    response = open('dummy_output.txt', 'w')

# funciones auxiliares para recorrer árbol sintáctico de la oración
def distance_to_token(current_token, target_token, distance=0):
    new_token = tokens[target_token['dependencyEdge']['headTokenIndex']]
    if target_token == current_token:
        # si encontré el token que buscaba
        return distance
    elif new_token == target_token:
        # si llegué a la raiz se vuelve circular
        return distance + 1
    else:
        distance += 1
        return distance_to_token(new_token, current_token, distance)
    
def find_tokens_by_label_or_tag(label_or_tag, identifier):
    tokens_found = []
    for i, token in enumerate(tokens):
        tag_match = (label_or_tag == "label" and token['dependencyEdge']['label'] == identifier)
        label_match = (label_or_tag == "tag" and token['partOfSpeech']['tag'] == identifier)
        if label_match or tag_match:
            tokens_found.append(token)            
    return tokens_found

def closest_token(current_token, candidates):
    closest = {'token': None, 'distance': 2112}
    for candidate in candidates:
        this_distance = distance_to_token(current_token, candidate)
        if this_distance < closest['distance']:
            closest['distance'] = this_distance
            closest['token'] = candidate
    return closest['token'], closest['distance']

def byteify(input):
    if isinstance(input, dict):
        return {byteify(key): byteify(value)
                for key, value in input.iteritems()}
    elif isinstance(input, list):
        return [byteify(element) for element in input]
    elif isinstance(input, unicode):
        return input.encode('utf-8')
    else:
        return input

def filter_data_by_word(word, column_index, data, case_sensitive=True, keep_if_found=True):
    if case_sensitive:
        data_lower = [[col.lower() for col in row] for row in data]
        word = word.lower()
    else:
        data_lower = data
    if keep_if_found:
        #print row
        return [row for row in data_lower if word in row[column_index]]
    else:
        return [row for row in data_lower if word not in row[column_index]]

def search_pattern(pattern, label_or_tag):
    if label_or_tag == "tag":
        if ",".join(pattern) in ",".join(tags_list):
            matched_tokens = []
            for i, tagi in enumerate(tags_list):
                for j, tagj in enumerate(pattern):
                    try:
                        if tags_list[i+j] == tagj:
                            matched_tokens.append(i+j)
                            if len(matched_tokens) == len(pattern):
                                return matched_tokens
                            else:
                                continue
                        else:
                            matched_tokens = []
                            break
                    except:
                        continue
            return None
        else:
            return None
    else:
        pass

def search_pattern2(pattern, label_or_tag, current_pattern_index, current_token_index=0, start_token_recur=0, found_tokens=[]):
    # busca el patrón en orden inverso, porque la cadena de punteros en los tokens indican comienzo de flecha
    if label_or_tag == "tag":
        if len(pattern) == len(found_tokens):
            return found_tokens
        elif len(tokens) == start_token_recur:
            return []
        else:
            print pattern[current_pattern_index], tokens[current_token_index]['partOfSpeech']['tag']
            if current_token_index == tokens[current_token_index]['dependencyEdge']['headTokenIndex']:
                # si se vuelve circular, seguir con siguiente token
                return search_pattern2(pattern, label_or_tag, len(pattern)-1, current_token_index=start_token_recur+1, start_token_recur=start_token_recur+1, found_tokens=[])
            elif pattern[current_pattern_index] == tokens[current_token_index]['partOfSpeech']['tag']:
                # encuentra match, seguir con pattern y token siguientes
                next_pattern_index = current_pattern_index - 1
                next_token_index = tokens[current_token_index]['dependencyEdge']['headTokenIndex']
                found_tokens.append(tokens[current_token_index])
                return search_pattern2(pattern, label_or_tag, next_pattern_index, current_token_index=next_token_index, start_token_recur=start_token_recur, found_tokens=found_tokens)
            else:
                # no hizo match, seguir con siguiente token y reiniciar pattern
                return search_pattern2(pattern, label_or_tag, len(pattern)-1, current_token_index=start_token_recur+1, start_token_recur=start_token_recur+1, found_tokens=[])


def unicode_csv_reader(utf8_data, dialect=csv.excel, **kwargs):
    as_list = []
    csv_reader = csv.reader(utf8_data, dialect=dialect, **kwargs)
    for row in csv_reader:
        as_list.append([unicode(cell, 'utf-8') for cell in row])
    return as_list

def n_categorias(first_row, n=0):
    if ('Categoria '+str(n+1)) in first_row:
        return n_categorias(first_row, n+1)
    else:
        return n

root = find_tokens_by_label_or_tag("label", identifier='ROOT')[0]
closest_noun, _ = closest_token(root, find_tokens_by_label_or_tag("tag", identifier='NOUN'))
root_is_noun = (root['partOfSpeech']['tag'] == 'NOUN')

pattern_indexes = search_pattern(["NOUN","ADP","NOUN"], "tag")
first_noun = pattern_indexes[0] if pattern_indexes else None
second_noun = pattern_indexes[2] if pattern_indexes else None


#--------------------------------------------------------------------------------
# Con toda la información sintáctica, decidir cuál es el producto y sus atributos
#--------------------------------------------------------------------------------
keywords = []
if root_is_noun:
    producto = root
else:
    producto = closest_noun

if first_noun and tokens[first_noun] is not closest_noun:
    keywords.append(tokens[first_noun]['text']['content']) 

if second_noun:
    keywords.append(tokens[second_noun]['text']['content'])
    # buscar hasta tercer nivel
    pattern_indexes = search_pattern(["NOUN","ADP","NOUN","ADP","NOUN"], "tag")
    third_noun = pattern_indexes[4] if pattern_indexes else None
    if third_noun:
        keywords.append(tokens[third_noun]['text']['content'])

try:
    print "Producto buscado: '{}' ({})".format(repr(closest_noun['text']['content']), repr(closest_noun['lemma']))
except:
    pass
print "Palabras clave adicionales de la búsqueda: {}".format(repr(",".join(keywords)))

#--------------------------------------------------------------------------------
# Leer y filtrar base de productos
#--------------------------------------------------------------------------------
data = unicode_csv_reader(open('../sharedFiles/Web scraping 15k.csv'))

header = data[0]
data = data[1:]

def print_sans(data):
    pop = [5, 6, 7, 8, 9, 11, 12]
    data_sans = [[col for i,col in enumerate(row) if i not in pop] for row in data]
    header_sans = [col for i,col in enumerate(header) if i not in pop]
    try:
        print tabulate(data_sans, headers=header_sans)
    except:
        pass

n_categorias = n_categorias(header)

# quitar productos sin match de pasillo
filtered_base = filter_data_by_word("Sin info", -1, data, case_sensitive=False, keep_if_found=False)

if producto:
    # filtrar segun nombre del producto
    filtered = filter_data_by_word(producto['text']['content'], header.index('Nombre'), filtered_base)
else:
    filtered = []

try:
    # unir filtrado de lemma sin duplicar filas
    aux_filtered_lemma = filter_data_by_word(producto['lemma'], header.index('Nombre'), filtered_base)
    for row in aux_filtered_lemma:
        if row not in filtered:
            filtered.append(row)
except:
    pass

# filtrar utilizando las palabras clave encontradas
have_keyword = []
for keyword in keywords:
    for i in range(n_categorias):
        have_keyword.extend(filter_data_by_word(keyword, header.index('Categoria '+str(i+1)), filtered, case_sensitive=False))
    have_keyword.extend(filter_data_by_word(keyword, header.index('Nombre'), filtered, case_sensitive=False))

# si quedaron filas tras filtrar por keywords, ocupar esos datos
if have_keyword:
    filtered = []
    for row in have_keyword:
        if row not in filtered:
            filtered.append(row)

# llenar categorias que estan vacias con el mas cercano hacia izquierda
for row in filtered:
    if row[header.index('Categoria '+str(n_categorias-1))] == u'':
        # buscar primera columna no vacia desde derecha
        for i in range(n_categorias-1, -1, -1):
            if row[i] != '':
                # llenar todas las columnas vacias
                for j in range(i, n_categorias):
                    row[j] = row[i]
                break

try:
    print "\nProductos encontrados: {} {}".format(len(filtered), repr(producto['text']['content']))
except:
    pass

if filtered:
    pasillos = list(set([row[header.index('pasillo')] for row in filtered]))
    if len(pasillos) > 1:
        seguir_filtrando = True
        print "Tenemos productos en distintos pasillos: {}".format(';'.join(byteify(pasillos)))
    else:
        seguir_filtrando = False
        print "Ubicación del producto: {}".format(pasillos[0].encode('utf-8'))
else:
    pasillos = []
    seguir_filtrando = False

categorias_a_usuario = []
categoria_actual = 1
for i in range(1, n_categorias):
    categorias = list(set([row[header.index('Categoria '+str(i))] for row in filtered]))
    if len(categorias) > 1:
        categorias_a_usuario = categorias
        categoria_actual = i
        break

if not seguir_filtrando:
    categorias_a_usuario = []
else:
    categorias_a_usuario.extend(["Subcategorías"])

if producto:
    # en base a género y número del producto, preparar 'artículo definido' de la oración
    sustantivo = producto['text']['content']
    if producto['partOfSpeech']['gender'] == 'FEMININE':
        if producto['partOfSpeech']['number'] == 'SINGULAR':
            articulo_definido = 'la'
        else:
            articulo_definido = 'las'
    else:
        if producto['partOfSpeech']['number'] == 'SINGULAR':
            articulo_definido = 'el'
        else:
            articulo_definido = 'los'
    try:
        if third_noun:
            palabras = [tokens[index]['text']['content'] for index in search_pattern(["NOUN","ADP","NOUN","ADP","NOUN"], "tag")]
            sustantivo = ' '.join(palabras)
        elif second_noun:
            palabras = [tokens[index]['text']['content'] for index in search_pattern(["NOUN","ADP","NOUN"], "tag")]
            sustantivo = ' '.join(palabras)
    except:
        pass

    # armar oración final, tal vez sólo parcial
    if not seguir_filtrando:
        if len(pasillos) > 0:
            mensaje_final = "Podrás encontrar {} {} que buscas en el {}".format(articulo_definido, sustantivo.encode('utf-8'), '; '.join(pasillos).encode('utf-8'))
        else:
            mensaje_final = "No tenemos {} en Sodimac".format(sustantivo.encode('utf-8'))
    else:
        mensaje_final = "Podrás encontrar {} {} que buscas en el ".format(articulo_definido, sustantivo.encode('utf-8'))
else:
    mensaje_final = "Porfa escribe en español más formal"

output = {
    'header': header,
    'data': filtered,
    'categorias_a_usuario': [categoria for categoria in categorias_a_usuario],
    'categoria_actual': categoria_actual,
    'seguir_filtrando': seguir_filtrando,
    'mensaje_final': mensaje_final
}

output = json.dumps(byteify(output), ensure_ascii=False)

print_sans(filtered)

print ""
#print output
response.write(output)
response.close()