#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os, json, csv, unicodedata

try:
    post_data = json.loads(open(os.environ['req']).read())
except:
    post_data = {
                "dominio": "diabetes",
                "query": "pie diabético con diabetes tipo 1"
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
with open('Sinonimos_w2v.csv', 'r') as f:
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
etiquetas_db = json.loads(open('etiquetas_db.json', 'rt').read())
dominio_db = etiquetas_db[post_data['dominio']]

# buscar etiquetas en query, no repetirlas y quitar acentos
# buscar sinonimos tambien
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

output = ','.join(labels)

print output.encode('utf-8')
response.write(output.encode('utf-8'))
response.close()
