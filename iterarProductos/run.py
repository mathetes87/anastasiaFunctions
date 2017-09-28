#!/usr/bin/env python
# coding: utf-8
import json, csv, os

# inputs y outputs
try:
    from tabulate import tabulate
    post_data = json.loads(json.dumps({
        "response": {"seguir_filtrando": True, "mensaje_final": "Podrás encontrar las u'sillas de fierro' que buscas en el ", "header": ["Categoria 1", "Categoria 2", "Categoria 3", "Categoria 4", "Categoria 5", "Categoria 6", "Categoria 7", "Imagen Url", "url", "Marca", "Nombre", "Precio", "Sku", "pasillo"], "categorias_a_usuario": ["imperdibles", "muebles", "molduras puertas y ventanas", "terrazas", "Subcategorías"], "data": [["muebles y decoración", "muebles", "muebles de comedor", "mesas de comedor", "mesas de comedor", "mesas de comedor", "mesas de comedor", "http://sodimac.scene7.com/is/image/sodimaccl/2314517?$lista175$", "http://www.sodimac.cl/sodimac-cl/category/scat887595/?cid=cgoall53086", "casa bonita", "comedor auxiliar 120x40x92 cm 2 sillas 3 repiza...", "39990", "2314517", "jardín, pasillo 13 - rack 13"], ["muebles y decoración", "muebles", "muebles de comedor", "mesas de comedor", "mesas de comedor", "mesas de comedor", "mesas de comedor", "http://sodimac.scene7.com/is/image/sodimaccl/1653407?$lista175$", "http://www.sodimac.cl/sodimac-cl/category/scat887595/?cid=cgoall53086", "hc", "comedor rectangular 110x70x76 cm 4 sillas", "49990", "1653407", "jardín, pasillo 13 - rack 13"], ["muebles y decoración", "muebles", "muebles de comedor", "juego de comedor", "juego de comedor", "juego de comedor", "juego de comedor", "http://sodimac.scene7.com/is/image/sodimaccl/3088898?$lista175$", "http://www.sodimac.cl/sodimac-cl/category/scat250758/?cid=cgoall53084", "home collection", "juego de comedor mesa + 4 sillas crista", "249990", "3088898", "jardín, pasillo 13 - rack 13"], ["muebles y decoración", "muebles", "muebles de comedor", "juego de comedor", "juego de comedor", "juego de comedor", "juego de comedor", "http://sodimac.scene7.com/is/image/sodimaccl/2681633?$lista175$", "http://www.sodimac.cl/sodimac-cl/category/scat250758/juego-de-comedor?no=16&nrpp=16", "home collection", "comedor dartagnan 6 sillas", "149990", "2681633", "jardín, pasillo 13 - rack 13"], ["molduras (marcos y guardapolvo)", "molduras puertas y ventanas", "molduras puertas y ventanas", "molduras puertas y ventanas", "molduras puertas y ventanas", "molduras puertas y ventanas", "molduras puertas y ventanas", "http://sodimac.scene7.com/is/image/sodimaccl/2508826?$lista175$", "http://www.sodimac.cl/sodimac-cl/category/cat4850349/molduras-puertas-y-ventanas?no=48&nrpp=16", "genérico", "moldura pino gu1 guardasilla 3 mt", "4290", "2508826", "pasillo 40 - rack 40"], ["destacados", "imperdibles", "muebles y organización", "muebles y organización", "muebles y organización", "muebles y organización", "muebles y organización", "http://sodimac.scene7.com/is/image/sodimaccl/2683873?$lista175$", "http://www.sodimac.cl/sodimac-cl/category/cat2000029/muebles-y-organizacion?nrpp=16&facetcat=categor%c3%ada&category=muebles%20y%20organizaci%c3%b3n", "asenti", "silla pc acrílico morado", "", "2683873", "pasillo 9 - rack 9"], ["destacados", "imperdibles", "muebles y organización", "muebles y organización", "muebles y organización", "muebles y organización", "muebles y organización", "http://sodimac.scene7.com/is/image/sodimaccl/2837846?$lista175$", "http://www.sodimac.cl/sodimac-cl/category/cat2000029/muebles-y-organizacion?nrpp=16&facetcat=categor%c3%ada&category=muebles%20y%20organizaci%c3%b3n", "asenti", "silla cayena", "", "2837846", "pasillo 9 - rack 9"], ["aire libre-parrillas", "terrazas", "muebles de exterior/terraza", "sillas y sillones de terraza", "sillas y sillones de terraza", "sillas y sillones de terraza", "sillas y sillones de terraza", "http://sodimac.scene7.com/is/image/sodimaccl/3153061?$lista175$", "http://www.sodimac.cl/sodimac-cl/category/scat546567/sillas-y-sillones-de-terraza?no=16&nrpp=16", "reyplast", "silla tavarua modelo ratán", "14990", "3153061", "pasillo 7 - rack 7"], ["aire libre-parrillas", "terrazas", "muebles de exterior/terraza", "sillas y sillones de terraza", "sillas y sillones de terraza", "sillas y sillones de terraza", "sillas y sillones de terraza", "http://sodimac.scene7.com/is/image/sodimaccl/3153096?$lista175$", "http://www.sodimac.cl/sodimac-cl/category/scat546567/sillas-y-sillones-de-terraza?no=16&nrpp=16", "reyplast", "silla blanca barcelona", "5990", "3153096", "pasillo 70 - rack 70"], ["aire libre-parrillas", "terrazas", "muebles de exterior/terraza", "sillas de terrazas", "sillas de terrazas", "sillas de terrazas", "sillas de terrazas", "http://sodimac.scene7.com/is/image/sodimaccl/3029263?$lista175$", "http://www.sodimac.cl/sodimac-cl/category/scat457298/?cid=cgoall52964", "home collection", "silla acacia/ratán pe bradford", "99990", "3029263", "pasillo 7 - rack 7"], ["aire libre-parrillas", "terrazas", "muebles de exterior/terraza", "sillas de terrazas", "sillas de terrazas", "sillas de terrazas", "sillas de terrazas", "http://sodimac.scene7.com/is/image/sodimaccl/3029204?$lista175$", "http://www.sodimac.cl/sodimac-cl/category/scat457298/?cid=cgoall52964", "home collection", "silla ratán pe/acacia tumbes", "99990", "3029204", "pasillo 7 - rack 7"], ["aire libre-parrillas", "terrazas", "muebles de exterior/terraza", "sillas de terrazas", "sillas de terrazas", "sillas de terrazas", "sillas de terrazas", "http://sodimac.scene7.com/is/image/sodimaccl/2971151?$lista175$", "http://www.sodimac.cl/sodimac-cl/category/scat457298/?cid=cgoall52964", "home collection", "silla ratán veracruz", "99990", "2971151", "pasillo 7 - rack 7"], ["aire libre-parrillas", "terrazas", "muebles de exterior/terraza", "sillas de terrazas", "sillas de terrazas", "sillas de terrazas", "sillas de terrazas", "http://sodimac.scene7.com/is/image/sodimaccl/3272826?$lista175$", "http://www.sodimac.cl/sodimac-cl/category/scat457298/sillas-de-terrazas?no=64&nrpp=16", "home collection", "silla polipropileno ramas grafito", "21990", "3272826", "pasillo 70 - rack 70"], ["aire libre-parrillas", "terrazas", "muebles de exterior/terraza", "sillas de terrazas", "sillas de terrazas", "sillas de terrazas", "sillas de terrazas", "http://sodimac.scene7.com/is/image/sodimaccl/3272818?$lista175$", "http://www.sodimac.cl/sodimac-cl/category/scat457298/sillas-de-terrazas?no=64&nrpp=16", "home collection", "silla polipropileno ramas blanco", "21990", "3272818", "pasillo 70 - rack 70"], ["aire libre-parrillas", "terrazas", "muebles de exterior/terraza", "sillas de terrazas", "sillas de terrazas", "sillas de terrazas", "sillas de terrazas", "http://sodimac.scene7.com/is/image/sodimaccl/3272796?$lista175$", "http://www.sodimac.cl/sodimac-cl/category/scat457298/sillas-de-terrazas?no=64&nrpp=16", "home collection", "silla polipropileno slats rojo", "19990", "3272796", "pasillo 70 - rack 70"], ["aire libre-parrillas", "terrazas", "muebles de exterior/terraza", "sillas de terrazas", "sillas de terrazas", "sillas de terrazas", "sillas de terrazas", "http://sodimac.scene7.com/is/image/sodimaccl/327280x?$lista175$", "http://www.sodimac.cl/sodimac-cl/category/scat457298/sillas-de-terrazas?no=64&nrpp=16", "home collection", "silla polipropileno slats taupe", "19990", "327280x", "pasillo 70 - rack 70"], ["aire libre-parrillas", "terrazas", "muebles de exterior/terraza", "sillas de terrazas", "sillas de terrazas", "sillas de terrazas", "sillas de terrazas", "http://sodimac.scene7.com/is/image/sodimaccl/3035514?$lista175$", "http://www.sodimac.cl/sodimac-cl/category/scat457298/sillas-de-terrazas?no=64&nrpp=16", "home collection", "silla plegable catania acacia", "16990", "3035514", "pasillo 7 - rack 7"], ["aire libre-parrillas", "terrazas", "muebles de exterior/terraza", "sillas de terrazas", "sillas de terrazas", "sillas de terrazas", "sillas de terrazas", "http://sodimac.scene7.com/is/image/sodimaccl/1468170?$lista175$", "http://www.sodimac.cl/sodimac-cl/category/scat457298/sillas-de-terrazas?no=48&nrpp=16", "home collection", "silla buque bambu natural negro", "34990", "1468170", "pasillo 7 - rack 7"], ["aire libre-parrillas", "terrazas", "muebles de exterior/terraza", "sillas de terrazas", "sillas de terrazas", "sillas de terrazas", "sillas de terrazas", "http://sodimac.scene7.com/is/image/sodimaccl/2779900?$lista175$", "http://www.sodimac.cl/sodimac-cl/category/scat457298/sillas-de-terrazas?no=80&nrpp=16", "home collection garden", "silla plegable spring rayas azul", "9990", "2779900", "pasillo 7 - rack 7"], ["aire libre-parrillas", "terrazas", "muebles de exterior/terraza", "sillas de terrazas", "sillas de terrazas", "sillas de terrazas", "sillas de terrazas", "http://sodimac.scene7.com/is/image/sodimaccl/698377?$lista175$", "http://www.sodimac.cl/sodimac-cl/category/scat457298/sillas-de-terrazas?no=80&nrpp=16", "home collection", "silla negra ratán de pe aplilable", "9990", "698377", "pasillo 7 - rack 7"], ["aire libre-parrillas", "terrazas", "muebles de exterior/terraza", "sillas de terrazas", "sillas de terrazas", "sillas de terrazas", "sillas de terrazas", "http://sodimac.scene7.com/is/image/sodimaccl/1292595?$lista175$", "http://www.sodimac.cl/sodimac-cl/category/scat457298/sillas-de-terrazas?no=80&nrpp=16", "home collection garden", "silla apilable metal negro-ratán de pvc café", "9990", "1292595", "pasillo 7 - rack 7"], ["aire libre-parrillas", "terrazas", "muebles de exterior/terraza", "sillas de terrazas", "sillas de terrazas", "sillas de terrazas", "sillas de terrazas", "http://sodimac.scene7.com/is/image/sodimaccl/3029190?$lista175$", "http://www.sodimac.cl/sodimac-cl/category/scat457298/sillas-de-terrazas/n-1z141uw?no=32&nrpp=16", "home collection", "silla acacia con apoya brazos brescia", "49990", "3029190", "pasillo 7 - rack 7"], ["aire libre-parrillas", "terrazas", "muebles de exterior/terraza", "sillas de terrazas", "sillas de terrazas", "sillas de terrazas", "sillas de terrazas", "http://sodimac.scene7.com/is/image/sodimaccl/2970007?$lista175$", "http://www.sodimac.cl/sodimac-cl/category/scat457298/sillas-de-terrazas/n-1z141uw?no=32&nrpp=16", "home collection", "silla cojín amalfi", "39990", "2970007", "pasillo 7 - rack 7"], ["aire libre-parrillas", "terrazas", "muebles de exterior/terraza", "sillas de terrazas", "sillas de terrazas", "sillas de terrazas", "sillas de terrazas", "http://sodimac.scene7.com/is/image/sodimaccl/2280272?$lista175$", "http://www.sodimac.cl/sodimac-cl/category/scat457298/sillas-de-terrazas/n-1z141uw?no=16&nrpp=16", "home collection", "silla aluminio-madera", "69990", "2280272", "pasillo 7 - rack 7"]], "categoria_actual": 2},
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
    mensaje_final = mensaje_final_parcial + '; '.join(pasillos)
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
print mensaje_final
response.write(output)
response.close()