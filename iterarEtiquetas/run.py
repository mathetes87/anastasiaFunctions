# coding: utf-8
import json, csv, requests

query = 'busco parrilla'

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
tokens = json.loads(r.text)['tokens']

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

# guardar el sustantivo mas cercano a la raiz
root = find_tokens_by_label_or_tag("label", identifier='ROOT')[0]
closest_verb, _ = closest_token(root, find_tokens_by_label_or_tag("tag", identifier='VERB'))
closest_noun, _ = closest_token(root, find_tokens_by_label_or_tag("tag", identifier='NOUN'))
        
print "Raíz de la oración: '{}'".format(root['text']['content'])
print "Sustantivo más cercano: '{}'".format(closest_noun['text']['content'])

producto = closest_noun['text']['content']

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

def filtrar_productos(filtered, categoria_inicial=1):
    print ""
    pasillos = set([row[header.index('pasillo')] for row in filtered])
    if len(pasillos) <= 1:
        return filtered
    else:
        # buscar donde bifurcan categorias
        for i in range(categoria_inicial, n_categorias):
            index_categoria = header.index('Categoria '+str(i))
            categorias = set([row[index_categoria] for row in filtered])
            if len(categorias) > 1:
                # tengo todavia mas de una categoria
                print "Filtra las categorías del producto por su número:"
                for j, categoria in enumerate(categorias):
                    print j+1, categoria
                print j+2, "No estoy seguro/Indiferente"
                print ""
                eleccion = int(raw_input())
                # filtrar resultados y chequear de nuevo de forma recursiva
                if eleccion == j+2:
                    print "Indiferente", categoria_inicial
                    return filtrar_productos(filtered, categoria_inicial=categoria_inicial+1)
                else:
                    filtered = [row for row in filtered if list(categorias)[eleccion-1] == row[index_categoria]]
                    return filtrar_productos(filtered)
            else:
                continue
        # si salgo es que no puedo seguir filtrando por categorias y quedan pasillos distintos
        print "No se puede seguir filtrando por categorias"
        return filtered

output = filtrar_productos(filtered)

if output:
    pasillos = list(set([row[header.index('pasillo')] for row in output]))
    if len(pasillos) > 1:
        print "Tenemos productos en distintos pasillos: {}".format(','.join(pasillos))
        
    else:
        print "Ubicación del producto: {}".format(pasillos[0])
