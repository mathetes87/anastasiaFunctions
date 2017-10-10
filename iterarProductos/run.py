#!/usr/bin/env python
# coding: utf-8
import json, csv, os

# inputs y outputs
try:
    from tabulate import tabulate
    post_data = json.loads(json.dumps({
        "response": {'seguir_filtrando': True, 'mensaje_final': 'Podr\xc3\xa1s encontrar los metales que buscas en el ', 'header': ['Categoria 1', 'Categoria 2', 'Categoria 3', 'Categoria 4', 'Categoria 5', 'Categoria 6', 'Categoria 7', 'Imagen Url', 'url', 'Marca', 'Nombre', 'Precio', 'Sku', 'pasillo'], 'categorias_a_usuario': ['construcci\xc3\xb3n y herramientas', 'ba\xc3\xb1o', 'muebles y decoraci\xc3\xb3n', 'electro y l\xc3\xadnea blanca', 'destacados', 'ferreter\xc3\xada', 'aire libre-parrillas', 'decohogar', 'Subcategor\xc3\xadas'], 'data': [['ba\xc3\xb1o', 'cocina y l\xc3\xadnea blanca', 'ba\xc3\xb1o', 'limpieza', 'detergentes y limpiadores', 'limpiadores espec\xc3\xadficos', '', 'http://sodimac.scene7.com/is/image/sodimaccl/557633?$lista175$', 'http://www.sodimac.cl/sodimac-cl/category/cat4850294/limpiadores-especificos/n-1z141uw?no=16&nrpp=16', 'brasso', 'limpiametales', '4990', '557633', 'pasillo 51 - rack 51'], ['destacados', 'imperdibles', 'imperdibles', 'imperdibles', 'imperdibles', 'imperdibles', 'imperdibles', 'http://sodimac.scene7.com/is/image/sodimaccl/2837005?$lista175$', 'http://www.sodimac.cl/sodimac-cl/category/cat1990064/?cid=bnnhom59899', 'gen\xc3\xa9rico', 'pack basurero metal pedal 12 + 20 lt', '', '2837005', 'pasillo 51 - rack 51'], ['destacados', 'imperdibles', 'imperdibles', 'imperdibles', 'imperdibles', 'imperdibles', 'imperdibles', 'http://sodimac.scene7.com/is/image/sodimaccl/2038218?$lista175$', 'http://www.sodimac.cl/sodimac-cl/category/cat1990064/imperdibles?no=96&nrpp=16', 'home collection', 'p\xc3\xa9rgola metal 300x300', '59990', '2038218', 'pasillo 7 - rack 7'], ['destacados', 'imperdibles', 'imperdibles', 'imperdibles', 'imperdibles', 'imperdibles', 'imperdibles', 'http://sodimac.scene7.com/is/image/sodimaccl/316962?$lista175$', 'http://www.sodimac.cl/sodimac-cl/category/cat1990064/imperdibles?no=80&nrpp=16', 'home collection', 'living mexico metal 4 piezas', '239990', '316962', 'pasillo 7 - rack 7'], ['destacados', 'imperdibles', 'imperdibles', 'imperdibles', 'imperdibles', 'imperdibles', 'imperdibles', 'http://sodimac.scene7.com/is/image/sodimaccl/203820x?$lista175$', 'http://www.sodimac.cl/sodimac-cl/category/cat1990064/imperdibles?no=112&nrpp=16', 'home collection', 'p\xc3\xa9rgola metal 300x300 cm blanco', '59990', '203820x', 'pasillo 7 - rack 7'], ['destacados', 'imperdibles', 'imperdibles', 'imperdibles', 'imperdibles', 'imperdibles', 'imperdibles', 'http://sodimac.scene7.com/is/image/sodimaccl/1844733?$lista175$', 'http://www.sodimac.cl/sodimac-cl/category/cat1990064/imperdibles?no=192&nrpp=16', 'home collection garden', 'p\xc3\xa9rgola metal rectangular de 295x395 cm.', '99990', '1844733', 'pasillo 7 - rack 7'], ['destacados', 'imperdibles', 'gasfiter\xc3\xada y ferreter\xc3\xada', 'gasfiter\xc3\xada y ferreter\xc3\xada', 'gasfiter\xc3\xada y ferreter\xc3\xada', 'gasfiter\xc3\xada y ferreter\xc3\xada', 'gasfiter\xc3\xada y ferreter\xc3\xada', 'http://sodimac.scene7.com/is/image/sodimaccl/2756501?$lista175$', 'http://www.sodimac.cl/sodimac-cl/category/cat2000019/gasfiteria-y-ferreteria?nrpp=16&facetcat=categor%c3%ada&category=gasfiter%c3%ada%20y%20ferreter%c3%ada', 'odis', 'cerradura sobreponer 773 con caja metal', '14990', '2756501', 'pasillo 44 - rack 44'], ['ferreter\xc3\xada', 'herramientas', 'herramientas por especialidad', 'herramientas para instalaci\xc3\xb3n de pisos', 'discos de corte y diamantado', 'discos de corte y diamantado', 'discos de corte y diamantado', 'http://sodimac.scene7.com/is/image/sodimaccl/674095?$lista175$', 'http://www.sodimac.cl/sodimac-cl/category/cat880069/discos-de-corte-y-diamantado', 'rasta', 'disco corte metal 4,5 mp', '990', '674095', 'pasillo 55 - rack 55'], ['ferreter\xc3\xada', 'herramientas', 'herramientas por especialidad', 'herramientas para instalaci\xc3\xb3n de pisos', 'discos de corte y diamantado', 'discos de corte y diamantado', 'discos de corte y diamantado', 'http://sodimac.scene7.com/is/image/sodimaccl/737453?$lista175$', 'http://www.sodimac.cl/sodimac-cl/category/cat880069/discos-de-corte-y-diamantado', 'de walt', 'disco de corte para metal 4,5 x 3/32', '1090', '737453', 'pasillo 55 - rack 55'], ['ferreter\xc3\xada', 'herramientas', 'herramientas por especialidad', 'herramientas para instalaci\xc3\xb3n de pisos', 'discos de corte y diamantado', 'discos de corte y diamantado', 'discos de corte y diamantado', 'http://sodimac.scene7.com/is/image/sodimaccl/1789872?$lista175$', 'http://www.sodimac.cl/sodimac-cl/category/cat880069/discos-de-corte-y-diamantado', 'bauker', "disco corte metal 4,5''", '1290', '1789872', 'pasillo 55 - rack 55'], ['ferreter\xc3\xada', 'herramientas', 'herramientas por especialidad', 'herramientas para instalaci\xc3\xb3n de pisos', 'discos de corte y diamantado', 'discos de corte y diamantado', 'discos de corte y diamantado', 'http://sodimac.scene7.com/is/image/sodimaccl/73747x?$lista175$', 'http://www.sodimac.cl/sodimac-cl/category/cat880069/discos-de-corte-y-diamantado', 'de walt', 'disco de corte para metal', '1290', '73747x', 'pasillo 55 - rack 55'], ['ferreter\xc3\xada', 'herramientas', 'herramientas por especialidad', 'herramientas para instalaci\xc3\xb3n de pisos', 'discos de corte y diamantado', 'discos de corte y diamantado', 'discos de corte y diamantado', 'http://sodimac.scene7.com/is/image/sodimaccl/720186?$lista175$', 'http://www.sodimac.cl/sodimac-cl/category/cat880069/discos-de-corte-y-diamantado', 'rasta', 'disco corte metal 7 mp', '1350', '720186', 'pasillo 55 - rack 55'], ['ferreter\xc3\xada', 'herramientas', 'herramientas el\xc3\xa9ctricas e inal\xc3\xa1mbricas', 'accesorios de herramientas el\xc3\xa9ctricas', 'lijadora y lijas', 'lijas', '', 'http://sodimac.scene7.com/is/image/sodimaccl/760250?$lista175$', 'http://www.sodimac.cl/sodimac-cl/category/scat358098/lijas?no=16&nrpp=16', 'isesa', 'lija para metal 60 granos 9" x 11"', '385', '760250', 'pasillo 32 - rack 32'], ['ferreter\xc3\xada', 'herramientas', 'herramientas el\xc3\xa9ctricas e inal\xc3\xa1mbricas', 'accesorios de herramientas el\xc3\xa9ctricas', 'lijadora y lijas', 'lijas', '', 'http://sodimac.scene7.com/is/image/sodimaccl/760242?$lista175$', 'http://www.sodimac.cl/sodimac-cl/category/scat358098/lijas?no=16&nrpp=16', 'isesa', 'lija para metal 80 granos 9" x 11"', '385', '760242', 'pasillo 32 - rack 32'], ['ferreter\xc3\xada', 'herramientas', 'herramientas el\xc3\xa9ctricas e inal\xc3\xa1mbricas', 'accesorios de herramientas el\xc3\xa9ctricas', 'lijadora y lijas', 'lijas', '', 'http://sodimac.scene7.com/is/image/sodimaccl/76020x?$lista175$', 'http://www.sodimac.cl/sodimac-cl/category/scat358098/lijas?no=16&nrpp=16', 'isesa', 'lija para metal 9" x 11" n\xc2\xba 40', '385', '76020x', 'pasillo 32 - rack 32'], ['ferreter\xc3\xada', 'herramientas', 'herramientas el\xc3\xa9ctricas e inal\xc3\xa1mbricas', 'accesorios de herramientas el\xc3\xa9ctricas', 'lijadora y lijas', 'lijas', '', 'http://sodimac.scene7.com/is/image/sodimaccl/760234?$lista175$', 'http://www.sodimac.cl/sodimac-cl/category/scat358098/lijas?no=16&nrpp=16', 'isesa', 'lija para metal 100 granos 9" x 11"', '385', '760234', 'pasillo 32 - rack 32'], ['ferreter\xc3\xada', 'herramientas', 'herramientas el\xc3\xa9ctricas e inal\xc3\xa1mbricas', 'accesorios de herramientas el\xc3\xa9ctricas', 'lijadora y lijas', 'lijas', '', 'http://sodimac.scene7.com/is/image/sodimaccl/243949?$lista175$', 'http://www.sodimac.cl/sodimac-cl/category/scat358098/lijas?no=16&nrpp=16', 'isesa', 'lija para metal 180 granos 9" x 11"', '385', '243949', 'pasillo 32 - rack 32'], ['ferreter\xc3\xada', 'herramientas', 'herramientas el\xc3\xa9ctricas e inal\xc3\xa1mbricas', 'accesorios de herramientas el\xc3\xa9ctricas', 'lijadora y lijas', 'lijas', '', 'http://sodimac.scene7.com/is/image/sodimaccl/760218?$lista175$', 'http://www.sodimac.cl/sodimac-cl/category/scat358098/lijas?no=16&nrpp=16', 'isesa', 'lija para metal 150 granos 9" x 11"', '385', '760218', 'pasillo 32 - rack 32'], ['ferreter\xc3\xada', 'herramientas', 'herramientas el\xc3\xa9ctricas e inal\xc3\xa1mbricas', 'accesorios de herramientas el\xc3\xa9ctricas', 'lijadora y lijas', 'lijas', '', 'http://sodimac.scene7.com/is/image/sodimaccl/760226?$lista175$', 'http://www.sodimac.cl/sodimac-cl/category/scat358098/lijas?no=16&nrpp=16', 'isesa', 'lija para metal 120 granos 9" x 11"', '385', '760226', 'pasillo 70 - rack 70'], ['ferreter\xc3\xada', 'herramientas', 'herramientas el\xc3\xa9ctricas e inal\xc3\xa1mbricas', 'accesorios de herramientas el\xc3\xa9ctricas', 'lijadora y lijas', 'lijas', '', 'http://sodimac.scene7.com/is/image/sodimaccl/760196?$lista175$', 'http://www.sodimac.cl/sodimac-cl/category/scat358098/lijas?no=16&nrpp=16', 'isesa', 'lija para metal 9" x 11" n\xc2\xba 50', '385', '760196', 'pasillo 32 - rack 32'], ['ferreter\xc3\xada', 'herramientas', 'herramientas por especialidad', 'herramientas para instalaci\xc3\xb3n de pisos', 'discos de corte y diamantado', 'discos de corte y diamantado', 'discos de corte y diamantado', 'http://sodimac.scene7.com/is/image/sodimaccl/856711?$lista175$', 'http://www.sodimac.cl/sodimac-cl/category/cat880069/discos-de-corte-y-diamantado/n-1z141uw?no=32&nrpp=16', 'rasta', 'disco corte metal 14 mp', '7170', '856711', 'pasillo 55 - rack 55'], ['ferreter\xc3\xada', 'herramientas', 'herramientas por especialidad', 'herramientas para instalaci\xc3\xb3n de pisos', 'discos de corte y diamantado', 'discos de corte y diamantado', 'discos de corte y diamantado', 'http://sodimac.scene7.com/is/image/sodimaccl/687650?$lista175$', 'http://www.sodimac.cl/sodimac-cl/category/cat880069/discos-de-corte-y-diamantado/n-1z141uw?no=16&nrpp=16', 'bosch', "disco corte metal 4,5''", '1690', '687650', 'pasillo 55 - rack 55'], ['ferreter\xc3\xada', 'herramientas', 'herramientas por especialidad', 'herramientas para instalaci\xc3\xb3n de pisos', 'discos de corte y diamantado', 'discos de corte y diamantado', 'discos de corte y diamantado', 'http://sodimac.scene7.com/is/image/sodimaccl/67415x?$lista175$', 'http://www.sodimac.cl/sodimac-cl/category/cat880069/discos-de-corte-y-diamantado/n-1z141uw?no=16&nrpp=16', 'rasta', 'disco corte metal 9 mp', '2490', '67415x', 'pasillo 55 - rack 55'], ['aire libre-parrillas', 'terrazas', 'quitasoles', 'toldos y p\xc3\xa9rgolas', 'toldos y p\xc3\xa9rgolas', 'toldos y p\xc3\xa9rgolas', 'toldos y p\xc3\xa9rgolas', 'http://sodimac.scene7.com/is/image/sodimaccl/1292617?$lista175$', 'http://www.sodimac.cl/sodimac-cl/category/scat273724/quitasoles,-toldos-y-pergolas?no=64&nrpp=16', 'home collection garden', 'quitasol circular metal d=200', '19990', '1292617', 'pasillo 7 - rack 7'], ['aire libre-parrillas', 'terrazas', 'quitasoles', 'toldos y p\xc3\xa9rgolas', 'toldos y p\xc3\xa9rgolas', 'toldos y p\xc3\xa9rgolas', 'toldos y p\xc3\xa9rgolas', 'http://sodimac.scene7.com/is/image/sodimaccl/578673?$lista175$', 'http://www.sodimac.cl/sodimac-cl/category/scat273724/quitasoles,-toldos-y-pergolas?no=64&nrpp=16', 'home collection garden', 'toldo piramidal metal 300x300', '19990', '578673', 'pasillo 7 - rack 7'], ['aire libre-parrillas', 'terrazas', 'quitasoles', 'toldos y p\xc3\xa9rgolas', 'toldos y p\xc3\xa9rgolas', 'toldos y p\xc3\xa9rgolas', 'toldos y p\xc3\xa9rgolas', 'http://sodimac.scene7.com/is/image/sodimaccl/578711?$lista175$', 'http://www.sodimac.cl/sodimac-cl/category/scat273724/quitasoles,-toldos-y-pergolas?no=64&nrpp=16', 'home collection garden', 'toldo piramidal metal 300x300', '19990', '578711', 'pasillo 7 - rack 7'], ['aire libre-parrillas', 'terrazas', 'quitasoles', 'toldos y p\xc3\xa9rgolas', 'toldos y p\xc3\xa9rgolas', 'toldos y p\xc3\xa9rgolas', 'toldos y p\xc3\xa9rgolas', 'http://sodimac.scene7.com/is/image/sodimaccl/225088?$lista175$', 'http://www.sodimac.cl/sodimac-cl/category/scat273724/quitasoles,-toldos-y-pergolas?no=48&nrpp=16', 'home collection', 'quitasol circular metal di\xc3\xa1metro 270 cm', '29990', '225088', 'pasillo 7 - rack 7'], ['aire libre-parrillas', 'terrazas', 'quitasoles', 'toldos y p\xc3\xa9rgolas', 'toldos y p\xc3\xa9rgolas', 'toldos y p\xc3\xa9rgolas', 'toldos y p\xc3\xa9rgolas', 'http://sodimac.scene7.com/is/image/sodimaccl/668133?$lista175$', 'http://www.sodimac.cl/sodimac-cl/category/scat273724/quitasoles,-toldos-y-pergolas?no=48&nrpp=16', 'home collection', 'quitasol circular metal di\xc3\xa1metro=270', '29990', '668133', 'pasillo 7 - rack 7'], ['aire libre-parrillas', 'terrazas', 'quitasoles', 'toldos y p\xc3\xa9rgolas', 'toldos y p\xc3\xa9rgolas', 'toldos y p\xc3\xa9rgolas', 'toldos y p\xc3\xa9rgolas', 'http://sodimac.scene7.com/is/image/sodimaccl/113646?$lista175$', 'http://www.sodimac.cl/sodimac-cl/category/scat273724/quitasoles,-toldos-y-pergolas?no=80&nrpp=16', 'home collection garden', 'toldo piramidal metal 300x300', '12990', '113646', 'pasillo 7 - rack 7'], ['muebles y decoraci\xc3\xb3n', 'muebles', 'iluminaci\xc3\xb3n', 'iluminaci\xc3\xb3n para tu negocio', 'l\xc3\xa1mparas de interior para tu negocio', 'l\xc3\xa1mparas de interior para tu negocio', 'l\xc3\xa1mparas de interior para tu negocio', 'http://sodimac.scene7.com/is/image/sodimaccl/2264552?$lista175$', 'http://www.sodimac.cl/sodimac-cl/category/cat3560018/lamparas-de-interior-para-tu-negocio?no=64&nrpp=16', 'philips', 'foco zinna metal/vidrio 2l', '24990', '2264552', 'pasillo 16 - rack 16'], ['aire libre-parrillas', 'iluminaci\xc3\xb3n exterior', 'reflectores y proyectores', 'proyectores industriales', 'proyectores industriales', 'proyectores industriales', 'proyectores industriales', 'http://sodimac.scene7.com/is/image/sodimaccl/1021613?$lista175$', 'http://www.sodimac.cl/sodimac-cl/category/cat4850463/proyectores-industriales', 'halux', 'proyector halurometal 400w', '46590', '1021613', 'pasillo 20 - rack 20'], ['destacados', 'destacados tecnolog\xc3\xada', 'destacados tecnolog\xc3\xada', 'destacados tecnolog\xc3\xada', 'destacados tecnolog\xc3\xada', 'destacados tecnolog\xc3\xada', 'destacados tecnolog\xc3\xada', 'http://sodimac.scene7.com/is/image/sodimaccl/948594?$lista175$', 'http://www.sodimac.cl/sodimac-cl/category/cat4850001/', 'kocom', 'set 1 cit\xc3\xb3fono + placa alta voz metal', '30990', '948594', 'pasillo 49 - rack 49'], ['destacados', 'destacados tecnolog\xc3\xada', 'destacados tecnolog\xc3\xada', 'destacados tecnolog\xc3\xada', 'destacados tecnolog\xc3\xada', 'destacados tecnolog\xc3\xada', 'destacados tecnolog\xc3\xada', 'http://sodimac.scene7.com/is/image/sodimaccl/74772?$lista175$', 'http://www.sodimac.cl/sodimac-cl/category/cat4850001/', 'commax', 'set 2 cit\xc3\xb3fonos + placa alta voz metal ffodp-ra01', '64990', '74772', 'pasillo 49 - rack 49'], ['electro y l\xc3\xadnea blanca', 'tecnolog\xc3\xada', 'control de acceso y seguridad', 'citofon\xc3\xada y timbres', 'al\xc3\xa1mbrico', 'al\xc3\xa1mbrico', 'al\xc3\xa1mbrico', 'http://sodimac.scene7.com/is/image/sodimaccl/74594?$lista175$', 'http://www.sodimac.cl/sodimac-cl/category/cat2940028/alambrico', 'commax', 'set 1 cit\xc3\xb3fono + placa alta voz metal ffodp-201r', '36490', '74594', 'pasillo 49 - rack 49'], ['electro y l\xc3\xadnea blanca', 'tecnolog\xc3\xada', 'control de acceso y seguridad', 'citofon\xc3\xada y timbres', 'al\xc3\xa1mbrico', 'al\xc3\xa1mbrico', 'al\xc3\xa1mbrico', 'http://sodimac.scene7.com/is/image/sodimaccl/593443?$lista175$', 'http://www.sodimac.cl/sodimac-cl/category/cat2940028/alambrico', 'commax', 'set 1 cit\xc3\xb3fono + placa alta voz metal ffodp-201rg', '40790', '593443', 'pasillo 49 - rack 49'], ['electro y l\xc3\xadnea blanca', 'tecnolog\xc3\xada', 'control de acceso y seguridad', 'citofon\xc3\xada y timbres', 'al\xc3\xa1mbrico', 'al\xc3\xa1mbrico', 'al\xc3\xa1mbrico', 'http://sodimac.scene7.com/is/image/sodimaccl/593451?$lista175$', 'http://www.sodimac.cl/sodimac-cl/category/cat2940028/alambrico', 'commax', 'set 2 cit\xc3\xb3fonos + placa alta voz metal ffodp-rao1r', '53990', '593451', 'pasillo 49 - rack 49'], ['aire libre-parrillas', 'decoracion de jard\xc3\xadn', 'flores y plantas artificiales', 'accesorios para flores artificiales', 'accesorios para flores artificiales', 'accesorios para flores artificiales', 'accesorios para flores artificiales', 'http://sodimac.scene7.com/is/image/sodimaccl/577308?$lista175$', 'http://www.sodimac.cl/sodimac-cl/category/cat4850006/accesorios-para-flores-artificiales', 'casa bonita', 'campana viento metal y madera 79 cm', '11990', '577308', 'jard\xc3\xadn, pasillo 3 - rack 3'], ['aire libre-parrillas', 'decoracion de jard\xc3\xadn', 'flores y plantas artificiales', 'accesorios para flores artificiales', 'accesorios para flores artificiales', 'accesorios para flores artificiales', 'accesorios para flores artificiales', 'http://sodimac.scene7.com/is/image/sodimaccl/577316?$lista175$', 'http://www.sodimac.cl/sodimac-cl/category/cat4850006/accesorios-para-flores-artificiales', 'casa bonita', 'campana viento metal y madera 107 cm', '17990', '577316', 'jard\xc3\xadn, pasillo 3 - rack 3'], ['ba\xc3\xb1o', 'cocina y l\xc3\xadnea blanca', 'ba\xc3\xb1o', 'limpieza', 'utensilios de aseo', 'escobas y escobillones', '', 'http://sodimac.scene7.com/is/image/sodimaccl/3006395?$lista175$', 'http://www.sodimac.cl/sodimac-cl/category/scat347954/escobas-y-escobillones?no=32&nrpp=16', 'kleine', 'escobill\xc3\xb3n municipal metal/pvc mango met\xc3\xa1lico 3...', '21990', '3006395', 'pasillo 51 - rack 51'], ['ba\xc3\xb1o', 'cocina y l\xc3\xadnea blanca', 'ba\xc3\xb1o', 'limpieza', 'utensilios de aseo', 'escobas y escobillones', '', 'http://sodimac.scene7.com/is/image/sodimaccl/2101580?$lista175$', 'http://www.sodimac.cl/sodimac-cl/category/scat347954/escobas-y-escobillones?no=16&nrpp=16', 'kleine', 'pala de basura metalica', '6990', '2101580', 'pasillo 51 - rack 51'], ['ba\xc3\xb1o', 'cocina y l\xc3\xadnea blanca', 'ba\xc3\xb1o', 'limpieza', 'utensilios de aseo', 'escobas y escobillones', '', 'http://sodimac.scene7.com/is/image/sodimaccl/3006409?$lista175$', 'http://www.sodimac.cl/sodimac-cl/category/scat347954/escobas-y-escobillones?no=16&nrpp=16', 'kleine', 'escobill\xc3\xb3n municipal metal/pvc mango met\xc3\xa1lico 8...', '9990', '3006409', 'pasillo 51 - rack 51'], ['construcci\xc3\xb3n y herramientas', 'materiales de construcci\xc3\xb3n', 'gasfiter\xc3\xada', 'grifer\xc3\xada', 'grifer\xc3\xada de cocina y lavadero', 'grifer\xc3\xada de cocina', '', 'http://sodimac.scene7.com/is/image/sodimaccl/2721821?$lista175$', 'http://www.sodimac.cl/sodimac-cl/category/scat293694/', 'stretto', 'combinaci\xc3\xb3n lavaplatos mossini metal tipo v', '15990', '2721821', 'pasillo 29 - rack 29'], ['aire libre-parrillas', 'terrazas', 'juegos de balcon', 'juegos de balcon', 'juegos de balcon', 'juegos de balcon', 'juegos de balcon', 'http://sodimac.scene7.com/is/image/sodimaccl/2049589?$lista175$', 'http://www.sodimac.cl/sodimac-cl/category/scat994164/?cid=cgoall52961', 'home collection garden', 'comedor balc\xc3\xb3n metal-textileno 3 piezas', '39990', '2049589', 'pasillo 7 - rack 7'], ['aire libre-parrillas', 'terrazas', 'juegos de balcon', 'juegos de balcon', 'juegos de balcon', 'juegos de balcon', 'juegos de balcon', 'http://sodimac.scene7.com/is/image/sodimaccl/1157353?$lista175$', 'http://www.sodimac.cl/sodimac-cl/category/scat994164/?cid=cgoall52961', 'home collection garden', 'comedor roma metal 3 piezas', '79990', '1157353', 'pasillo 7 - rack 7'], ['aire libre-parrillas', 'terrazas', 'juegos de balcon', 'juegos de balcon', 'juegos de balcon', 'juegos de balcon', 'juegos de balcon', 'http://sodimac.scene7.com/is/image/sodimaccl/1844520?$lista175$', 'http://www.sodimac.cl/sodimac-cl/category/scat994164/juegos-de-balcon?no=16&nrpp=16', 'home collection garden', 'comedor madrid metal 3 piezas', '59990', '1844520', 'pasillo 70 - rack 70'], ['aire libre-parrillas', 'terrazas', 'muebles de exterior/terraza', 'sillas de terrazas', 'sillas de terrazas', 'sillas de terrazas', 'sillas de terrazas', 'http://sodimac.scene7.com/is/image/sodimaccl/1292595?$lista175$', 'http://www.sodimac.cl/sodimac-cl/category/scat457298/sillas-de-terrazas?no=80&nrpp=16', 'home collection garden', 'silla apilable metal negro-rat\xc3\xa1n de pvc caf\xc3\xa9', '9990', '1292595', 'pasillo 7 - rack 7'], ['muebles y decoraci\xc3\xb3n', 'muebles', 'iluminaci\xc3\xb3n', 'iluminaci\xc3\xb3n interior', 'l\xc3\xa1mparas de pie', 'l\xc3\xa1mparas de pie', 'l\xc3\xa1mparas de pie', 'http://sodimac.scene7.com/is/image/sodimaccl/2715716?$lista175$', 'http://www.sodimac.cl/sodimac-cl/category/cat520042/lamparas-de-pie/?cid=cgoall57646', 'home collection', 'l\xc3\xa1mpara de pie metal 1 luz e27 gris', '17990', '2715716', 'pasillo 18 - rack 18'], ['muebles y decoraci\xc3\xb3n', 'muebles', 'iluminaci\xc3\xb3n', 'iluminaci\xc3\xb3n interior', 'lamparas de mesa y velador', 'lamparas de mesa y velador', 'lamparas de mesa y velador', 'http://sodimac.scene7.com/is/image/sodimaccl/2879379?$lista175$', 'http://www.sodimac.cl/sodimac-cl/category/cat520046/lamparas-de-mesa-y-velador?no=64&nrpp=16', 'casa bonita', 'pack 2 l\xc3\xa1mpara de mesa metal lille e27', '25990', '2879379', 'pasillo 18 - rack 18'], ['muebles y decoraci\xc3\xb3n', 'muebles', 'iluminaci\xc3\xb3n', 'iluminaci\xc3\xb3n interior', 'lamparas de mesa y velador', 'lamparas de mesa y velador', 'lamparas de mesa y velador', 'http://sodimac.scene7.com/is/image/sodimaccl/2858991?$lista175$', 'http://www.sodimac.cl/sodimac-cl/category/cat520046/lamparas-de-mesa-y-velador?no=96&nrpp=16', 'casa bonita', 'l\xc3\xa1mpara de mesa metal blanca e27', '19990', '2858991', 'pasillo 16 - rack 16'], ['muebles y decoraci\xc3\xb3n', 'muebles', 'iluminaci\xc3\xb3n', 'iluminaci\xc3\xb3n interior', 'lamparas de mesa y velador', 'lamparas de mesa y velador', 'lamparas de mesa y velador', 'http://sodimac.scene7.com/is/image/sodimaccl/2715759?$lista175$', 'http://www.sodimac.cl/sodimac-cl/category/cat520046/lamparas-de-mesa-y-velador?no=80&nrpp=16', 'home collection', 'l\xc3\xa1mpara de mesa metal regulable 1 luz e27', '21990', '2715759', 'pasillo 16 - rack 16'], ['muebles y decoraci\xc3\xb3n', 'muebles', 'iluminaci\xc3\xb3n', 'iluminaci\xc3\xb3n interior', 'lamparas de mesa y velador', 'lamparas de mesa y velador', 'lamparas de mesa y velador', 'http://sodimac.scene7.com/is/image/sodimaccl/2715961?$lista175$', 'http://www.sodimac.cl/sodimac-cl/category/cat520046/lamparas-de-mesa-y-velador?no=128&nrpp=16', 'home collection', 'l\xc3\xa1mpara de mesa metal cilindrica gris e27', '13990', '2715961', 'pasillo 18 - rack 18'], ['muebles y decoraci\xc3\xb3n', 'muebles', 'iluminaci\xc3\xb3n', 'iluminaci\xc3\xb3n interior', 'lamparas de mesa y velador', 'lamparas de mesa y velador', 'lamparas de mesa y velador', 'http://sodimac.scene7.com/is/image/sodimaccl/2879395?$lista175$', 'http://www.sodimac.cl/sodimac-cl/category/cat520046/lamparas-de-mesa-y-velador?no=128&nrpp=16', 'home collection', 'pack 2 l\xc3\xa1mpara de mesa metal niza e27', '12990', '2879395', 'pasillo 16 - rack 16'], ['muebles y decoraci\xc3\xb3n', 'muebles', 'iluminaci\xc3\xb3n', 'iluminaci\xc3\xb3n interior', 'lamparas de mesa y velador', 'lamparas de mesa y velador', 'lamparas de mesa y velador', 'http://sodimac.scene7.com/is/image/sodimaccl/2879387?$lista175$', 'http://www.sodimac.cl/sodimac-cl/category/cat520046/lamparas-de-mesa-y-velador?no=128&nrpp=16', 'home collection', 'pack 2 l\xc3\xa1mpara de mesa metal lyon e27', '12990', '2879387', 'pasillo 18 - rack 18'], ['muebles y decoraci\xc3\xb3n', 'muebles', 'iluminaci\xc3\xb3n', 'iluminaci\xc3\xb3n interior', 'lamparas de mesa y velador', 'lamparas de mesa y velador', 'lamparas de mesa y velador', 'http://sodimac.scene7.com/is/image/sodimaccl/1543237?$lista175$', 'http://www.sodimac.cl/sodimac-cl/category/cat520046/lamparas-de-mesa-y-velador?no=128&nrpp=16', 'casa bonita', 'pack 2 l\xc3\xa1mpara de mesa metal dijon e14', '11990', '1543237', 'pasillo 16 - rack 16'], ['muebles y decoraci\xc3\xb3n', 'muebles', 'iluminaci\xc3\xb3n', 'iluminaci\xc3\xb3n interior', 'l\xc3\xa1mparas colgantes y techo', 'l\xc3\xa1mparas colgantes y techo', 'l\xc3\xa1mparas colgantes y techo', 'http://sodimac.scene7.com/is/image/sodimaccl/2873397?$lista175$', 'http://www.sodimac.cl/sodimac-cl/category/scat303247/lamparas-colgantes-y-techo?no=128&nrpp=16', 'casa bonita', 'l\xc3\xa1mpara de techo metal vidrio 3 luces e27', '18990', '2873397', 'pasillo 18 - rack 18'], ['muebles y decoraci\xc3\xb3n', 'muebles', 'iluminaci\xc3\xb3n', 'iluminaci\xc3\xb3n interior', 'lamparas de mesa y velador', 'lamparas de mesa y velador', 'lamparas de mesa y velador', 'http://sodimac.scene7.com/is/image/sodimaccl/2715767?$lista175$', 'http://www.sodimac.cl/sodimac-cl/category/cat520046/lamparas-de-mesa-y-velador?no=160&nrpp=16', 'home collection', 'l\xc3\xa1mpara de mesa metal tel 1 luces beige', '9990', '2715767', 'pasillo 18 - rack 18'], ['muebles y decoraci\xc3\xb3n', 'muebles', 'iluminaci\xc3\xb3n', 'l\xc3\xa1mparas infantiles', 'l\xc3\xa1mparas infantiles', 'l\xc3\xa1mparas infantiles', 'l\xc3\xa1mparas infantiles', 'http://sodimac.scene7.com/is/image/sodimaccl/2698463?$lista175$', 'http://www.sodimac.cl/sodimac-cl/category/scat915264/lamparas-infantiles/n-1z141uw?no=48&nrpp=16', 'home collection', 'l\xc3\xa1mpara de escritorio metal cromada gris', '23990', '2698463', 'pasillo 16 - rack 16'], ['muebles y decoraci\xc3\xb3n', 'muebles', 'iluminaci\xc3\xb3n', 'iluminaci\xc3\xb3n interior', 'l\xc3\xa1mparas de pie', 'l\xc3\xa1mparas de pie', 'l\xc3\xa1mparas de pie', 'http://sodimac.scene7.com/is/image/sodimaccl/2715686?$lista175$', 'http://www.sodimac.cl/sodimac-cl/category/cat520042/lamparas-de-pie/n-1z141uw?no=16&nrpp=16', 'home collection', 'l\xc3\xa1mpara de pie foco metal 1 luz e27 negro', '31990', '2715686', 'pasillo 18 - rack 18'], ['muebles y decoraci\xc3\xb3n', 'muebles', 'iluminaci\xc3\xb3n', 'iluminaci\xc3\xb3n interior', 'plafones', 'plafones', 'plafones', 'http://sodimac.scene7.com/is/image/sodimaccl/2727129?$lista175$', 'http://www.sodimac.cl/sodimac-cl/category/scat304028/plafones?no=80&nrpp=16', 'homy', 'plafon vidrio - metal satinado', '10990', '2727129', 'pasillo 16 - rack 16'], ['muebles y decoraci\xc3\xb3n', 'muebles', 'iluminaci\xc3\xb3n', 'iluminaci\xc3\xb3n interior', 'l\xc3\xa1mparas colgantes y techo', 'l\xc3\xa1mparas colgantes y techo', 'l\xc3\xa1mparas colgantes y techo', 'http://sodimac.scene7.com/is/image/sodimaccl/2873400?$lista175$', 'http://www.sodimac.cl/sodimac-cl/category/scat303247/lamparas-colgantes-y-techo?no=368&nrpp=16', 'casa bonita', 'l\xc3\xa1mpara de techo metal cromo vidrio 5 luces', '31990', '2873400', 'pasillo 18 - rack 18'], ['muebles y decoraci\xc3\xb3n', 'muebles', 'muebles de bar', 'taburetes y sillas bar', 'taburetes y sillas bar', 'taburetes y sillas bar', 'taburetes y sillas bar', 'http://sodimac.scene7.com/is/image/sodimaccl/1711121?$lista175$', 'http://www.sodimac.cl/sodimac-cl/category/cat1930017/taburetes-y-sillas-bar?no=32&nrpp=16', 'homy', 'piso de bar metal-pvc alton caf\xc3\xa9', '34990', '1711121', 'pasillo 11 - rack 11'], ['decohogar', 'accesorios y textil de ba\xc3\xb1o', 'cortinas y barras de ba\xc3\xb1o', 'ganchos para cortinas de ba\xc3\xb1o', 'ganchos para cortinas de ba\xc3\xb1o', 'ganchos para cortinas de ba\xc3\xb1o', 'ganchos para cortinas de ba\xc3\xb1o', 'http://sodimac.scene7.com/is/image/sodimaccl/2972468?$lista175$', 'http://www.sodimac.cl/sodimac-cl/category/scat102387/ganchos-para-cortinas-de-bano', 'home collection', 'set 12 ganchos metal doble', '5390', '2972468', 'pasillo 31 - rack 31'], ['decohogar', 'accesorios y textil de ba\xc3\xb1o', 'cortinas y barras de ba\xc3\xb1o', 'ganchos para cortinas de ba\xc3\xb1o', 'ganchos para cortinas de ba\xc3\xb1o', 'ganchos para cortinas de ba\xc3\xb1o', 'ganchos para cortinas de ba\xc3\xb1o', 'http://sodimac.scene7.com/is/image/sodimaccl/2972441?$lista175$', 'http://www.sodimac.cl/sodimac-cl/category/scat102387/ganchos-para-cortinas-de-bano', 'home collection', 'set 12 ganchos cuadrados metal', '5190', '2972441', 'pasillo 31 - rack 31'], ['muebles y decoraci\xc3\xb3n', 'muebles', 'muebles de dormitorio', 'organizaci\xc3\xb3n de closet', 'portazapatos', 'portazapatos', 'portazapatos', 'http://sodimac.scene7.com/is/image/sodimaccl/1074059?$lista175$', 'http://www.sodimac.cl/sodimac-cl/category/cat4850453/portazapatos', 'ordenna', 'zapatera extensible metal madera', '14990', '1074059', 'pasillo 15 - rack 15'], ['muebles y decoraci\xc3\xb3n', 'muebles', 'muebles de dormitorio', 'organizaci\xc3\xb3n de closet', 'colgadores', 'colgadores', 'colgadores', 'http://sodimac.scene7.com/is/image/sodimaccl/1666207?$lista175$', 'http://www.sodimac.cl/sodimac-cl/category/cat1420091/colgadores', 'ordenna', 'colgador metal con antideslizante negro', '1590', '1666207', 'pasillo 15 - rack 15'], ['muebles y decoraci\xc3\xb3n', 'muebles', 'muebles de dormitorio', 'organizaci\xc3\xb3n de closet', 'colgadores', 'colgadores', 'colgadores', 'http://sodimac.scene7.com/is/image/sodimaccl/2346176?$lista175$', 'http://www.sodimac.cl/sodimac-cl/category/cat1420091/colgadores?no=16&nrpp=16', 'gen\xc3\xa9rico', 'colgador con clip metal beige', '2690', '2346176', 'pasillo 15 - rack 15'], ['muebles y decoraci\xc3\xb3n', 'muebles', 'muebles de dormitorio', 'organizaci\xc3\xb3n de closet', 'colgadores', 'colgadores', 'colgadores', 'http://sodimac.scene7.com/is/image/sodimaccl/2346168?$lista175$', 'http://www.sodimac.cl/sodimac-cl/category/cat1420091/colgadores?no=16&nrpp=16', 'gen\xc3\xa9rico', 'colgador 4 barras metal beige', '3990', '2346168', 'pasillo 15 - rack 15']], 'categoria_actual': 1},
        "eleccion": 9
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
if eleccion == len(categorias_a_usuario):
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
    mensaje_final = mensaje_final_parcial.encode('utf-8') +"{}. Encontrarás {}, junto a otras cosas relacionadas".format('; '.join(pasillos).encode('utf-8'), ', '.join([row[header.index('Nombre')] for row in data[:3]]).encode('utf-8'))
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