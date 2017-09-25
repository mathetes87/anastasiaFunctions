#!/usr/bin/env python
# coding: utf-8
import json, csv, requests

# inputs y outputs
try:
    post_data = json.loads(open(os.environ['req']).read())
except:
    query = "donde puedo encontrar una parrilla"

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
        "categoria": 1,
        "eleccion": 2,
        "response": json.loads(r.text)
    }

# datos obtenidos de llamada
categoria_inicial = post_data['categoria']
eleccion = post_data['eleccion']
tokens = post_data['response']['tokens']

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

root = find_tokens_by_label_or_tag("label", identifier='ROOT')[0]
closest_noun, _ = closest_token(root, find_tokens_by_label_or_tag("tag", identifier='NOUN'))
        
print "Raíz de la oración: '{}'".format(root['text']['content'])
print "Sustantivo más cercano: '{}'".format(closest_noun['text']['content'])

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
filtered = [row for row in data if "Sin info" not in row]

# dejar solo donde calza el producto
filtered = [row for row in filtered if producto in row[header.index('Nombre')]]
print "Productos encontrados: {} {}".format(len(filtered), producto)

pasillos = set([row[header.index('pasillo')] for row in filtered])
if len(pasillos) > 1:
    # buscar donde bifurcan categorias
    for i in range(categoria_inicial, n_categorias):
        index_categoria = header.index('Categoria '+str(i))
        categorias = set([row[index_categoria] for row in filtered])
        if len(categorias) > 1:
            # filtrar resultados
            if eleccion == -1:
                print "Indiferente", categoria_inicial
                break
            else:
                filtered = [row for row in filtered if list(categorias)[eleccion-1] == row[index_categoria]]
                break
        else:
            continue
    # si salgo es que no puedo seguir filtrando por categorias y quedan pasillos distintos
    print "No se puede seguir filtrando por categorias"

if filtered:
    pasillos = list(set([row[header.index('pasillo')] for row in filtered]))
    if len(pasillos) > 1:
        seguir_filtrando = True
        print "Tenemos productos en distintos pasillos: {}".format(','.join(byteify(pasillos)))
    else:
        seguir_filtrando = False
        print "Ubicación del producto: {}".format(pasillos[0])

output = {
    'data': filtered,
    'seguir_filtrando': seguir_filtrando
}

output = json.dumps(byteify(output), ensure_ascii=False)

print ""
print output
response.write(output)
response.close()