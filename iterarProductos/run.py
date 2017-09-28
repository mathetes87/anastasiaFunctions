#!/usr/bin/env python
# coding: utf-8
import json, csv, os

# inputs y outputs
try:
    from tabulate import tabulate
    post_data = json.loads(json.dumps({
        "response": {"seguir_filtrando": True, "mensaje_final": "Podrás encontrar la lámpara de aluminio que buscas en el ", "header": ["Categoria 1", "Categoria 2", "Categoria 3", "Categoria 4", "Categoria 5", "Categoria 6", "Categoria 7", "Imagen Url", "url", "Marca", "Nombre", "Precio", "Sku", "pasillo"], "categorias_a_usuario": ["lamparas de mesa y velador", "lámparas colgantes y techo", "Subcategorías"], "data": [["muebles y decoración", "muebles", "iluminación", "iluminación interior", "lamparas de mesa y velador", "lamparas de mesa y velador", "lamparas de mesa y velador", "http://sodimac.scene7.com/is/image/sodimaccl/3213544?$lista175$", "http://www.sodimac.cl/sodimac-cl/category/cat520046/lamparas-de-mesa-y-velador/?cid=cgoall57849", "tempora", "lámpara sobremesa aluminio marroqui", "54990", "3213544", "pasillo 18 - rack 18"], ["muebles y decoración", "muebles", "iluminación", "iluminación interior", "lámparas colgantes y techo", "lámparas colgantes y techo", "lámparas colgantes y techo", "http://sodimac.scene7.com/is/image/sodimaccl/2841371?$lista175$", "http://www.sodimac.cl/sodimac-cl/category/scat303247/lamparas-colgantes-y-techo?no=192&nrpp=16", "casa bonita", "lámpara de colgar 1 luz aluminio perforado", "12990", "2841371", "pasillo 16 - rack 16"]], "categoria_actual": 5},
        "eleccion": 1
    }))
except:
    post_data = json.loads(open(os.environ['req']).read())

try:
    response = open(os.environ['res'], 'w')
except:
    response = open('dummy_output.txt', 'w')

# pasar objetos a string utf-8
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

def n_categorias(first_row, n=0):
    if ('Categoria '+str(n+1)) in first_row:
        return n_categorias(first_row, n+1)
    else:
        return n

def print_sans(l):
    pop = [4,5,6,7, 8, 9, 11, 12]
    data_sans = [[col for i,col in enumerate(row) if i not in pop] for row in l]
    header_sans = [col for i,col in enumerate(header) if i not in pop]
    try:
        print tabulate(data_sans, headers=header_sans)
    except:
        pass

# datos obtenidos de llamada
header = post_data['response']['header']
categoria_actual = post_data['response']['categoria_actual']
categorias_a_usuario = post_data['response']['categorias_a_usuario']
eleccion = post_data['eleccion']
data = post_data['response']['data']
mensaje_final_parcial = post_data['response']['mensaje_final']

n_categorias = n_categorias(header)

print_sans(data) 

# ------------------------------------------
# 1. Filtrar data según elección del usuario
# ------------------------------------------
if eleccion+1 == len(categorias_a_usuario):
    # elige la ultima (indiferente/no sabe), data se mantiene igual
    pass
else:
    data = [row for row in data if categorias_a_usuario[eleccion] == row[header.index('Categoria '+str(categoria_actual))]]


# ---------------------------------------------------
# 2. Obtener categorias a mostrar como opciones al usuario
# ---------------------------------------------------
categoria_actual += 1

# buscar donde bifurcan categorias
seguir_filtrando = False
for i in range(categoria_actual, n_categorias):
    categoria_index = header.index('Categoria '+str(i))
    categorias = set([row[categoria_index] for row in data])
    if len(categorias) > 1:        
        categorias_a_usuario = list(set([row[categoria_index] for row in data if row[categoria_index] != '']))
        seguir_filtrando = True
        break
    else:
        continue

# -----------------------------------------------------
# 3. Si existe una única ubicación, no seguir filtrando
# -----------------------------------------------------
pasillos = list(set([row[header.index('pasillo')] for row in data]))
if len(pasillos) == 1:
    seguir_filtrando = False

# --------------------------
# 4. Armar output a retornar
# --------------------------
if not seguir_filtrando:
    categorias_a_usuario = []
else:
   categorias_a_usuario.extend(["Subcategorías"])

mesaje_final = "Problema para encontrar el pasillo :("
if len(pasillos) > 0:
    mensaje_final = mensaje_final_parcial + '; '.join(pasillos)

print ""
print_sans(data)

output = {
    'data': data,
    'header': header,
    'seguir_filtrando': seguir_filtrando,
    'categoria_actual': categoria_actual,
    'categorias_a_usuario': [categoria.capitalize() for categoria in categorias_a_usuario],
    'mensaje_final': mensaje_final
}

# -----------------
# 5. Retornar datos
# -----------------
output = json.dumps(byteify(output), ensure_ascii=False)

print ""
#print_sans(data)
#print '["'+'","'.join(categorias_a_usuario)+'"]', seguir_filtrando, pasillos
#print output
print mensaje_final.encode('utf-8')
response.write(output)
response.close()