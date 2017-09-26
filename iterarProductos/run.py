#!/usr/bin/env python
# coding: utf-8
import json, csv, os

# inputs y outputs
try:
    from tabulate import tabulate
    post_data = json.loads(json.dumps({
        "header": ["Categoria 1", "Categoria 2", "Categoria 3", "Categoria 4", "Categoria 5", "Categoria 6", "Categoria 7", "Imagen Url", "url", "Marca", "Nombre", "Precio", "Sku", "pasillo"],
        "categoria_actual": 2,
        "categorias_a_usuario": ["Preparación y reparación de superficies", "Herramientas", "No sé/Indiferente"],
        "eleccion": 0,
        "data": [["Ferretería", "Herramientas", "Herramientas por Especialidad", "Herramientas para instalación de pisos", "Protectores de piso y ropa", "Protectores de piso y ropa", "Protectores de piso y ropa", "http://sodimac.scene7.com/is/image/SodimacCL/161918?$lista175$", "http://www.sodimac.cl/sodimac-cl/category/cat2960096/Protectores-de-piso-y-ropa?No=16&Nrpp=16", "Atlas", "Balde para Pintura 10 litros", "6190", "161918", "Pasillo 70 - Rack 70"], ["Pinturas", "Preparación y reparación de superficies", "Antióxido y Convertidores de óxido", "Antióxido y Convertidores de óxido", "Antióxido y Convertidores de óxido", "Antióxido y Convertidores de óxido", "Antióxido y Convertidores de óxido", "http://sodimac.scene7.com/is/image/SodimacCL/97527?$lista175$", "http://www.sodimac.cl/sodimac-cl/category/cat4850043/Antioxido-y-Convertidores-de-oxido", "Sipa", "Pintura Antióxido Maestranza 1/4 galón Negro", "6190", "97527", "Pasillo 28 - Rack 28"], ["Pinturas", "Preparación y reparación de superficies", "Antióxido y Convertidores de óxido", "Antióxido y Convertidores de óxido", "Antióxido y Convertidores de óxido", "Antióxido y Convertidores de óxido", "Antióxido y Convertidores de óxido", "http://sodimac.scene7.com/is/image/SodimacCL/181625?$lista175$", "http://www.sodimac.cl/sodimac-cl/category/cat4850043/Antioxido-y-Convertidores-de-oxido", "Sipa", "Pintura Antióxido Maestranza 1/4 galón Rojo", "6190", "181625", "Pasillo 28 - Rack 28"], ["Pinturas", "Preparación y reparación de superficies", "Antióxido y Convertidores de óxido", "Antióxido y Convertidores de óxido", "Antióxido y Convertidores de óxido", "Antióxido y Convertidores de óxido", "Antióxido y Convertidores de óxido", "http://sodimac.scene7.com/is/image/SodimacCL/961655?$lista175$", "http://www.sodimac.cl/sodimac-cl/category/cat4850043/Antioxido-y-Convertidores-de-oxido", "Sipa", "Pintura Antióxido Maestranza 1 galón Rojo", "14490", "961655", "Pasillo 28 - Rack 28"], ["Pinturas", "Preparación y reparación de superficies", "Antióxido y Convertidores de óxido", "Antióxido y Convertidores de óxido", "Antióxido y Convertidores de óxido", "Antióxido y Convertidores de óxido", "Antióxido y Convertidores de óxido", "http://sodimac.scene7.com/is/image/SodimacCL/181102?$lista175$", "http://www.sodimac.cl/sodimac-cl/category/cat4850043/Antioxido-y-Convertidores-de-oxido", "Sipa", "Pintura Antióxido Maestranza 1 galón Gris", "14490", "181102", "Pasillo 28 - Rack 28"], ["Pinturas", "Preparación y reparación de superficies", "Antióxido y Convertidores de óxido", "Antióxido y Convertidores de óxido", "Antióxido y Convertidores de óxido", "Antióxido y Convertidores de óxido", "Antióxido y Convertidores de óxido", "http://sodimac.scene7.com/is/image/SodimacCL/225282?$lista175$", "http://www.sodimac.cl/sodimac-cl/category/cat4850043/Antioxido-y-Convertidores-de-oxido", "Sipa", "Pintura Antióxido Maestranza 1 galón Negro", "14490", "225282", "Pasillo 28 - Rack 28"]]
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
    pop = [6,7, 8, 9, 11, 12]
    data_sans = [[col for i,col in enumerate(row) if i not in pop] for row in l]
    header_sans = [col for i,col in enumerate(header) if i not in pop]
    try:
        print tabulate(data_sans, headers=header_sans)
    except:
        pass

# datos obtenidos de llamada
header = post_data['header']
categoria_actual = post_data['categoria_actual']
categorias_a_usuario = post_data['categorias_a_usuario']
eleccion = post_data['eleccion']
data = post_data['data']

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

print ""
print_sans(data)

output = {
    'data': data,
    'seguir_filtrando': seguir_filtrando,
    'categoria_actual': categoria_actual,
    'categorias_a_usuario': categorias_a_usuario,
    'ubicaciones': pasillos
}

# -----------------
# 5. Retornar datos
# -----------------
output = json.dumps(byteify(output), ensure_ascii=False)

print ""
#print_sans(data)
#print '["'+'","'.join(categorias_a_usuario)+'"]', seguir_filtrando, pasillos
print output
response.write(output)
response.close()