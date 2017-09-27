#!/usr/bin/env python
# coding: utf-8
import json, csv, os

# inputs y outputs
try:
    from tabulate import tabulate
    post_data = json.loads(json.dumps({
        "response": {"seguir_filtrando": True, "header": ["Categoria 1", "Categoria 2", "Categoria 3", "Categoria 4", "Categoria 5", "Categoria 6", "Categoria 7", "Imagen Url", "url", "Marca", "Nombre", "Precio", "Sku", "pasillo"], "categorias_a_usuario": ["Herramientas de GasfiterÃ­a", "Bombas y Motobombas"], "ubicaciones": ["JardÃ­n, Pasillo 70 - Rack 70", "JardÃ­n, Pasillo 6 - Rack 6", "Pasillo 35 - Rack 35"], "data": [["ConstrucciÃ³n y Herramientas", "Materiales de ConstrucciÃ³n", "GasfiterÃ­a", "Herramientas de GasfiterÃ­a", "Otras Herramientas Manuales", "Otras Herramientas Manuales", "Otras Herramientas Manuales", "http://sodimac.scene7.com/is/image/SodimacCL/3147584?$lista175$", "http://www.sodimac.cl/sodimac-cl/category/cat4850374/Otras-Herramientas-Manuales", "Redline", "Tijera corte de manguera 38 mm", "10390", "3147584", "Pasillo 35 - Rack 35"], ["ConstrucciÃ³n y Herramientas", "Materiales de ConstrucciÃ³n", "GasfiterÃ­a", "Bombas y Motobombas", "Accesorios de Bombas", "Mangueras", "Manguera sin accesorios", "http://sodimac.scene7.com/is/image/SodimacCL/3129500?$lista175$", "http://www.sodimac.cl/sodimac-cl/category/cat5270002/Manguera-sin-accesorios", "Ergo", "Reparador manguera universal 1/2\" a 3/4\"", "1490", "3129500", "JardÃ­n, Pasillo 6 - Rack 6"], ["ConstrucciÃ³n y Herramientas", "Materiales de ConstrucciÃ³n", "GasfiterÃ­a", "Bombas y Motobombas", "Accesorios de Bombas", "Mangueras", "Manguera sin accesorios", "http://sodimac.scene7.com/is/image/SodimacCL/2894092?$lista175$", "http://www.sodimac.cl/sodimac-cl/category/cat5270002/Manguera-sin-accesorios", "Tramontina", "Manguera JardÃ­n 6m 1/2 sin accesorios", "3890", "2894092", "JardÃ­n, Pasillo 6 - Rack 6"], ["ConstrucciÃ³n y Herramientas", "Materiales de ConstrucciÃ³n", "GasfiterÃ­a", "Bombas y Motobombas", "Accesorios de Bombas", "Mangueras", "Manguera sin accesorios", "http://sodimac.scene7.com/is/image/SodimacCL/3174131?$lista175$", "http://www.sodimac.cl/sodimac-cl/category/cat5270002/Manguera-sin-accesorios", "Ergo", "Manguera bicolor 1/2 10 m sin accesorios", "3990", "3174131", "JardÃ­n, Pasillo 6 - Rack 6"], ["ConstrucciÃ³n y Herramientas", "Materiales de ConstrucciÃ³n", "GasfiterÃ­a", "Bombas y Motobombas", "Accesorios de Bombas", "Mangueras", "Manguera sin accesorios", "http://sodimac.scene7.com/is/image/SodimacCL/849839?$lista175$", "http://www.sodimac.cl/sodimac-cl/category/cat5270002/Manguera-sin-accesorios", "Rehau", "Set de manguera raucolor", "7690", "849839", "JardÃ­n, Pasillo 6 - Rack 6"], ["ConstrucciÃ³n y Herramientas", "Materiales de ConstrucciÃ³n", "GasfiterÃ­a", "Bombas y Motobombas", "Accesorios de Bombas", "Mangueras", "Manguera sin accesorios", "http://sodimac.scene7.com/is/image/SodimacCL/849871?$lista175$", "http://www.sodimac.cl/sodimac-cl/category/cat5270002/Manguera-sin-accesorios", "Rehau", "Set de manguera raucolor", "8790", "849871", "JardÃ­n, Pasillo 6 - Rack 6"], ["ConstrucciÃ³n y Herramientas", "Materiales de ConstrucciÃ³n", "GasfiterÃ­a", "Bombas y Motobombas", "Accesorios de Bombas", "Mangueras", "Manguera sin accesorios", "http://sodimac.scene7.com/is/image/SodimacCL/2447827?$lista175$", "http://www.sodimac.cl/sodimac-cl/category/cat5270002/Manguera-sin-accesorios", "GenÃ©rico", "Manguera Pocket Hose", "9990", "2447827", "JardÃ­n, Pasillo 6 - Rack 6"], ["ConstrucciÃ³n y Herramientas", "Materiales de ConstrucciÃ³n", "GasfiterÃ­a", "Bombas y Motobombas", "Accesorios de Bombas", "Mangueras", "Manguera sin accesorios", "http://sodimac.scene7.com/is/image/SodimacCL/3174565?$lista175$", "http://www.sodimac.cl/sodimac-cl/category/cat5270002/Manguera-sin-accesorios", "Ergo", "Manguera bicolor 1/2 30 m sin accesorios", "10990", "3174565", "JardÃ­n, Pasillo 6 - Rack 6"], ["ConstrucciÃ³n y Herramientas", "Materiales de ConstrucciÃ³n", "GasfiterÃ­a", "Bombas y Motobombas", "Accesorios de Bombas", "Mangueras", "Manguera sin accesorios", "http://sodimac.scene7.com/is/image/SodimacCL/2894106?$lista175$", "http://www.sodimac.cl/sodimac-cl/category/cat5270002/Manguera-sin-accesorios", "Tramontina", "Manguera JardÃ­n 20m 1/2 sin accesorios", "11290", "2894106", "JardÃ­n, Pasillo 6 - Rack 6"], ["ConstrucciÃ³n y Herramientas", "Materiales de ConstrucciÃ³n", "GasfiterÃ­a", "Bombas y Motobombas", "Accesorios de Bombas", "Mangueras", "Manguera con accesorios", "http://sodimac.scene7.com/is/image/SodimacCL/2894068?$lista175$", "http://www.sodimac.cl/sodimac-cl/category/cat5270001/Manguera-con-accesorios", "Tramontina", "Manguera JardÃ­n 10m con acople", "7490", "2894068", "JardÃ­n, Pasillo 6 - Rack 6"], ["ConstrucciÃ³n y Herramientas", "Materiales de ConstrucciÃ³n", "GasfiterÃ­a", "Bombas y Motobombas", "Accesorios de Bombas", "Mangueras", "Manguera con accesorios", "http://sodimac.scene7.com/is/image/SodimacCL/1550977?$lista175$", "http://www.sodimac.cl/sodimac-cl/category/cat5270001/Manguera-con-accesorios", "Tramontina", "Manguera reforzada con accesorios", "10990", "1550977", "JardÃ­n, Pasillo 6 - Rack 6"], ["ConstrucciÃ³n y Herramientas", "Materiales de ConstrucciÃ³n", "GasfiterÃ­a", "Bombas y Motobombas", "Accesorios de Bombas", "Mangueras", "Manguera con accesorios", "http://sodimac.scene7.com/is/image/SodimacCL/2894076?$lista175$", "http://www.sodimac.cl/sodimac-cl/category/cat5270001/Manguera-con-accesorios", "Tramontina", "Manguera JardÃ­n 20m con acople", "11990", "2894076", "JardÃ­n, Pasillo 6 - Rack 6"], ["ConstrucciÃ³n y Herramientas", "Materiales de ConstrucciÃ³n", "GasfiterÃ­a", "Bombas y Motobombas", "Accesorios de Bombas", "Mangueras", "Manguera con accesorios", "http://sodimac.scene7.com/is/image/SodimacCL/2894084?$lista175$", "http://www.sodimac.cl/sodimac-cl/category/cat5270001/Manguera-con-accesorios", "Tramontina", "Manguera JardÃ­n 25m con acople", "14990", "2894084", "JardÃ­n, Pasillo 6 - Rack 6"], ["ConstrucciÃ³n y Herramientas", "Materiales de ConstrucciÃ³n", "GasfiterÃ­a", "Bombas y Motobombas", "Accesorios de Bombas", "Mangueras", "Manguera con accesorios", "http://sodimac.scene7.com/is/image/SodimacCL/178136?$lista175$", "http://www.sodimac.cl/sodimac-cl/category/cat5270001/Manguera-con-accesorios", "Rehau", "Set de manguera Rausan 20 metros con accesorios", "17990", "178136", "JardÃ­n, Pasillo 6 - Rack 6"], ["ConstrucciÃ³n y Herramientas", "Materiales de ConstrucciÃ³n", "GasfiterÃ­a", "Bombas y Motobombas", "Accesorios de Bombas", "Mangueras", "Manguera con accesorios", "http://sodimac.scene7.com/is/image/SodimacCL/850098?$lista175$", "http://www.sodimac.cl/sodimac-cl/category/cat5270001/Manguera-con-accesorios", "Rehau", "Set de manguera raubiflex", "18990", "850098", "JardÃ­n, Pasillo 6 - Rack 6"], ["ConstrucciÃ³n y Herramientas", "Materiales de ConstrucciÃ³n", "GasfiterÃ­a", "Bombas y Motobombas", "Accesorios de Bombas", "Mangueras", "Manguera con accesorios", "http://sodimac.scene7.com/is/image/SodimacCL/2735245?$lista175$", "http://www.sodimac.cl/sodimac-cl/category/cat5270001/Manguera-con-accesorios", "Petroflex", "Manguera piscina 1 1/2 15m c/acc", "31490", "2735245", "JardÃ­n, Pasillo 70 - Rack 70"], ["ConstrucciÃ³n y Herramientas", "Materiales de ConstrucciÃ³n", "GasfiterÃ­a", "Bombas y Motobombas", "Accesorios de Bombas", "Mangueras", "Manguera sin accesorios", "http://sodimac.scene7.com/is/image/SodimacCL/1566172?$lista175$", "http://www.sodimac.cl/sodimac-cl/category/cat5270002/Manguera-sin-accesorios?No=16&Nrpp=16", "Dvp", "Manguera Helifrex 25 metros", "15990", "1566172", "JardÃ­n, Pasillo 6 - Rack 6"], ["ConstrucciÃ³n y Herramientas", "Materiales de ConstrucciÃ³n", "GasfiterÃ­a", "Bombas y Motobombas", "Accesorios de Bombas", "Mangueras", "Manguera sin accesorios", "http://sodimac.scene7.com/is/image/SodimacCL/167614?$lista175$", "http://www.sodimac.cl/sodimac-cl/category/cat5270002/Manguera-sin-accesorios?No=16&Nrpp=16", "Rehau", "Set de manguera rausan", "17490", "167614", "JardÃ­n, Pasillo 6 - Rack 6"], ["ConstrucciÃ³n y Herramientas", "Materiales de ConstrucciÃ³n", "GasfiterÃ­a", "Bombas y Motobombas", "Accesorios de Bombas", "Mangueras", "Manguera sin accesorios", "http://sodimac.scene7.com/is/image/SodimacCL/3174557?$lista175$", "http://www.sodimac.cl/sodimac-cl/category/cat5270002/Manguera-sin-accesorios?No=16&Nrpp=16", "Ergo", "Manguera bicolor 3/4 20 m sin accesorios", "19990", "3174557", "JardÃ­n, Pasillo 6 - Rack 6"]], "categoria_actual": 3},
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
    pop = [6,7, 8, 9, 11, 12]
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

print ""
print_sans(data)

output = {
    'data': data,
    'header': header,
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