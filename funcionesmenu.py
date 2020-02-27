
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

#####Buscar o filtrar Informacion: Pide una fecha y muestra la informacion completa del tiempo.

def info_prediccion_completa(fecha,doc):

    ## Lista donde guardaremos toda la información de la programacion
    prediccion=[]
    prediccion.append("\t\tPREDICCIÓN DEL TIEMPO:")
    prediccion.append("\t\t----------------------")
    prediccion.append("")

    ############################################################################
    ## Probabilidad de precipitacion
    ############################################################################

    #ipp1 // ipp2 -> indicador Probabilidad Precipitacion
    porcentaje="%"
    ipp1=False
    ipp2=False

    prediccion.append("\t\t -> Precipitaciones registradas:")
    prediccion.append("")
    for prob_prep in doc.xpath('//dia[@fecha="%s"]/prob_precipitacion'%(fecha)):
        try:
            if prob_prep.xpath('./text()'):
                ## PP -> Probabilidad de Precipitacion
                for pp in prob_prep.xpath('./text()'):
                    if pp != "0":
                        ipp1=True
                        prediccion.append("\t\t\tProbabilidad de precipitacion del %s%s entre las %s h."%(pp,porcentaje,prob_prep.xpath('./@periodo')[0]))

        except IndexError:
            if prob_prep.xpath('./text()'):
                ## PP -> Probabilidad de Precipitacion
                for pp in prob_prep.xpath('./text()'):
                    if pp != "0":
                        ipp2=True
                        prediccion.append("\t\t\tProbabilidad de precipitacion del %s%s."%(pp,porcentaje))

    if not ipp1 and not ipp2:
        prediccion.append("\t\t\tNo hay precipitaciones registradas.")

    ############################################################################
    ############################################################################

    ############################################################################
    ## Estado Cielo
    ############################################################################

    prediccion.append("")
    prediccion.append("\t\t -> Estados de cielo registrados:")
    prediccion.append("")
    # lista_et -> Lista estado cielo // est_cielo -> estado cielo
    # iec -> Indicador estado cielo
    lista_et=[]

    for est_cielo in doc.xpath('//dia[@fecha="%s"]/estado_cielo'%(fecha)):
        try:
            if est_cielo.xpath('./@descripcion')[0] != "":
                if est_cielo.xpath('./@descripcion')[0] not in lista_et:
                    lista_et.append(est_cielo.xpath('./@descripcion')[0])
                    try:
                        prediccion.append("\t\t\t%s entre las %sh. "%(est_cielo.xpath('./@descripcion')[0],est_cielo.xpath('./@periodo')[0]))
                    except IndexError:
                        prediccion.append("\t\t\t%s sin hora registrada."%(est_cielo.xpath('./@descripcion')[0]))
        except IndexError:
            pass

    if not doc.xpath('//dia[@fecha="%s"]/estado_cielo/@descripcion'%(fecha)):
        prediccion.append("\t\t\tNo hay estado de cielo registrado.")

    ############################################################################
    ############################################################################

    ############################################################################
    ## Probabilidad cota nieve
    ############################################################################

    #ict -> indicador probabilidad cota de nieve
    ipcn=False
    prediccion.append("")
    prediccion.append("\t\t -> Cota de nieve registradas:")
    prediccion.append("")

    ## r_viento -> Rachas de viento.
    for cota_nieve in doc.xpath('//dia[@fecha="%s"]/cota_nieve_prov'%(fecha)):
        try:
            if cota_nieve.xpath('./text()')[0] != "0":
                ipcn=True
                prediccion.append("\t\t\tCota de nieve a los %s m. entre las %s h."%(cota_nieve.xpath('./text()')[0],cota_nieve.xpath('./@periodo')[0]))
        except IndexError:
            try:
                prediccion.append("\t\t\tCota de nieve a los %s m. sin horas registradas."%(cota_nieve.xpath('./text()')[0]))
            except IndexError:
                pass

    if not ipcn:
        prediccion.append("\t\t\tSin cotas de nieve registradas.")

    ############################################################################
    ############################################################################

    ############################################################################
    ## Rachas de viento
    ############################################################################

    #irv -> indicador rachas de viento
    irv=False

    prediccion.append("")
    prediccion.append("\t\t -> Rachas de viento registradas:")
    prediccion.append("")

    ## r_viento -> Rachas de viento.
    for r_viento in doc.xpath('//dia[@fecha="%s"]/viento'%(fecha)):
        try:
            if r_viento.xpath('./velocidad/text()')[0] != "0":
                irv=True
                try:
                    prediccion.append("\t\t\tRacha de viento de %s km/h dirección \"%s\" entre las %s h."%(r_viento.xpath('./velocidad/text()')[0],r_viento.xpath('./direccion/text()')[0],r_viento.xpath('./@periodo')[0]))
                except IndexError:
                    try:
                        prediccion.append("\t\t\tRacha de viento de %s km/h sin dirección registrada entre las %s h."%(r_viento.xpath('./velocidad/text()')[0],r_viento.xpath('./@periodo')[0]))
                    except IndexError:
                        prediccion.append("\t\t\tRacha de viento de %s km/h dirección \"%s\" sin hora registrada."%(r_viento.xpath('./velocidad/text()')[0],r_viento.xpath('./direccion/text()')[0],))
        except IndexError:
            pass
    if not irv:
        prediccion.append("\t\t\tNo hay rachas de viento registradas.")

    ############################################################################
    ############################################################################

    ############################################################################
    ## Temperatura
    ############################################################################

    prediccion.append("")
    prediccion.append("\t\t -> Temperaturas registradas:")
    prediccion.append("")

    try:
        if doc.xpath('//dia[@fecha="%s"]/temperatura/maxima/text()'%(fecha)) != "":
            prediccion.append("\t\t\tTemperatura máxima %sºC."%(doc.xpath('//dia[@fecha="%s"]/temperatura/maxima/text()'%(fecha))[0]))
        try:
            if doc.xpath('//dia[@fecha="%s"]/temperatura/minima/text()'%(fecha)) != "":
                prediccion.append("\t\t\tTemperatura mínima %sºC."%(doc.xpath('//dia[@fecha="%s"]/temperatura/minima/text()'%(fecha))[0]))
        except IndexError:
            pass
    except IndexError:
        try:
            if doc.xpath('//dia[@fecha="%s"]/temperatura/minima/text()'%(fecha)) != "":
                prediccion.append("\t\t\tTemperatura mínima %sºC."%(doc.xpath('//dia[@fecha="%s"]/temperatura/minima/text()'%(fecha))[0]))
        except IndexError:
            pass

    ## Comprueba si hay o no temperatura tanto maxima como minima.

    if not doc.xpath('//dia[@fecha="%s"]/temperatura/maxima/text()'%(fecha)) and not doc.xpath('//dia[@fecha="%s"]/temperatura/minima/text()'%(fecha)):
        prediccion.append("\t\t\tNo hay temperaturas registradas.")
    elif not doc.xpath('//dia[@fecha="%s"]/temperatura/maxima/text()'%(fecha)):
        prediccion.append("\t\t\tNo hay temperatura máxima registrada.")
    elif not doc.xpath('//dia[@fecha="%s"]/temperatura/minima/text()'%(fecha)):
        prediccion.append("\t\t\tNo hay temperatura mínima registrada.")


    ############################################################################
    ############################################################################

    ############################################################################
    ## Sensacion termica
    ############################################################################

    prediccion.append("")
    prediccion.append("\t\t -> Sensaciones térmicas registradas:")
    prediccion.append("")

    try:
        if doc.xpath('//dia[@fecha="%s"]/sens_termica/maxima/text()'%(fecha)) != "":
            prediccion.append("\t\t\tSensasión térmica máxima %sºC."%(doc.xpath('//dia[@fecha="%s"]/sens_termica/maxima/text()'%(fecha))[0]))
        try:
            if doc.xpath('//dia[@fecha="%s"]/sens_termica/minima/text()'%(fecha)) != "":
                prediccion.append("\t\t\tSensasión térmica mínima %sºC."%(doc.xpath('//dia[@fecha="%s"]/sens_termica/minima/text()'%(fecha))[0]))
        except IndexError:
            pass
    except IndexError:
        try:
            if doc.xpath('//dia[@fecha="%s"]/sens_termica/minima/text()'%(fecha)) != "":
                prediccion.append("\t\t\tSensasión térmica mínima %sºC."%(doc.xpath('//dia[@fecha="%s"]/sens_termica/minima/text()'%(fecha))[0]))
        except IndexError:
            pass

    ## Comprueba si hay o no Sensasión térmica tanto maxima como minima.

    if not doc.xpath('//dia[@fecha="%s"]/sens_termica/maxima/text()'%(fecha)) and not doc.xpath('//dia[@fecha="%s"]/sens_termica/minima/text()'%(fecha)):
        prediccion.append("\t\t\tNo hay sensaciones térmicas registradas.")
    elif not doc.xpath('//dia[@fecha="%s"]/sens_termica/maxima/text()'%(fecha)):
        prediccion.append("\t\t\tNo hay sensación térmica máxima registrada.")
    elif not doc.xpath('//dia[@fecha="%s"]/sens_termica/minima/text()'%(fecha)):
        prediccion.append("\t\t\tNo hay sensación térmica registrada.")


    ############################################################################
    ############################################################################

    ############################################################################
    ## Humedad Relativa
    ############################################################################

    prediccion.append("")
    prediccion.append("\t\t -> Humedad relativa registrada:")
    prediccion.append("")

    try:
        if doc.xpath('//dia[@fecha="%s"]/humedad_relativa/maxima/text()'%(fecha)) != "":
            prediccion.append("\t\t\tHumedad relativa máxima %s%s."%(doc.xpath('//dia[@fecha="%s"]/humedad_relativa/maxima/text()'%(fecha))[0],porcentaje))
        try:
            if doc.xpath('//dia[@fecha="%s"]/humedad_relativa/minima/text()'%(fecha)) != "":
                prediccion.append("\t\t\tHumedad relativa mínima %s%s."%(doc.xpath('//dia[@fecha="%s"]/humedad_relativa/minima/text()'%(fecha))[0],porcentaje))
        except IndexError:
            pass
    except IndexError:
        try:
            if doc.xpath('//dia[@fecha="%s"]/humedad_relativa/minima/text()'%(fecha)) != "":
                prediccion.append("\t\t\tHumedad relativa mínima %s%s."%(doc.xpath('//dia[@fecha="%s"]/humedad_relativa/minima/text()'%(fecha))[0],porcentaje))
        except IndexError:
            pass

    ## Comprueba si hay o no Sensasión térmica tanto maxima como minima.

    if not doc.xpath('//dia[@fecha="%s"]/humedad_relativa/maxima/text()'%(fecha)) and not doc.xpath('//dia[@fecha="%s"]/humedad_relativa/minima/text()'%(fecha)):
        prediccion.append("\t\t\tNo hay humedad relativa registrada.")
    elif not doc.xpath('//dia[@fecha="%s"]/humedad_relativa/maxima/text()'%(fecha)):
        prediccion.append("\t\t\tNo hay Humedad relativa máxima registrada.")
    elif not doc.xpath('//dia[@fecha="%s"]/humedad_relativa/minima/text()'%(fecha)):
        prediccion.append("\t\t\tNo hay Humedad relativa mínima registrada.")


    ############################################################################
    ############################################################################

    return prediccion







#####Buscar informacion relacionada: Mostrar la fecha cuya temperatura max y min sean igual a la introducida por teclado.



#####Ejercicio Libre: Pide el una temperatura max y min y muestra por teclado aquella fecha cual estado_cielo sea igual al introducido por teclado teniendo en cuenta la temperatura max y min.
