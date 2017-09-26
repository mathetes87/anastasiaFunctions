#!/usr/bin/env python
# coding: utf-8
import json, csv, os

# inputs y outputs
try:
    from tabulate import tabulate
    post_data = json.loads(json.dumps({
        "header": ["Categoria 1", "Categoria 2", "Categoria 3", "Categoria 4", "Categoria 5", "Categoria 6", "Categoria 7", "Imagen Url", "url", "Marca", "Nombre", "Precio", "Sku", "pasillo"],
        "categoria_actual": 3,
        "categorias_a_usuario": ["Parrillas y Quinchos", "Imperdibles", "Cocina y Línea Blanca"],
        "eleccion": 3,
        "data_productos": [["Aire libre-Parrillas", "Parrillas y Quinchos", "Braseros", "Braseros", "Braseros", "Braseros", "Braseros", "http://sodimac.scene7.com/is/image/SodimacCL/3345130?$lista175$", "http://www.sodimac.cl/sodimac-cl/category/cat520024/Braseros-y-Discos", "Varvacoa", "Parrilla mesa brasero a carbón Ranco", "349990", "3345130", "Pasillo 1 - Rack 1"], ["Aire libre-Parrillas", "Parrillas y Quinchos", "Parrillas a Carbón", "Parrillas a Carbón", "Parrillas a Carbón", "Parrillas a Carbón", "Parrillas a Carbón", "http://sodimac.scene7.com/is/image/SodimacCL/1462733?$lista175$", "http://www.sodimac.cl/sodimac-cl/category/scat354868/Parrillas-a-Carbon", "Mr Beef", "Parrilla a carbón 40x35x34 cm", "18990", "1462733", "Jardín, Pasillo 3 - Rack 3"], ["Aire libre-Parrillas", "Parrillas y Quinchos", "Parrillas a Carbón", "Parrillas a Carbón", "Parrillas a Carbón", "Parrillas a Carbón", "Parrillas a Carbón", "http://sodimac.scene7.com/is/image/SodimacCL/1478869?$lista175$", "http://www.sodimac.cl/sodimac-cl/category/scat354868/Parrillas-a-Carbon", "Mr Beef", "Parrilla a Carbón 1/2 tambor con tapa", "30890", "1478869", "Jardín, Pasillo 3 - Rack 3"], ["Aire libre-Parrillas", "Parrillas y Quinchos", "Parrillas a Carbón", "Parrillas a Carbón", "Parrillas a Carbón", "Parrillas a Carbón", "Parrillas a Carbón", "http://sodimac.scene7.com/is/image/SodimacCL/1478885?$lista175$", "http://www.sodimac.cl/sodimac-cl/category/scat354868/Parrillas-a-Carbon", "Mr Beef", "Parrilla a Carbón 1/2 tambor con roldana", "19990", "1478885", "Jardín, Pasillo 3 - Rack 3"], ["Aire libre-Parrillas", "Parrillas y Quinchos", "Parrillas a Carbón", "Parrillas a Carbón", "Parrillas a Carbón", "Parrillas a Carbón", "Parrillas a Carbón", "http://sodimac.scene7.com/is/image/SodimacCL/177679?$lista175$", "http://www.sodimac.cl/sodimac-cl/category/scat354868/Parrillas-a-Carbon", "Mr Beef", "Parrilla a Carbón Circular", "8290", "177679", "Jardín, Pasillo 3 - Rack 3"], ["Aire libre-Parrillas", "Parrillas y Quinchos", "Parrillas a Carbón", "Parrillas a Carbón", "Parrillas a Carbón", "Parrillas a Carbón", "Parrillas a Carbón", "http://sodimac.scene7.com/is/image/SodimacCL/3247414?$lista175$", "http://www.sodimac.cl/sodimac-cl/category/scat354868/Parrillas-a-Carbon", "Mr Beef", "Parrilla a carbón PG-CG004", "79990", "3247414", "Jardín, Pasillo 70 - Rack 70"], ["Aire libre-Parrillas", "Parrillas y Quinchos", "Parrillas a Carbón", "Parrillas a Carbón", "Parrillas a Carbón", "Parrillas a Carbón", "Parrillas a Carbón", "http://sodimac.scene7.com/is/image/SodimacCL/672394?$lista175$", "http://www.sodimac.cl/sodimac-cl/category/scat354868/Parrillas-a-Carbon", "Mr Beef", "Parrilla carbón rectangular 66x36 x 26 cm. Ple...", "10990", "672394", "Jardín, Pasillo 3 - Rack 3"], ["Aire libre-Parrillas", "Parrillas y Quinchos", "Parrillas a Gas", "Parrillas a Gas", "Parrillas a Gas", "Parrillas a Gas", "Parrillas a Gas", "http://sodimac.scene7.com/is/image/SodimacCL/2747375?$lista175$", "http://www.sodimac.cl/sodimac-cl/category/scat354867/Parrillas-a-Gas", "Mr Beef", "Parrilla a gas 2 quemadores", "159990", "2747375", "Jardín, Pasillo 3 - Rack 3"], ["Aire libre-Parrillas", "Parrillas y Quinchos", "Parrillas a Gas", "Parrillas a Gas", "Parrillas a Gas", "Parrillas a Gas", "Parrillas a Gas", "http://sodimac.scene7.com/is/image/SodimacCL/2831805?$lista175$", "http://www.sodimac.cl/sodimac-cl/category/scat354867/Parrillas-a-Gas", "Mr Beef", "Parrilla a gas 4 quemadores", "299990", "2831805", "Jardín, Pasillo 3 - Rack 3"], ["Aire libre-Parrillas", "Parrillas y Quinchos", "Parrillas a Gas", "Parrillas a Gas", "Parrillas a Gas", "Parrillas a Gas", "Parrillas a Gas", "http://sodimac.scene7.com/is/image/SodimacCL/3104583?$lista175$", "http://www.sodimac.cl/sodimac-cl/category/scat354867/Parrillas-a-Gas", "Mr Beef", "Parrilla a gas ny 4 quemadores 1 bandeja 1ql ac...", "199990", "3104583", "Pasillo 1 - Rack 1"], ["Aire libre-Parrillas", "Parrillas y Quinchos", "Parrillas a Gas", "Parrillas a Gas", "Parrillas a Gas", "Parrillas a Gas", "Parrillas a Gas", "http://sodimac.scene7.com/is/image/SodimacCL/2778874?$lista175$", "http://www.sodimac.cl/sodimac-cl/category/scat354867/Parrillas-a-Gas", "Mr Beef", "Parrilla a gas 4 quemadores", "279990", "2778874", "Jardín, Pasillo 3 - Rack 3"], ["Aire libre-Parrillas", "Parrillas y Quinchos", "Parrillas a Gas", "Parrillas a Gas", "Parrillas a Gas", "Parrillas a Gas", "Parrillas a Gas", "http://sodimac.scene7.com/is/image/SodimacCL/2877767?$lista175$", "http://www.sodimac.cl/sodimac-cl/category/scat354867/Parrillas-a-Gas", "Mr Beef", "Parrilla a gas 3 quemadores", "169990", "2877767", "Jardín, Pasillo 3 - Rack 3"], ["Aire libre-Parrillas", "Parrillas y Quinchos", "Parrillas a Gas", "Parrillas a Gas", "Parrillas a Gas", "Parrillas a Gas", "Parrillas a Gas", "http://sodimac.scene7.com/is/image/SodimacCL/2791129?$lista175$", "http://www.sodimac.cl/sodimac-cl/category/scat354867/Parrillas-a-Gas", "Charbroil", "Parrilla a gas 3 quemadores", "399990", "2791129", "Jardín, Pasillo 3 - Rack 3"], ["Aire libre-Parrillas", "Parrillas y Quinchos", "Parrillas a Gas", "Parrillas a Gas", "Parrillas a Gas", "Parrillas a Gas", "Parrillas a Gas", "http://sodimac.scene7.com/is/image/SodimacCL/2777177?$lista175$", "http://www.sodimac.cl/sodimac-cl/category/scat354867/Parrillas-a-Gas", "Karson", "Parrilla a gas 2 quemadores", "49990", "2777177", "Jardín, Pasillo 3 - Rack 3"], ["Aire libre-Parrillas", "Parrillas y Quinchos", "Parrillas a Gas", "Parrillas a Gas", "Parrillas a Gas", "Parrillas a Gas", "Parrillas a Gas", "http://sodimac.scene7.com/is/image/SodimacCL/2791110?$lista175$", "http://www.sodimac.cl/sodimac-cl/category/scat354867/Parrillas-a-Gas", "Charbroil", "Parrilla a gas 2 quemadores", "299990", "2791110", "Jardín, Pasillo 3 - Rack 3"], ["Aire libre-Parrillas", "Parrillas y Quinchos", "Braseros", "Braseros", "Braseros", "Braseros", "Braseros", "http://sodimac.scene7.com/is/image/SodimacCL/3049973?$lista175$", "http://www.sodimac.cl/sodimac-cl/category/cat520024/Braseros?No=16&Nrpp=16", "Mr Beef", "Brasero de fibra con parrilla cuadrado", "89990", "3049973", "Pasillo 2 - Rack 2"], ["Aire libre-Parrillas", "Parrillas y Quinchos", "Parrillas a Carbón", "Parrillas a Carbón", "Parrillas a Carbón", "Parrillas a Carbón", "Parrillas a Carbón", "http://sodimac.scene7.com/is/image/SodimacCL/1458620?$lista175$", "http://www.sodimac.cl/sodimac-cl/category/scat354868/Parrillas-a-Carbon?No=32&Nrpp=16", "Mr Beef", "Parrilla a Carbón con Ahumador", "109990", "1458620", "Jardín, Pasillo 3 - Rack 3"], ["Aire libre-Parrillas", "Parrillas y Quinchos", "Parrillas a Carbón", "Parrillas a Carbón", "Parrillas a Carbón", "Parrillas a Carbón", "Parrillas a Carbón", "http://sodimac.scene7.com/is/image/SodimacCL/1458639?$lista175$", "http://www.sodimac.cl/sodimac-cl/category/scat354868/Parrillas-a-Carbon?No=32&Nrpp=16", "Mr Beef", "Parrilla a Carbón", "99990", "1458639", "Jardín, Pasillo 3 - Rack 3"], ["Aire libre-Parrillas", "Parrillas y Quinchos", "Parrillas a Gas", "Parrillas a Gas", "Parrillas a Gas", "Parrillas a Gas", "Parrillas a Gas", "http://sodimac.scene7.com/is/image/SodimacCL/2777169?$lista175$", "http://www.sodimac.cl/sodimac-cl/category/scat354867/Parrillas-a-Gas?No=16&Nrpp=16", "Mr Beef", "Parrilla a gas 2 quemadores", "89990", "2777169", "Jardín, Pasillo 3 - Rack 3"], ["Aire libre-Parrillas", "Parrillas y Quinchos", "Parrillas a Gas", "Parrillas a Gas", "Parrillas a Gas", "Parrillas a Gas", "Parrillas a Gas", "http://sodimac.scene7.com/is/image/SodimacCL/2854317?$lista175$", "http://www.sodimac.cl/sodimac-cl/category/scat354867/Parrillas-a-Gas?No=16&Nrpp=16", "BBQ Grill", "Parrilla a gas 4 quemadores para empotrar", "539000", "2854317", "Pasillo 1 - Rack 1"], ["Aire libre-Parrillas", "Parrillas y Quinchos", "Parrillas a Gas", "Parrillas a Gas", "Parrillas a Gas", "Parrillas a Gas", "Parrillas a Gas", "http://sodimac.scene7.com/is/image/SodimacCL/162220X?$lista175$", "http://www.sodimac.cl/sodimac-cl/category/scat354867/Parrillas-a-Gas?No=16&Nrpp=16", "Mr Beef", "Parrilla a gas 6 quemadores", "789990", "162220X", "Pasillo 1 - Rack 1"], ["Aire libre-Parrillas", "Parrillas y Quinchos", "Accesorios de Parrillas", "Otros Accesorios", "Otros Accesorios", "Otros Accesorios", "Otros Accesorios", "http://sodimac.scene7.com/is/image/SodimacCL/2929171?$lista175$", "http://www.sodimac.cl/sodimac-cl/category/cat5030014/Otros-Accesorios/?cid=cgoall60337", "Mr Beef", "Lámpara magnética para parrilla", "6990", "2929171", "Jardín, Pasillo 3 - Rack 3"], ["Aire libre-Parrillas", "Parrillas y Quinchos", "Accesorios de Parrillas", "Otros Accesorios", "Otros Accesorios", "Otros Accesorios", "Otros Accesorios", "http://sodimac.scene7.com/is/image/SodimacCL/292918X?$lista175$", "http://www.sodimac.cl/sodimac-cl/category/cat5030014/Otros-Accesorios/?cid=cgoall60337", "Mr Beef", "Plancha de hierro con tabla para parrilla", "12790", "292918X", "Pasillo 70 - Rack 70"], ["Aire libre-Parrillas", "Parrillas y Quinchos", "Accesorios de Parrillas", "Otros Accesorios", "Otros Accesorios", "Otros Accesorios", "Otros Accesorios", "http://sodimac.scene7.com/is/image/SodimacCL/625280?$lista175$", "http://www.sodimac.cl/sodimac-cl/category/cat5030014/Otros-Accesorios/?cid=cgoall60337", "Mr Beef", "Parrilla cuadrada de teflón mango de madera 23....", "4890", "625280", "Jardín, Pasillo 3 - Rack 3"], ["Aire libre-Parrillas", "Parrillas y Quinchos", "Accesorios de Parrillas", "Otros Accesorios", "Otros Accesorios", "Otros Accesorios", "Otros Accesorios", "http://sodimac.scene7.com/is/image/SodimacCL/300886X?$lista175$", "http://www.sodimac.cl/sodimac-cl/category/cat5030014/Otros-Accesorios/?cid=cgoall60337", "Char-Broil", "Funda para parrilla Premium 2 quemadores", "12990", "300886X", "Jardín, Pasillo 3 - Rack 3"], ["Destacados", "Imperdibles", "Imperdibles", "Imperdibles", "Imperdibles", "Imperdibles", "Imperdibles", "http://sodimac.scene7.com/is/image/SodimacCL/2653877?$lista175$", "http://www.sodimac.cl/sodimac-cl/category/cat1990064/Imperdibles?No=128&Nrpp=16", "Mr Beef", "Parrilla Carbón Rectangular 130x120x60", "119990", "2653877", "Jardín, Pasillo 3 - Rack 3"], ["Destacados", "Imperdibles", "Imperdibles", "Imperdibles", "Imperdibles", "Imperdibles", "Imperdibles", "http://sodimac.scene7.com/is/image/SodimacCL/2877953?$lista175$", "http://www.sodimac.cl/sodimac-cl/category/cat1990064/Imperdibles?No=208&Nrpp=16", "Grillcorp", "Caja china chica + parrilla de varillas", "79990", "2877953", "Pasillo 2 - Rack 2"], ["Baño", "Cocina y Línea Blanca", "Baño", "Limpieza", "Detergentes y Limpiadores", "Limpiadores de cocina", "Limpiadores de cocina", "http://sodimac.scene7.com/is/image/SodimacCL/3095665?$lista175$", "http://www.sodimac.cl/sodimac-cl/category/cat4850292/Limpiadores-de-cocina", "Kleine", "Limpiador y desengrasante de parrillas 500 ml k...", "2990", "3095665", "Pasillo 51 - Rack 51"]]
    }))
