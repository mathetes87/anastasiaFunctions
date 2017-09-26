#!/usr/bin/env python
# coding: utf-8
import json, csv, os

# inputs y outputs
try:
    import requests
    query = "Electricidad. que pasillo?"

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
    new_token = tokens[current_token['dependencyEdge']['headTokenIndex']]
    if current_token == target_token:
        # si encontré el token que buscaba
        return distance
    elif new_token == current_token:
        # si llegué a la raiz se vuelve circular
        return distance + 1
    else:
        distance += 1
        return distance_to_token(new_token, target_token, distance)
    
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

def closest_pattern(pattern):
    

root = find_tokens_by_label_or_tag("label", identifier='ROOT')[0]
closest_noun, _ = closest_token(root, find_tokens_by_label_or_tag("tag", identifier='NOUN'))
root_is_noun = (root['partOfSpeech']['tag'] == 'NOUN')
noun_adp_noun = ("NOUN,ADP,NOUN" in ",".join(tags_list))

        
print "Raíz de la oración: '{}'".format(repr(root['text']['content'].decode('utf-8')))
print "Sustantivo más cercano: '{}'".format(repr(closest_noun['text']['content']))

#--------------------------------------------------------------------------------
# Con toda la información sintáctica, decidir cuál es el producto y sus atributos
#--------------------------------------------------------------------------------
if root_is_noun:
    producto = root['text']['content']
else:
    producto = closest_noun['text']['content']

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
filtered = [row for row in data if "Sin info" not in row[-1]]

# dejar solo donde calza el producto
filtered = [row for row in filtered if producto in row[header.index('Nombre')].lower()]

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


print "Productos encontrados: {} {}".format(len(filtered), repr(producto))

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
categoria_actual = []
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
    'categoria_actual': categoria_actual,
    'seguir_filtrando': seguir_filtrando
}

output = json.dumps(byteify(output), ensure_ascii=False)

print ""
print output
response.write(output)
response.close()