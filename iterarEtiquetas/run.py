#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os, json, csv, unicodedata

try:
    post_data = json.loads(open(os.environ['req']).read())
except:
    post_data = {
        "dominio": "diabetes",
        "query": "embarazo",
        "etiqueta": "Diabetes Gestacional",
        "profundidad": 1
    }
try:
    response = open(os.environ['res'], 'w')
except:
    response = open('dummy_output.txt', 'w')

# para quitar acentos
def remove_accents(input_str):
    if type(input_str) == str:
        input_str = unicode(input_str, 'utf-8')
    nfkd_form = unicodedata.normalize('NFKD', input_str)
    return u"".join([c for c in nfkd_form if not unicodedata.combining(c)])

# obtener query de llamada sin acentos
query = remove_accents(post_data['query'].lower())

# leer base de etiquetas
etiquetas_db = json.loads(open('../sharedFiles/etiquetas_db.json', 'rt').read())
dominio_db = etiquetas_db[post_data['dominio']]

# encontrar subetiquetas a partir de nivel de profundidad indicado
label = post_data['etiqueta']
depth = post_data['profundidad']
with open("../sharedFiles/arbol_etiquetas.csv", "rt") as f:
    reader = csv.reader(f, delimiter=',')
    caminos = list(reader)
    caminos = [[nodo for nodo in camino if nodo != ''] for camino in caminos]

caminos_match_etiquetas = []
for camino in caminos:
    try:
        if label == camino[depth]:
            caminos_match_etiquetas.append(camino)
    except:
        pass

# tiene subetiquetas?
subetiquetas = []
for camino in caminos_match_etiquetas:
    if len(camino)-1 > depth:
        subetiquetas.append(camino[depth+1].encode('utf-8'))

# armar output
# si es nivel final, buscar preguntas resumen
if len(subetiquetas) == 0:
    sin_resumen = []
    preguntas_resumen = []
    # buscar preguntas
    with open("../sharedFiles/resumen_preguntas_etiquetas.tsv", "rt") as f:
        reader = csv.reader(f, delimiter='\t')
        preguntas = list(reader)
    for i, col in enumerate(preguntas[0]):
        if col == 'Etiqueta '+str(depth+1):
            depth_index = i
    for row in preguntas:
        label_at_depth = row[depth_index]
        resumen_pregunta = row[2]
        respuesta = row[1]
        pregunta = row[0] # IDEALMENTE TENER UN ID!!!
        if label_at_depth == label:
            if resumen_pregunta == '':
                sin_resumen.append(pregunta)
            else:
                pregunta_resumen = {
                    'resumen_pregunta': resumen_pregunta, 
                    'respuesta': respuesta
                }
                if pregunta_resumen not in preguntas_resumen:
                    preguntas_resumen.append(pregunta_resumen)
    output = {
                'falta_filtrar': False,
                'preguntas': {
                            'con_resumen': preguntas_resumen,
                            'sin_resumen': sin_resumen
                        },
                'etiquetas': label,
                'profundidad': depth
            }
# si NO es nivel final, retornarlos para que usuario filtre
else:
    labels = [etiqueta.encode('utf-8') for etiqueta in subetiquetas]
    output = {
                'falta_filtrar': True,
                'etiquetas': labels,
                'profundidad': depth+1,
            }

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

output = json.dumps(byteify(output), ensure_ascii=False)
print output

response.write(output)
response.close()