except:
    post_data = json.loads(open(os.environ['req']).read())

# datos obtenidos de llamada
header = post_data['header']
categoria_actual = post_data['categoria_actual']
categorias_a_usuario = post_data['categorias_a_usuario']
eleccion = post_data['eleccion']
data = post_data['data_productos']

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
    pop = [7, 8, 9, 11, 12]
    data_sans = [[col for i,col in enumerate(row) if i not in pop] for row in l]
    header_sans = [col for i,col in enumerate(header) if i not in pop]
    try:
        print tabulate(data_sans, headers=header_sans)
    except:
        pass

print_sans(data) 

n_categorias = n_categorias(header)

categorias_a_usuario = []
pasillos = list(set([row[header.index('pasillo')] for row in data]))
if len(pasillos) > 1:
    seguir_filtrando = True
    if eleccion == -1:
        # data se mantiene igual
        print "Indiferente", categoria_actual
        categoria_actual += 1
        categorias_a_usuario = list(set([row[categoria_actual-1] for row in data if row[categoria_actual-1] != '']))
    else:
        # buscar donde bifurcan categorias
        for i in range(categoria_actual, n_categorias):
            index_categoria = header.index('Categoria '+str(i))
            categorias = set([row[index_categoria] for row in data])
            if len(categorias) > 1:
                # filtrar resultados
                data = [row for row in data if list(categorias)[eleccion-1] == row[index_categoria]]
                categoria_actual += 1
                categorias_a_usuario = list(set([row[categoria_actual-1] for row in data if row[categoria_actual-1] != '']))
                break
            else:
                continue
        # si salgo es que no puedo seguir filtrando por categorias y quedan pasillos distintos
        print "No se puede seguir filtrando por categorias"
        seguir_filtrando = False

    if categoria_actual == n_categorias:
        seguir_filtrando = False
else:
    seguir_filtrando = False

output = {
    'data': data,
    'seguir_filtrando': seguir_filtrando,
    'categoria_actual': categoria_actual,
    'categorias_a_usuario': categorias_a_usuario
}

output = json.dumps(byteify(output), ensure_ascii=False)

print ""
print_sans(data)
print categorias_a_usuario
#print output
response.write(output)
response.close()