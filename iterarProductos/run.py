#!/usr/bin/env python
# coding: utf-8
import json, csv, os

# inputs y outputs
try:
    from tabulate import tabulate
    post_data = json.loads(json.dumps({
        "response": {"seguir_filtrando": True, "mensaje_final": "Podrás encontrar las pinturas que buscas en el ", "header": ["Categoria 1", "Categoria 2", "Categoria 3", "Categoria 4", "Categoria 5", "Categoria 6", "Categoria 7", "Imagen Url", "url", "Marca", "Nombre", "Precio", "Sku", "pasillo"], "categorias_a_usuario": ["ferretería", "pinturas", "Subcategorías"], "data": [["ferretería", "herramientas", "herramientas por especialidad", "herramientas para instalación de pisos", "protectores de piso y ropa", "protectores de piso y ropa", "protectores de piso y ropa", "http://sodimac.scene7.com/is/image/sodimaccl/161918?$lista175$", "http://www.sodimac.cl/sodimac-cl/category/cat2960096/protectores-de-piso-y-ropa?no=16&nrpp=16", "atlas", "balde para pintura 10 litros", "6190", "161918", "pasillo 70 - rack 70"], ["pinturas", "preparación y reparación de superficies", "antióxido y convertidores de óxido", "antióxido y convertidores de óxido", "antióxido y convertidores de óxido", "antióxido y convertidores de óxido", "antióxido y convertidores de óxido", "http://sodimac.scene7.com/is/image/sodimaccl/97527?$lista175$", "http://www.sodimac.cl/sodimac-cl/category/cat4850043/antioxido-y-convertidores-de-oxido", "sipa", "pintura antióxido maestranza 1/4 galón negro", "6190", "97527", "pasillo 28 - rack 28"], ["pinturas", "preparación y reparación de superficies", "antióxido y convertidores de óxido", "antióxido y convertidores de óxido", "antióxido y convertidores de óxido", "antióxido y convertidores de óxido", "antióxido y convertidores de óxido", "http://sodimac.scene7.com/is/image/sodimaccl/181625?$lista175$", "http://www.sodimac.cl/sodimac-cl/category/cat4850043/antioxido-y-convertidores-de-oxido", "sipa", "pintura antióxido maestranza 1/4 galón rojo", "6190", "181625", "pasillo 28 - rack 28"], ["pinturas", "preparación y reparación de superficies", "antióxido y convertidores de óxido", "antióxido y convertidores de óxido", "antióxido y convertidores de óxido", "antióxido y convertidores de óxido", "antióxido y convertidores de óxido", "http://sodimac.scene7.com/is/image/sodimaccl/961655?$lista175$", "http://www.sodimac.cl/sodimac-cl/category/cat4850043/antioxido-y-convertidores-de-oxido", "sipa", "pintura antióxido maestranza 1 galón rojo", "14490", "961655", "pasillo 28 - rack 28"], ["pinturas", "preparación y reparación de superficies", "antióxido y convertidores de óxido", "antióxido y convertidores de óxido", "antióxido y convertidores de óxido", "antióxido y convertidores de óxido", "antióxido y convertidores de óxido", "http://sodimac.scene7.com/is/image/sodimaccl/181102?$lista175$", "http://www.sodimac.cl/sodimac-cl/category/cat4850043/antioxido-y-convertidores-de-oxido", "sipa", "pintura antióxido maestranza 1 galón gris", "14490", "181102", "pasillo 28 - rack 28"], ["pinturas", "preparación y reparación de superficies", "antióxido y convertidores de óxido", "antióxido y convertidores de óxido", "antióxido y convertidores de óxido", "antióxido y convertidores de óxido", "antióxido y convertidores de óxido", "http://sodimac.scene7.com/is/image/sodimaccl/225282?$lista175$", "http://www.sodimac.cl/sodimac-cl/category/cat4850043/antioxido-y-convertidores-de-oxido", "sipa", "pintura antióxido maestranza 1 galón negro", "14490", "225282", "pasillo 28 - rack 28"]], "categoria_actual": 1},
        "eleccion": 2
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

# ------------------------------------------
# 1. Filtrar data según elección del usuario
# ------------------------------------------
if eleccion+1 == len(categorias_a_usuario):
    # elige la ultima (indiferente/no sabe), data se mantiene igual
    pass
else:
    data = [row for row in data if categorias_a_usuario[eleccion].lower() == row[header.index('Categoria '+str(categoria_actual))].lower()]

#print categorias_a_usuario[eleccion].lower().encode('utf-8')

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
        categoria_actual = i
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

#print ""
#print_sans(data)

# --------------------------
# 4. Armar output a retornar
# --------------------------
if not seguir_filtrando:
    categorias_a_usuario = []
    mensaje_final = mensaje_final_parcial + '; '.join(pasillos)
else:
    categorias_a_usuario.extend(["Subcategorías"])
    mensaje_final = mensaje_final_parcial

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

#print '["'+'","'.join(categorias_a_usuario)+'"]', seguir_filtrando, pasillos
#print output
#print mensaje_final.encode('utf-8')
response.write(output)
response.close()