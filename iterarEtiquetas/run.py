#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os, json, csv, unicodedata

try:
    post_data = json.loads(open(os.environ['req']).read())
except:
    post_data = {
        "dominio": "diabetes",
        "query": "embarazo",
        "etiqueta": "Diabetes gestacional",
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
if len(subetiquetas) == 0:    # si es nivel final, buscar preguntas resumen
    falta_filtrar = False
    # buscar preguntas
    output = {
                'preguntas': [],
                'etiquetas': subetiquetas
            }
else:    # si NO es nivel final, retornarlos para que usuario filtre
    falta_filtrar = True
    labels = [etiqueta.encode('utf-8') for etiqueta in subetiquetas]
    depth = depth + 1
    output = {
                'etiquetas': labels,
                'profundidad': depth,
                'falta_filtrar': falta_filtrar
            }

output = json.dumps(output, ensure_ascii=False)

print output
response.write(output)
response.close()
