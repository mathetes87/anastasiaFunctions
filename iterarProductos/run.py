#!/usr/bin/env python
# coding: utf-8
import json, csv, os

# inputs y outputs
try:
    from tabulate import tabulate
    post_data = json.loads(json.dumps({
        "head": ["Categoria 1", "Categoria 2", "Categoria 3", "Categoria 4", "Categoria 5", "Categoria 6", "Categoria 7", "Imagen Url", "url", "Marca", "Nombre", "Precio", "Sku", "pasillo"],
        "categoria": 2,
        "eleccion": 2,
        "data_productos": [["Aire libre-Parrillas", "Parrillas y Quinchos", "Braseros", "", "", "", "", "http://sodimac.scene7.com/is/image/SodimacCL/3049973?$lista175$", "http://www.sodimac.cl/sodimac-cl/category/cat520024/Braseros?No=16&Nrpp=16", "Mr Beef", "Brasero de fibra con parrilla cuadrado", "89990", "3049973", "Pasillo 2 - Rack 2"], ["Aire libre-Parrillas", "Parrillas y Quinchos", "Accesorios de Parrillas", "Otros Accesorios", "", "", "", "http://sodimac.scene7.com/is/image/SodimacCL/2929171?$lista175$", "http://www.sodimac.cl/sodimac-cl/category/cat5030014/Otros-Accesorios/?cid=cgoall60337", "Mr Beef", "Lámpara magnética para parrilla", "6990", "2929171", "Jardín, Pasillo 3 - Rack 3"], ["Aire libre-Parrillas", "Parrillas y Quinchos", "Accesorios de Parrillas", "Otros Accesorios", "", "", "", "http://sodimac.scene7.com/is/image/SodimacCL/292918X?$lista175$", "http://www.sodimac.cl/sodimac-cl/category/cat5030014/Otros-Accesorios/?cid=cgoall60337", "Mr Beef", "Plancha de hierro con tabla para parrilla", "12790", "292918X", "Pasillo 70 - Rack 70"], ["Aire libre-Parrillas", "Parrillas y Quinchos", "Accesorios de Parrillas", "Otros Accesorios", "", "", "", "http://sodimac.scene7.com/is/image/SodimacCL/300886X?$lista175$", "http://www.sodimac.cl/sodimac-cl/category/cat5030014/Otros-Accesorios/?cid=cgoall60337", "Char-Broil", "Funda para parrilla Premium 2 quemadores", "12990", "300886X", "Jardín, Pasillo 3 - Rack 3"], ["Destacados", "Imperdibles", "", "", "", "", "", "http://sodimac.scene7.com/is/image/SodimacCL/2877953?$lista175$", "http://www.sodimac.cl/sodimac-cl/category/cat1990064/Imperdibles?No=208&Nrpp=16", "Grillcorp", "Caja china chica + parrilla de varillas", "79990", "2877953", "Pasillo 2 - Rack 2"], ["Baño", "Cocina y Línea Blanca", "Baño", "Limpieza", "Detergentes y Limpiadores", "Limpiadores de cocina", "", "http://sodimac.scene7.com/is/image/SodimacCL/3095665?$lista175$", "http://www.sodimac.cl/sodimac-cl/category/cat4850292/Limpiadores-de-cocina", "Kleine", "Limpiador y desengrasante de parrillas 500 ml k...", "2990", "3095665", "Pasillo 51 - Rack 51"]]
    }))
except:
    post_data = json.loads(open(os.environ['req']).read())

# datos obtenidos de llamada
header = post_data['head']
categoria_actual = post_data['categoria']
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

print tabulate(data, headers=header)

n_categorias = n_categorias(header)

pasillos = set([row[header.index('pasillo')] for row in data])
if len(pasillos) > 1:
    # buscar donde bifurcan categorias
    for i in range(categoria_actual, n_categorias):
        index_categoria = header.index('Categoria '+str(i))
        categorias = set([row[index_categoria] for row in data])
        if len(categorias) > 1:
            # filtrar resultados
            if eleccion == -1:
                print "Indiferente", categoria_actual
                break
            else:
                data = [row for row in data if list(categorias)[eleccion-1] == row[index_categoria]]
                break
        else:
            continue
    # si salgo es que no puedo seguir filtrando por categorias y quedan pasillos distintos
    print "No se puede seguir filtrando por categorias"

if data:
    pasillos = list(set([row[header.index('pasillo')] for row in data]))
    if len(pasillos) > 1:
        seguir_filtrando = True
        print "Tenemos productos en distintos pasillos: {}".format(','.join(byteify(pasillos)))
    else:
        seguir_filtrando = False
        print "Ubicación del producto: {}".format(pasillos[0])

output = {
    'data': data,
    'seguir_filtrando': seguir_filtrando
}

output = json.dumps(byteify(output), ensure_ascii=False)

print ""
print output
response.write(output)
response.close()