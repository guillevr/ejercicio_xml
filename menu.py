from lxml import etree
from funcionesmenu import *
doc = etree.parse('eltiempoendh.xml')

while True:
    print()
    print()
    print("\t------ MENU DE OPCIONES ------")
    print()
    print("\t1. Listar informacion.")
    print("\t2. Contar informacion.")
    print("\t3. Buscar o filtrar informacion.")
    print("\t4. Buscar informacion relacionada.")
    print("\t5. Ejercicio libre.")
    print("\t0. Salir del programa.")
    print()
    print("\t------------------------------")
    print()
    opcion=int(input("\tOpcion: "))

    if opcion ==0:
        break;

    elif opcion ==1:
        print()
        print("\t--- Dias de los cuales tenemos información del tiempo ---")
        print()
        for fecha in lista_fechas(doc):
            print("\t",fecha)
        print()

    elif opcion == 2:
        print()
        print("\t--- Contador de informacion ---")
        print()
        while True:
            print("\t--- MENU DE CONTAR ---")
            print()
            print("\t1. Contar el número de dias de los cuales tenemos información del tiempo.")
            print("\t2. Contar los dias cuyo temperatura max es la introducida por teclado.")
            print("\t3. Contar los dias cuyo temperatura min es la introducida por teclado.")
            print("\t0. Salir del programa contador.")
            print()
            print("\t------------------------")
            opcion=int(input("\tOpcion: "))

            if opcion==0:
                break
            elif opcion==1:
                print()
                print("\tTenemos informacion del tiempo de %i dias."%(contar_num_dias(doc)))
                print()
            elif opcion==2:
                print()
                tmaxima=int(input("\tTemperatura Maxima: "))
                print()
                print("\tTendremos %s dias con una máxima de %iºC"%(contar_num_dias_con_max(tmaxima,doc),tmaxima))
                print()
            elif opcion==3:
                print()
                tminima=int(input("\tTemperatura Minima: "))
                print()
                print("\tTendremos %i dias con una mínima de %iºC"%(contar_num_dias_con_min(tminima,doc),tminima))
                print()
            else:
                print("\tError, opción incorrecta.")
        print()

    elif opcion == 3:
        print()
        dias="| "
        print("\t--- Predicción del tiempo ---")
        for f in lista_fechas(doc):
            dias=dias+f+" | "
        print("\tFechas disponibles: ",dias)
        print()
        fecha=input("\tIntroduzca una fecha: ")
        print()

        for elem in info_prediccion_completa(fecha,doc):
            print(elem)


    elif opcion == 4:
        print()

        print()

    elif opcion == 5:
        print()

        print()
    else:
        print()
        print("\tError. opcion incorrecta")
        print()
