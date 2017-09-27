#!/usr/bin/env python
# coding: utf-8
import json, csv, os

# inputs y outputs
try:
    import requests
    query = "donde puedo encontrar una parrilla a carbon para exteriores"

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
    producto = root['text']['content']
else:
    producto = closest_noun['text']['content']

if first_noun and tokens[first_noun] is not closest_noun:
    keywords.append(tokens[first_noun]['text']['content']) 

if second_noun:
    keywords.append(tokens[second_noun]['text']['content'])
    # buscar hasta tercer nivel
    pattern_indexes = search_pattern(["NOUN","ADP","NOUN","ADP","NOUN"], "tag")
    third_noun = pattern_indexes[4] if pattern_indexes else None
    if third_noun:
        keywords.append(tokens[third_noun]['text']['content'])

print "Producto buscado: '{}'".format(repr(closest_noun['text']['content']))
print "Palabras clave adicionales de la búsqueda: {}".format(repr(",".join(keywords)))

# leer base de productos
def unicode_csv_reader(utf8_data, dialect=csv.excel, **kwargs):
    as_list = []
    csv_reader = csv.reader(utf8_data, dialect=dialect, **kwargs)
    for row in csv_reader:
        as_list.append([unicode(cell, 'utf-8') for cell in row])
    return as_list

data = unicode_csv_reader(open('../sharedFiles/Web scraping 15k.csv'))

header = data[0]
data = data[1:]

def n_categorias(first_row, n=0):
    if ('Categoria '+str(n+1)) in first_row:
        return n_categorias(first_row, n+1)
    else:
        return n

n_categorias = n_categorias(header)

# quitar productos sin match de pasillo
raw_data = [row for row in data if "Sin info" not in row[-1]]

# dejar solo donde calza el producto
filtered = [row for row in raw_data if producto in row[header.index('Nombre')].lower()]

# si no encontré nada, intentar con el lemma
if len(filtered) == 0:
    try:
        closest_noun_lemma = closest_noun['lemma']
        filtered = [row for row in raw_data if closest_noun_lemma in row[header.index('Nombre')].lower()]
    except:
        pass

# llenar categorias que estan vacias con el mas cercano hacia izquierda
for row in filtered:
    if row[n_categorias-1] == u'':
        # buscar primera columna no vacia desde derecha
        for i in range(n_categorias-1, -1, -1):
            if row[i] != '':
                # llenar todas las columnas vacias
                for j in range(i, n_categorias):
                    row[j] = row[i]
                break

print "\nProductos encontrados: {} {}".format(len(filtered), repr(producto))

if filtered:
    pasillos = list(set([row[header.index('pasillo')] for row in filtered]))
    if len(pasillos) > 1:
        seguir_filtrando = True
        print "Tenemos productos en distintos pasillos: {}".format(';'.join(byteify(pasillos)))
    else:
        seguir_filtrando = False
        print "Ubicación del producto: {}".format(pasillos[0])
else:
    seguir_filtrando = False

categorias_a_usuario = []
categoria_actual = 0
for i in range(1, n_categorias):
    categorias = list(set([row[i] for row in filtered]))
    if len(categorias) > 1:
        categorias_a_usuario = categorias
        categoria_actual = i
        break

categorias_a_usuario.extend(["No sé/Indiferente"])

output = {
    'header': header,
    'data': filtered,
    'categorias_a_usuario': categorias_a_usuario,
    'categoria_actual': categoria_actual+1,
    'seguir_filtrando': seguir_filtrando,
    'keywords': keywords
}

output = json.dumps(byteify(output), ensure_ascii=False)

print byteify(output)

print ""
print output
response.write(output)
response.close()