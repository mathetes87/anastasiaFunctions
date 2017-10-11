#!/usr/bin/env python
# coding: utf-8
import json, csv, os

# inputs y outputs
try:
    from tabulate import tabulate
    post_data = json.loads(json.dumps({
        "response": {'seguir_filtrando': True, 'mensaje_final': 'Podr\xc3\xa1s encontrar el martillo que buscas en el ', 'header': ['Categoria 1', 'Categoria 2', 'Categoria 3', 'Categoria 4', 'Categoria 5', 'Categoria 6', 'Categoria 7', 'Imagen Url', 'url', 'Marca', 'Nombre', 'Precio', 'Sku', 'pasillo'], 'categorias_a_usuario': ['construcci\xc3\xb3n y herramientas', 'destacados', 'muebles y decoraci\xc3\xb3n', 'ferreter\xc3\xada', 'Subcategor\xc3\xadas'], 'data': [['construcci\xc3\xb3n y herramientas', 'especial herramientas', 'especial herramientas', 'especial herramientas', 'especial herramientas', 'especial herramientas', 'especial herramientas', 'http://sodimac.scene7.com/is/image/sodimaccl/2695588?$lista175$', 'http://www.sodimac.cl/sodimac-cl/category/cat5820009/especial-herramientas?no=48&nrpp=16', 'de walt', 'rotomartillo 32mm 1000w', '463990', '2695588', 'pasillo 70 - rack 70'], ['destacados', 'imperdibles', 'imperdibles', 'imperdibles', 'imperdibles', 'imperdibles', 'imperdibles', 'http://sodimac.scene7.com/is/image/sodimaccl/2913909?$lista175$', 'http://www.sodimac.cl/sodimac-cl/category/cat1990064/imperdibles?no=112&nrpp=16', 'ubermann', 'rotomartillo inalambrico 20v i\xc3\xb3n-li', '', '2913909', 'pasillo 52 - rack 52'], ['ferreter\xc3\xada', 'herramientas', 'herramientas el\xc3\xa9ctricas e inal\xc3\xa1mbricas', 'demoledores', 'demoledores', 'demoledores', 'demoledores', 'http://sodimac.scene7.com/is/image/sodimaccl/611417?$lista175$', 'http://www.sodimac.cl/sodimac-cl/category/cat750201/demoledores', 'bosch', 'rotomartillo 20mm 650w', '113990', '611417', 'pasillo 54 - rack 54'], ['ferreter\xc3\xada', 'herramientas', 'herramientas el\xc3\xa9ctricas e inal\xc3\xa1mbricas', 'demoledores', 'demoledores', 'demoledores', 'demoledores', 'http://sodimac.scene7.com/is/image/sodimaccl/2916711?$lista175$', 'http://www.sodimac.cl/sodimac-cl/category/cat750201/demoledores', 'de walt', 'rotomartillo sds plus de 800 w 3 modos', '119990', '2916711', 'pasillo 54 - rack 54'], ['ferreter\xc3\xada', 'herramientas', 'herramientas el\xc3\xa9ctricas e inal\xc3\xa1mbricas', 'demoledores', 'demoledores', 'demoledores', 'demoledores', 'http://sodimac.scene7.com/is/image/sodimaccl/3617x?$lista175$', 'http://www.sodimac.cl/sodimac-cl/category/cat750201/demoledores', 'bosch', 'rotomartillo 24mm 800w', '164990', '3617x', 'pasillo 54 - rack 54'], ['ferreter\xc3\xada', 'herramientas', 'herramientas el\xc3\xa9ctricas e inal\xc3\xa1mbricas', 'demoledores', 'demoledores', 'demoledores', 'demoledores', 'http://sodimac.scene7.com/is/image/sodimaccl/2659565?$lista175$', 'http://www.sodimac.cl/sodimac-cl/category/cat750201/demoledores', 'bosch', 'martillo demoledor 1100w', '386990', '2659565', 'pasillo 70 - rack 70'], ['ferreter\xc3\xada', 'herramientas', 'herramientas el\xc3\xa9ctricas e inal\xc3\xa1mbricas', 'demoledores', 'demoledores', 'demoledores', 'demoledores', 'http://sodimac.scene7.com/is/image/sodimaccl/1689479?$lista175$', 'http://www.sodimac.cl/sodimac-cl/category/cat750201/demoledores', 'makita', 'martillo demoledor 1510w hm1307', '748990', '1689479', 'pasillo 54 - rack 54'], ['muebles y decoraci\xc3\xb3n', 'muebles', 'menaje', 'menaje cocina', 'utensilios de cocina', 'otros utensilios de cocina', '', 'http://sodimac.scene7.com/is/image/sodimaccl/149861?$lista175$', 'http://www.sodimac.cl/sodimac-cl/category/cat2960008/otros-utensilios-de-cocina?no=144&nrpp=16', 'home collection', 'martillo ablandador de carne', '3990', '149861', 'pasillo 14 - rack 14']], 'categoria_actual': 1},
        "eleccion": 0
    }))
except:
    post_data = json.loads(open(os.environ['req']).read())

print post_data

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

print ""
print_sans(data)

# ------------------------------------------
# 1. Filtrar data según elección del usuario
# ------------------------------------------
if eleccion + 1 == len(categorias_a_usuario):
    # elige la ultima (subcategorías), data se mantiene igual
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

print ""
print_sans(data)

# --------------------------
# 4. Armar output a retornar
# --------------------------
if not seguir_filtrando:
    categorias_a_usuario = []
    mensaje_final = mensaje_final_parcial.encode('utf-8') +"{}. Encontrarás {}, junto a otros artículos relacionados".format('; '.join(pasillos).encode('utf-8'), ', '.join([row[header.index('Nombre')] for row in data[:3]]).encode('utf-8'))
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
#print mensaje_final#.encode('utf-8')
response.write(output)
response.close()