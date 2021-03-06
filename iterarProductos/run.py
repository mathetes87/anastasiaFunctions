#!/usr/bin/env python
# coding: utf-8
import json, csv, os

# inputs y outputs
try:
    from tabulate import tabulate
    post_data = json.loads(json.dumps({
        "response": {"seguir_filtrando": True, "mensaje_final": "Podrás encontrar las parrillas que buscas en el ", "header": ["Categoria 1", "Categoria 2", "Categoria 3", "Categoria 4", "Categoria 5", "Categoria 6", "Categoria 7", "Imagen Url", "url", "Marca", "Nombre", "Precio", "Sku", "pasillo"], "categorias_a_usuario": ["destacados", "aire libre-parrillas", "baño", "Subcategorías"], "data": [["baño", "cocina y línea blanca", "baño", "limpieza", "detergentes y limpiadores", "limpiadores de cocina", "", "http://sodimac.scene7.com/is/image/sodimaccl/3095665?$lista175$", "http://www.sodimac.cl/sodimac-cl/category/cat4850292/limpiadores-de-cocina", "kleine", "limpiador y desengrasante de parrillas 500 ml k...", "2990", "3095665", "pasillo 51 - rack 51"], ["aire libre-parrillas", "parrillas y quinchos", "braseros", "braseros", "braseros", "braseros", "braseros", "http://sodimac.scene7.com/is/image/sodimaccl/3345130?$lista175$", "http://www.sodimac.cl/sodimac-cl/category/cat520024/braseros-y-discos", "varvacoa", "parrilla mesa brasero a carbón ranco", "349990", "3345130", "pasillo 1 - rack 1"], ["aire libre-parrillas", "parrillas y quinchos", "parrillas a carbón", "parrillas a carbón", "parrillas a carbón", "parrillas a carbón", "parrillas a carbón", "http://sodimac.scene7.com/is/image/sodimaccl/1462733?$lista175$", "http://www.sodimac.cl/sodimac-cl/category/scat354868/parrillas-a-carbon", "mr beef", "parrilla a carbón 40x35x34 cm", "18990", "1462733", "jardín, pasillo 3 - rack 3"], ["aire libre-parrillas", "parrillas y quinchos", "parrillas a carbón", "parrillas a carbón", "parrillas a carbón", "parrillas a carbón", "parrillas a carbón", "http://sodimac.scene7.com/is/image/sodimaccl/1478869?$lista175$", "http://www.sodimac.cl/sodimac-cl/category/scat354868/parrillas-a-carbon", "mr beef", "parrilla a carbón 1/2 tambor con tapa", "30890", "1478869", "jardín, pasillo 3 - rack 3"], ["aire libre-parrillas", "parrillas y quinchos", "parrillas a carbón", "parrillas a carbón", "parrillas a carbón", "parrillas a carbón", "parrillas a carbón", "http://sodimac.scene7.com/is/image/sodimaccl/1478885?$lista175$", "http://www.sodimac.cl/sodimac-cl/category/scat354868/parrillas-a-carbon", "mr beef", "parrilla a carbón 1/2 tambor con roldana", "19990", "1478885", "jardín, pasillo 3 - rack 3"], ["aire libre-parrillas", "parrillas y quinchos", "parrillas a carbón", "parrillas a carbón", "parrillas a carbón", "parrillas a carbón", "parrillas a carbón", "http://sodimac.scene7.com/is/image/sodimaccl/177679?$lista175$", "http://www.sodimac.cl/sodimac-cl/category/scat354868/parrillas-a-carbon", "mr beef", "parrilla a carbón circular", "8290", "177679", "jardín, pasillo 3 - rack 3"], ["aire libre-parrillas", "parrillas y quinchos", "parrillas a carbón", "parrillas a carbón", "parrillas a carbón", "parrillas a carbón", "parrillas a carbón", "http://sodimac.scene7.com/is/image/sodimaccl/3247414?$lista175$", "http://www.sodimac.cl/sodimac-cl/category/scat354868/parrillas-a-carbon", "mr beef", "parrilla a carbón pg-cg004", "79990", "3247414", "jardín, pasillo 70 - rack 70"], ["aire libre-parrillas", "parrillas y quinchos", "parrillas a carbón", "parrillas a carbón", "parrillas a carbón", "parrillas a carbón", "parrillas a carbón", "http://sodimac.scene7.com/is/image/sodimaccl/672394?$lista175$", "http://www.sodimac.cl/sodimac-cl/category/scat354868/parrillas-a-carbon", "mr beef", "parrilla carbón rectangular 66x36 x 26 cm. ple...", "10990", "672394", "jardín, pasillo 3 - rack 3"], ["aire libre-parrillas", "parrillas y quinchos", "parrillas a gas", "parrillas a gas", "parrillas a gas", "parrillas a gas", "parrillas a gas", "http://sodimac.scene7.com/is/image/sodimaccl/2747375?$lista175$", "http://www.sodimac.cl/sodimac-cl/category/scat354867/parrillas-a-gas", "mr beef", "parrilla a gas 2 quemadores", "159990", "2747375", "jardín, pasillo 3 - rack 3"], ["aire libre-parrillas", "parrillas y quinchos", "parrillas a gas", "parrillas a gas", "parrillas a gas", "parrillas a gas", "parrillas a gas", "http://sodimac.scene7.com/is/image/sodimaccl/2831805?$lista175$", "http://www.sodimac.cl/sodimac-cl/category/scat354867/parrillas-a-gas", "mr beef", "parrilla a gas 4 quemadores", "299990", "2831805", "jardín, pasillo 3 - rack 3"], ["aire libre-parrillas", "parrillas y quinchos", "parrillas a gas", "parrillas a gas", "parrillas a gas", "parrillas a gas", "parrillas a gas", "http://sodimac.scene7.com/is/image/sodimaccl/3104583?$lista175$", "http://www.sodimac.cl/sodimac-cl/category/scat354867/parrillas-a-gas", "mr beef", "parrilla a gas ny 4 quemadores 1 bandeja 1ql ac...", "199990", "3104583", "pasillo 1 - rack 1"], ["aire libre-parrillas", "parrillas y quinchos", "parrillas a gas", "parrillas a gas", "parrillas a gas", "parrillas a gas", "parrillas a gas", "http://sodimac.scene7.com/is/image/sodimaccl/2778874?$lista175$", "http://www.sodimac.cl/sodimac-cl/category/scat354867/parrillas-a-gas", "mr beef", "parrilla a gas 4 quemadores", "279990", "2778874", "jardín, pasillo 3 - rack 3"], ["aire libre-parrillas", "parrillas y quinchos", "parrillas a gas", "parrillas a gas", "parrillas a gas", "parrillas a gas", "parrillas a gas", "http://sodimac.scene7.com/is/image/sodimaccl/2877767?$lista175$", "http://www.sodimac.cl/sodimac-cl/category/scat354867/parrillas-a-gas", "mr beef", "parrilla a gas 3 quemadores", "169990", "2877767", "jardín, pasillo 3 - rack 3"], ["aire libre-parrillas", "parrillas y quinchos", "parrillas a gas", "parrillas a gas", "parrillas a gas", "parrillas a gas", "parrillas a gas", "http://sodimac.scene7.com/is/image/sodimaccl/2791129?$lista175$", "http://www.sodimac.cl/sodimac-cl/category/scat354867/parrillas-a-gas", "charbroil", "parrilla a gas 3 quemadores", "399990", "2791129", "jardín, pasillo 3 - rack 3"], ["aire libre-parrillas", "parrillas y quinchos", "parrillas a gas", "parrillas a gas", "parrillas a gas", "parrillas a gas", "parrillas a gas", "http://sodimac.scene7.com/is/image/sodimaccl/2777177?$lista175$", "http://www.sodimac.cl/sodimac-cl/category/scat354867/parrillas-a-gas", "karson", "parrilla a gas 2 quemadores", "49990", "2777177", "jardín, pasillo 3 - rack 3"], ["aire libre-parrillas", "parrillas y quinchos", "parrillas a gas", "parrillas a gas", "parrillas a gas", "parrillas a gas", "parrillas a gas", "http://sodimac.scene7.com/is/image/sodimaccl/2791110?$lista175$", "http://www.sodimac.cl/sodimac-cl/category/scat354867/parrillas-a-gas", "charbroil", "parrilla a gas 2 quemadores", "299990", "2791110", "jardín, pasillo 3 - rack 3"], ["aire libre-parrillas", "parrillas y quinchos", "braseros", "braseros", "braseros", "braseros", "braseros", "http://sodimac.scene7.com/is/image/sodimaccl/3049973?$lista175$", "http://www.sodimac.cl/sodimac-cl/category/cat520024/braseros?no=16&nrpp=16", "mr beef", "brasero de fibra con parrilla cuadrado", "89990", "3049973", "pasillo 2 - rack 2"], ["aire libre-parrillas", "parrillas y quinchos", "parrillas a carbón", "parrillas a carbón", "parrillas a carbón", "parrillas a carbón", "parrillas a carbón", "http://sodimac.scene7.com/is/image/sodimaccl/1458620?$lista175$", "http://www.sodimac.cl/sodimac-cl/category/scat354868/parrillas-a-carbon?no=32&nrpp=16", "mr beef", "parrilla a carbón con ahumador", "109990", "1458620", "jardín, pasillo 3 - rack 3"], ["aire libre-parrillas", "parrillas y quinchos", "parrillas a carbón", "parrillas a carbón", "parrillas a carbón", "parrillas a carbón", "parrillas a carbón", "http://sodimac.scene7.com/is/image/sodimaccl/1458639?$lista175$", "http://www.sodimac.cl/sodimac-cl/category/scat354868/parrillas-a-carbon?no=32&nrpp=16", "mr beef", "parrilla a carbón", "99990", "1458639", "jardín, pasillo 3 - rack 3"], ["aire libre-parrillas", "parrillas y quinchos", "parrillas a gas", "parrillas a gas", "parrillas a gas", "parrillas a gas", "parrillas a gas", "http://sodimac.scene7.com/is/image/sodimaccl/2777169?$lista175$", "http://www.sodimac.cl/sodimac-cl/category/scat354867/parrillas-a-gas?no=16&nrpp=16", "mr beef", "parrilla a gas 2 quemadores", "89990", "2777169", "jardín, pasillo 3 - rack 3"], ["aire libre-parrillas", "parrillas y quinchos", "parrillas a gas", "parrillas a gas", "parrillas a gas", "parrillas a gas", "parrillas a gas", "http://sodimac.scene7.com/is/image/sodimaccl/2854317?$lista175$", "http://www.sodimac.cl/sodimac-cl/category/scat354867/parrillas-a-gas?no=16&nrpp=16", "bbq grill", "parrilla a gas 4 quemadores para empotrar", "539000", "2854317", "pasillo 1 - rack 1"], ["aire libre-parrillas", "parrillas y quinchos", "parrillas a gas", "parrillas a gas", "parrillas a gas", "parrillas a gas", "parrillas a gas", "http://sodimac.scene7.com/is/image/sodimaccl/162220x?$lista175$", "http://www.sodimac.cl/sodimac-cl/category/scat354867/parrillas-a-gas?no=16&nrpp=16", "mr beef", "parrilla a gas 6 quemadores", "789990", "162220x", "pasillo 1 - rack 1"], ["aire libre-parrillas", "parrillas y quinchos", "accesorios de parrillas", "otros accesorios", "otros accesorios", "otros accesorios", "otros accesorios", "http://sodimac.scene7.com/is/image/sodimaccl/2929171?$lista175$", "http://www.sodimac.cl/sodimac-cl/category/cat5030014/otros-accesorios/?cid=cgoall60337", "mr beef", "lámpara magnética para parrilla", "6990", "2929171", "jardín, pasillo 3 - rack 3"], ["aire libre-parrillas", "parrillas y quinchos", "accesorios de parrillas", "otros accesorios", "otros accesorios", "otros accesorios", "otros accesorios", "http://sodimac.scene7.com/is/image/sodimaccl/292918x?$lista175$", "http://www.sodimac.cl/sodimac-cl/category/cat5030014/otros-accesorios/?cid=cgoall60337", "mr beef", "plancha de hierro con tabla para parrilla", "12790", "292918x", "pasillo 70 - rack 70"], ["aire libre-parrillas", "parrillas y quinchos", "accesorios de parrillas", "otros accesorios", "otros accesorios", "otros accesorios", "otros accesorios", "http://sodimac.scene7.com/is/image/sodimaccl/625280?$lista175$", "http://www.sodimac.cl/sodimac-cl/category/cat5030014/otros-accesorios/?cid=cgoall60337", "mr beef", "parrilla cuadrada de teflón mango de madera 23....", "4890", "625280", "jardín, pasillo 3 - rack 3"], ["aire libre-parrillas", "parrillas y quinchos", "accesorios de parrillas", "otros accesorios", "otros accesorios", "otros accesorios", "otros accesorios", "http://sodimac.scene7.com/is/image/sodimaccl/300886x?$lista175$", "http://www.sodimac.cl/sodimac-cl/category/cat5030014/otros-accesorios/?cid=cgoall60337", "char-broil", "funda para parrilla premium 2 quemadores", "12990", "300886x", "jardín, pasillo 3 - rack 3"], ["destacados", "imperdibles", "imperdibles", "imperdibles", "imperdibles", "imperdibles", "imperdibles", "http://sodimac.scene7.com/is/image/sodimaccl/2653877?$lista175$", "http://www.sodimac.cl/sodimac-cl/category/cat1990064/imperdibles?no=128&nrpp=16", "mr beef", "parrilla carbón rectangular 130x120x60", "119990", "2653877", "jardín, pasillo 3 - rack 3"], ["destacados", "imperdibles", "imperdibles", "imperdibles", "imperdibles", "imperdibles", "imperdibles", "http://sodimac.scene7.com/is/image/sodimaccl/2877953?$lista175$", "http://www.sodimac.cl/sodimac-cl/category/cat1990064/imperdibles?no=208&nrpp=16", "grillcorp", "caja china chica + parrilla de varillas", "79990", "2877953", "pasillo 2 - rack 2"]], "categoria_actual": 1},
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
if "Subcategor" in categorias_a_usuario[eleccion]:
    # elige la ultima (subcategorías), data se mantiene igual
    pass
else:
    print categorias_a_usuario[eleccion].encode('utf-8')
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
#print_sans(data)

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
print output
#print mensaje_final#.encode('utf-8')
response.write(output)
response.close()