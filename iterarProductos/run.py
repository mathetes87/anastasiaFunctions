#!/usr/bin/env python
# coding: utf-8
import json, csv, os

# inputs y outputs
try:
    from tabulate import tabulate
    post_data = json.loads(json.dumps({
        "response": {"seguir_filtrando": True, "mensaje_final": "PodrÃ¡s encontrar el carbÃ³n que buscas en el ", "header": ["Categoria 1", "Categoria 2", "Categoria 3", "Categoria 4", "Categoria 5", "Categoria 6", "Categoria 7", "Imagen Url", "url", "Marca", "Nombre", "Precio", "Sku", "pasillo"], "categorias_a_usuario": ["ferreterÃ­a", "aire libre-parrillas", "SubcategorÃ­as"], "data": [["aire libre-parrillas", "parrillas y quinchos", "braseros", "braseros", "braseros", "braseros", "braseros", "http://sodimac.scene7.com/is/image/sodimaccl/3345130?$lista175$", "http://www.sodimac.cl/sodimac-cl/category/cat520024/braseros-y-discos", "varvacoa", "parrilla mesa brasero a carbÃ³n ranco", "349990", "3345130", "pasillo 1 - rack 1"], ["aire libre-parrillas", "parrillas y quinchos", "parrillas a carbÃ³n", "parrillas a carbÃ³n", "parrillas a carbÃ³n", "parrillas a carbÃ³n", "parrillas a carbÃ³n", "http://sodimac.scene7.com/is/image/sodimaccl/1462733?$lista175$", "http://www.sodimac.cl/sodimac-cl/category/scat354868/parrillas-a-carbon", "mr beef", "parrilla a carbÃ³n 40x35x34 cm", "18990", "1462733", "jardÃ­n, pasillo 3 - rack 3"], ["aire libre-parrillas", "parrillas y quinchos", "parrillas a carbÃ³n", "parrillas a carbÃ³n", "parrillas a carbÃ³n", "parrillas a carbÃ³n", "parrillas a carbÃ³n", "http://sodimac.scene7.com/is/image/sodimaccl/1478869?$lista175$", "http://www.sodimac.cl/sodimac-cl/category/scat354868/parrillas-a-carbon", "mr beef", "parrilla a carbÃ³n 1/2 tambor con tapa", "30890", "1478869", "jardÃ­n, pasillo 3 - rack 3"], ["aire libre-parrillas", "parrillas y quinchos", "parrillas a carbÃ³n", "parrillas a carbÃ³n", "parrillas a carbÃ³n", "parrillas a carbÃ³n", "parrillas a carbÃ³n", "http://sodimac.scene7.com/is/image/sodimaccl/1478885?$lista175$", "http://www.sodimac.cl/sodimac-cl/category/scat354868/parrillas-a-carbon", "mr beef", "parrilla a carbÃ³n 1/2 tambor con roldana", "19990", "1478885", "jardÃ­n, pasillo 3 - rack 3"], ["aire libre-parrillas", "parrillas y quinchos", "parrillas a carbÃ³n", "parrillas a carbÃ³n", "parrillas a carbÃ³n", "parrillas a carbÃ³n", "parrillas a carbÃ³n", "http://sodimac.scene7.com/is/image/sodimaccl/177679?$lista175$", "http://www.sodimac.cl/sodimac-cl/category/scat354868/parrillas-a-carbon", "mr beef", "parrilla a carbÃ³n circular", "8290", "177679", "jardÃ­n, pasillo 3 - rack 3"], ["aire libre-parrillas", "parrillas y quinchos", "parrillas a carbÃ³n", "parrillas a carbÃ³n", "parrillas a carbÃ³n", "parrillas a carbÃ³n", "parrillas a carbÃ³n", "http://sodimac.scene7.com/is/image/sodimaccl/3247414?$lista175$", "http://www.sodimac.cl/sodimac-cl/category/scat354868/parrillas-a-carbon", "mr beef", "parrilla a carbÃ³n pg-cg004", "79990", "3247414", "jardÃ­n, pasillo 70 - rack 70"], ["aire libre-parrillas", "parrillas y quinchos", "parrillas a carbÃ³n", "parrillas a carbÃ³n", "parrillas a carbÃ³n", "parrillas a carbÃ³n", "parrillas a carbÃ³n", "http://sodimac.scene7.com/is/image/sodimaccl/672394?$lista175$", "http://www.sodimac.cl/sodimac-cl/category/scat354868/parrillas-a-carbon", "mr beef", "parrilla carbÃ³n rectangular 66x36 x 26 cm. ple...", "10990", "672394", "jardÃ­n, pasillo 3 - rack 3"], ["aire libre-parrillas", "parrillas y quinchos", "parrillas a carbÃ³n", "parrillas a carbÃ³n", "parrillas a carbÃ³n", "parrillas a carbÃ³n", "parrillas a carbÃ³n", "http://sodimac.scene7.com/is/image/sodimaccl/1458620?$lista175$", "http://www.sodimac.cl/sodimac-cl/category/scat354868/parrillas-a-carbon?no=32&nrpp=16", "mr beef", "parrilla a carbÃ³n con ahumador", "109990", "1458620", "jardÃ­n, pasillo 3 - rack 3"], ["aire libre-parrillas", "parrillas y quinchos", "parrillas a carbÃ³n", "parrillas a carbÃ³n", "parrillas a carbÃ³n", "parrillas a carbÃ³n", "parrillas a carbÃ³n", "http://sodimac.scene7.com/is/image/sodimaccl/1458639?$lista175$", "http://www.sodimac.cl/sodimac-cl/category/scat354868/parrillas-a-carbon?no=32&nrpp=16", "mr beef", "parrilla a carbÃ³n", "99990", "1458639", "jardÃ­n, pasillo 3 - rack 3"], ["ferreterÃ­a", "herramientas", "herramientas elÃ©ctricas e inalÃ¡mbricas", "herramientas multipropÃ³sito", "accesorios de herramientas multipropÃ³sito", "accesorios de herramientas multipropÃ³sito", "accesorios de herramientas multipropÃ³sito", "http://sodimac.scene7.com/is/image/sodimaccl/65003x?$lista175$", "http://www.sodimac.cl/sodimac-cl/category/cat750180/?cid=cgoall54826", "dremel", "cepillo acero al carbÃ³n 12,7mm", "3390", "65003x", "pasillo 54 - rack 54"], ["ferreterÃ­a", "herramientas", "herramientas elÃ©ctricas e inalÃ¡mbricas", "herramientas multipropÃ³sito", "accesorios de herramientas multipropÃ³sito", "accesorios de herramientas multipropÃ³sito", "accesorios de herramientas multipropÃ³sito", "http://sodimac.scene7.com/is/image/sodimaccl/649511?$lista175$", "http://www.sodimac.cl/sodimac-cl/category/cat750180/accesorios-de-herramientas-multiproposito?no=16&nrpp=16", "dremel", "cepillo acero al carbÃ³n 19mm", "4190", "649511", "pasillo 54 - rack 54"]], "categoria_actual": 1},
        "eleccion": 2
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

print ""
print_sans(data)

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
print output
#print mensaje_final.encode('utf-8')
response.write(output)
response.close()