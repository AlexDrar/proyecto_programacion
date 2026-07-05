from herramientas import generacion, fin_de_partida,  interfaz, limpiar, nombres, verificar, ganaroperder, reducir_lista, crear_lista
from random import randint
def automatico():  # Modo automatico entre 2 jugadores
    secreto1 = generacion()
    secreto2 = generacion()
    intentosjugador1 = []
    aciertosjugador1 = []
    intentosjugador2 = []
    aciertosjugador2 = []
    isplayer1 = True
    limpiar()
    print(secreto1, secreto2)
    jugador1, jugador2 = nombres(True)
    interfaz(jugador1, jugador2, intentosjugador1, aciertosjugador1, intentosjugador2, aciertosjugador2, jugador1)

    while True:
        #########################################################################################3
        while True:
            intentopl1 = input("Ingrese una consulta: ")
            if len(intentopl1) != 3:
                print("error")
            elif (
                intentopl1[0] == intentopl1[1]
                or intentopl1[0] == intentopl1[2]
                or intentopl1[1] == intentopl1[2]
            ):
                print("error")
            else:
                intentosjugador1.append(intentopl1)
                break
        ######################################################################################
        aciertos1 = verificar(secreto2, intentopl1)
        aciertosjugador1.append(aciertos1)
        if aciertos1 == 3:
            if ganaroperder(secreto2, intentopl1):
                break
        interfaz(jugador1, jugador2, intentosjugador1, aciertosjugador1, intentosjugador2, aciertosjugador2, jugador2)
       

        while True:
            intentopl2 = input("Ingrese una consulta: ")
            if len(intentopl2) != 3:
                print("error")
            elif (
                intentopl2[0] == intentopl2[1]
                or intentopl2[0] == intentopl2[2]
                or intentopl2[1] == intentopl2[2]
            ):
                print("error")
            else:
                intentosjugador2.append(intentopl2)
                break
        ##################################################################################
        aciertos2 = verificar(secreto1, intentopl2)
        aciertosjugador2.append(aciertos2)
        if aciertos2 == 3:
            if ganaroperder(secreto1, intentopl2):
                isplayer1 = False
                break
        interfaz(jugador1, jugador2, intentosjugador1, aciertosjugador1, intentosjugador2, aciertosjugador2, jugador1)
    if isplayer1:
        fin_de_partida(jugador1, intentosjugador1)
    else:
        fin_de_partida(jugador2, intentosjugador2)
def manual():  # modo manual entre 2 jugadores
    candidatos1 = crear_lista()  # posibles codigos del jugador 1, vistos desde afuera
    candidatos2 = crear_lista()  # posibles codigos del jugador 2, vistos desde afuera
    intentosjugador1 = []
    aciertosjugador1 = []
    intentosjugador2 = []
    aciertosjugador2 = []
    isplayer1 = True
    inconsistente = False
    limpiar()
    jugador1, jugador2 = nombres(True)

    interfaz(jugador1, jugador2, intentosjugador1, aciertosjugador1, intentosjugador2, aciertosjugador2, jugador1)
    ##################################################################################
    while True:
        while True:
            intentopl1 = input("Consulta jugador 1: ")

            if len(intentopl1) != 3:
                print("error")
            elif (
                intentopl1[0] == intentopl1[1]
                or intentopl1[0] == intentopl1[2]
                or intentopl1[1] == intentopl1[2]
            ):
                print("error")
            else:
                intentosjugador1.append(intentopl1)
                break
        while True:
            aciertos1 = input("Aciertos jugador 1: ")

            if not aciertos1.isdigit() or int(aciertos1) < 0 or int(aciertos1) > 3:
                print("error")
            else:
                aciertos1 = int(aciertos1)
                break
        aciertosjugador1.append(aciertos1)

        candidatos2 = reducir_lista(candidatos2, intentopl1, aciertos1)
        interfaz(jugador1, jugador2, intentosjugador1, aciertosjugador1, intentosjugador2, aciertosjugador2, jugador2)

        if len(candidatos2) == 0:
            inconsistente = True
            break

        if aciertos1 == 3:
            exacto1 = input("Aciertos 3! El codigo fue adivinado ? (y/n): ")
            if exacto1 == "Y" or exacto1 == "y":
                break
            else:
                interfaz(jugador1, jugador2, intentosjugador1, aciertosjugador1, intentosjugador2, aciertosjugador2, jugador2)
        ##################################################################################
        while True:
            intentopl2 = input("Consulta jugador 2: ")
            if len(intentopl2) != 3:
                print("error")
            elif (
                intentopl2[0] == intentopl2[1]
                or intentopl2[0] == intentopl2[2]
                or intentopl2[1] == intentopl2[2]
            ):
                print("error")
            else:
                intentosjugador2.append(intentopl2)
                break

        while True:
            aciertos2 = input("Acierto jugador 2: ")

            if not aciertos2.isdigit() or  int(aciertos2) < 0 or int(aciertos2) > 3:
                print("error")
            else:
                aciertos2 = int(aciertos2)
                break
        aciertosjugador2.append(aciertos2)

        candidatos1 = reducir_lista(candidatos1, intentopl2, aciertos2)
        interfaz(jugador1, jugador2, intentosjugador1, aciertosjugador1, intentosjugador2, aciertosjugador2, jugador1)

        if len(candidatos1) == 0:
            inconsistente = True
            break

        if aciertos2 == 3:
            exacto2 = input("Aciertos 3! El codigo fue adivinado ? (y/n): ")
            if exacto2 == "Y" or exacto2 == "y":
                isplayer1 = False
                break
            else:
                interfaz(jugador1, jugador2, intentosjugador1, aciertosjugador1, intentosjugador2, aciertosjugador2, jugador1)
    ##################################################################################
    if inconsistente:
        fin_de_partida(jugador1, intentosjugador1, True)
    elif isplayer1:
        fin_de_partida(jugador1, intentosjugador1)
    else:
        fin_de_partida(jugador2, intentosjugador2)
