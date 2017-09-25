#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os, json, csv, unicodedata

try:
    post_data = json.loads(open(os.environ['req']).read())
except:
    post_data = {
        "dominio": "diabetes",
        "query": "población"
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

# para obtener listado de sinonimos
with open('../sharedFiles/Sinonimos_w2v.csv', 'rt') as f:
    reader = csv.reader(f, delimiter=',')
    sinonimos = list(reader)
def get_sinonimos(keyword):
    for group in sinonimos:
        if keyword in group:
            return group
    return [keyword]

# obtener query de llamada sin acentos
query = remove_accents(post_data['query'].lower())

# leer base de etiquetas
etiquetas_db = json.loads(open('../sharedFiles/etiquetas_db.json', 'rt').read())
dominio_db = etiquetas_db[post_data['dominio']]

# buscar etiquetas en query
# no repetirlas, quitar acentos y buscar sinonimos
labels = []
for label, keyword in dominio_db:
    label = label.capitalize()
    keywords_syn = get_sinonimos(keyword)
    # buscar keyword y sus sinonimos en base de etiquetas
    for keyword_syn in keywords_syn:
        if remove_accents(keyword_syn) in query and len(keyword_syn) > 1:
            # revisar que etiqueta no este repetida
            if label not in labels:
                labels.append(label)
                
# identificar etiquetas mas profundas
# primero identificar caminos en el arbol, quitando nodos vacios
caminos_match_etiquetas = []
with open("../sharedFiles/arbol_etiquetas.csv", "rt") as f:
    reader = csv.reader(f, delimiter=',')
    caminos = list(reader)
    caminos = [[nodo for nodo in camino if nodo != ''] for camino in caminos]

# armar listado auxiliar con match entre etiquetas y caminos
# registrar profundidad de nodo identificado
max_label_depth = -1
for label in labels:
    for camino in caminos:
        if label in camino:
            for idx, node in enumerate(camino):
                if label == node and idx >= max_label_depth:
                    caminos_match_etiquetas.append([camino, label, idx])
                    if max_label_depth < idx:
                        max_label_depth = idx

# dejar solo los nodos mas profundos
caminos_profundos = []
for i, camino_match_etiqueta in enumerate(caminos_match_etiquetas):
    if camino_match_etiqueta[2] == max_label_depth:
        caminos_profundos.append(camino_match_etiqueta)
        
with open("../sharedFiles/resumen_preguntas_etiquetas.tsv", "rt") as f:
    reader = csv.reader(f, delimiter='\t')
    preguntas = list(reader)

def get_preguntas(label, depth):
    sin_resumen = []
    preguntas_resumen = []
    for i, col in enumerate(preguntas[0]):
        if col == 'Etiqueta '+str(depth+1):
            depth_index = i
    for row in preguntas:
        label_at_depth = row[depth_index].lower()
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
    return (sin_resumen, preguntas_resumen)

# si es más de uno, retornarlos para que usuario filtre
if len(caminos_profundos) > 1:
    falta_filtrar = True
    labels = []
    for camino_profundo in caminos_profundos:
        # si no tiene subetiquetas, el mismo es la etiqueta
        try:
            labels.append({
                'etiqueta': camino_profundo[0][max_label_depth+1],
                'subetiquetas': True
            })
        except:
            etiqueta = camino_profundo[0][max_label_depth].lower()
            sin_resumen, preguntas_resumen = get_preguntas(etiqueta, max_label_depth)
            labels.append({
                'etiqueta': etiqueta,
                'subetiquetas': False , 
                'preguntas': {
                    'con_resumen': preguntas_resumen,
                    'sin_resumen': sin_resumen
                }, 
            })
else:
    falta_filtrar = False
    labels = [row[1].encode('utf-8') for row in caminos_profundos]

depth = max_label_depth
output = {
    'etiquetas': labels,
    'profundidad': depth,
    'falta_filtrar': falta_filtrar
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
