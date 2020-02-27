
#####Listar Informacion: Listar los dias para los cuales hay prediccion del tiempo.

def lista_fechas(doc):
    return doc.xpath("//@fecha")

#####Contar Informacion: ¿De que quieres contar informacion? (Dentro del programa habra un submenu en el que podras elegir que informacion quieres contar.)

## Contar el numero de dias de los cuales tenemos información del tiempo.
def contar_num_dias(doc):
    return doc.xpath("count(//@fecha)")

## Contar el numero de dias cuya temperatura max es la introducida por teclado.
def contar_num_dias_con_max(tmax,doc):
    return int(doc.xpath('count(//temperatura[maxima="%i"])'%(tmax)))

## Contar el numero de dias cuya temperatura min es la introducida por teclado.
def contar_num_dias_con_min(tmin,doc):
    return int(doc.xpath('count(//temperatura[minima="%i"])'%(tmin)))