def computadora():
    listaorigen = crear_lista()
    numerocpu = generacion()
    #print(numerocpu)
    cpuintento = []
    listacpu = []
    isfirstround = True
    isplayer1 = True
    inconsistente = False
    limpiar()
    jugador1 = nombres()
    limpiar()
    intentosjugador1 = []
    aciertosjugador1 = []
    modo = int(input("Seleccione el modo de dificultad:\n(1) Modo Dificil\n(2) Modo Normal\n(3) Modo Facil\nIngrese el numero correspondiente al modo: "))
    interfaz(jugador1, "", intentosjugador1, aciertosjugador1, "", "", jugador1, True)
    ##################################################################################
    while True:
        if isfirstround:
            guess = generacion()
            cpuintento.append(guess)
        while True:
            intentopl1 = input("Consulta jugador: ")

            if len(intentopl1) != 3:
                print("error")
            elif (
                intentopl1[0] == intentopl1[1]
                or intentopl1[0] == intentopl1[2]
                or intentopl1[1] == intentopl1[2]
            ):
                print("error")
            else:
                intentosjugador1.append(intentopl1)
                break
        aciertos1 = verificar(numerocpu, intentopl1)
        aciertosjugador1.append(aciertos1)
        if aciertos1 == 3:
            if ganaroperder(numerocpu, intentopl1):
                break
        interfaz(jugador1, "", intentosjugador1, aciertosjugador1, "", "", jugador1, True)

        ##################################################################################

        if not isfirstround:
            if modo == 1:
                pool = listacpu  # dificil: elige de la lista ya reducida por TODO el historial
            elif modo == 2:
                pool = reducir_lista(listaorigen, guess, aciertoscpu)  # normal: filtra la lista completa solo con la ultima respuesta
            else:
                pool = listaorigen  # facil: elige de la lista completa, sin usar los aciertos

            while True:
                i = randint(0, len(pool)-1)
                guess = pool[i]
                if guess not in cpuintento:
                    cpuintento.append(guess)
                    break

        print("Consulta Computadora: ", end="")
        print(guess)

        while True:
            aciertoscpu = input("Aciertos Computadora: ")

            if not aciertoscpu.isdigit() or int(aciertoscpu) < 0 or int(aciertoscpu) > 3:
                print("error")
            else:
                aciertoscpu = int(aciertoscpu)
                interfaz(jugador1, "", intentosjugador1, aciertosjugador1, "", "", jugador1, True)
                break
        if isfirstround:
            listacpu = reducir_lista(listaorigen, guess, aciertoscpu)
        else:
            listacpu = reducir_lista(listacpu, guess, aciertoscpu)
        if len(listacpu) == 0:
            inconsistente = True
            break
        isfirstround = False
        if aciertoscpu == 3:
            exacto2 = input("Aciertos 3! El codigo fue adivinado ? (y/n): ")
            if exacto2 == "Y" or exacto2 == "y":
                isplayer1 = False
                break
            else:
                interfaz(jugador1, "", intentosjugador1, aciertosjugador1, "", "", jugador1, True)
    ##################################################################################
    if inconsistente:
        fin_de_partida(jugador1, aciertos1, True)
    elif isplayer1:
        fin_de_partida(jugador1, intentosjugador1)
    else:
        fin_de_partida("Computadora", cpuintento)