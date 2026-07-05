import random

def verificar(secreto, intento):  # devuelva cantidad de aciertos
    secreto = str(secreto)
    intento = str(intento)

    aciertos = 0

    for i in range(3):
        if intento[i] in secreto:
            aciertos += 1

    return aciertos


def generacion():  # genera un numero al azar de 3 digitos diferentes (0-9)

    cifra1 = random.randint(0, 9)

    cifra2 = random.randint(0, 9)

    while cifra1 == cifra2:
        cifra2 = random.randint(0, 9)

    cifra3 = random.randint(0, 9)

    while cifra3 == cifra1 or cifra3 == cifra2:
        cifra3 = random.randint(0, 9)

    return str(cifra1) + str(cifra2) + str(cifra3)

def nombres(is2player = False):
    if not is2player:
        return input("Ingrese el nombre del jugador 1: ")
    else:
        jugador1 = input("Ingrese el nombre del jugador 1: ")
        jugador2 = input("Ingrese el nombre del jugador 2: ")
        return jugador1, jugador2
def ganaroperder(x, y):  # retorna True si 2 numeros coinciden, si no False

    str(x)
    str(y)
    if x == y:
        return True
    else:
        return False


def automatico():  # Modo automatico entre 2 jugadores
    secreto1 = generacion()
    secreto2 = generacion()
    isplayer1 = True
    print("PARTIDA:")
    print("TURNO JUGADOR JUGADOR 1")

    print(secreto1, secreto2)

    while True:
        #########################################################################################3
        while True:
            intentopl1 = input("Acierto jugador 1: ")

            if len(intentopl1) != 3:
                print("error")
            elif (
                intentopl1[0] == intentopl1[1]
                or intentopl1[0] == intentopl1[2]
                or intentopl1[1] == intentopl1[2]
            ):
                print("error")
            else:
                break
        ######################################################################################
        aciertos1 = verificar(secreto2, intentopl1)

        print("Aciertos:", aciertos1)
        if aciertos1 == 3:
            if ganaroperder(secreto2, intentopl1):
                break

        while True:
            intentopl2 = input("Acierto jugador 2: ")
            ##############################################################################################33
            if len(intentopl2) != 3:
                print("error")
            elif (
                intentopl2[0] == intentopl2[1]
                or intentopl2[0] == intentopl2[2]
                or intentopl2[1] == intentopl2[2]
            ):
                print("error")
            else:
                break
        ##################################################################################
        aciertos2 = verificar(secreto1, intentopl2)
        print("Aciertos:", aciertos2)
        if aciertos2 == 3:
            if ganaroperder(secreto1, intentopl2):
                isplayer1 = False
                break
    if isplayer1:
        print(
            f"El jugador 1 ha ganado la partida! \nEl codigo a adivinar era {secreto2}"
        )
    else:
        print(
            f"El jugador 2 ha ganado la partida! \nEl codigo a adivinar era {secreto1}"
        )


def crear_lista():  # Crea una lista con todos los 720 numero posibles
    lista = []

    for i in range(1000):
        numero = f"{i:03}"

        if len(set(numero)) == 3:
            lista.append(numero)

    return lista


def reducir_lista(lista_actual, numero, aciertos):  # Reduce una lista con criterio de aciertos
    nueva_lista = []

    for i in lista_actual:
        if verificar(i, numero) == aciertos:
            nueva_lista.append(i)

    return nueva_lista


def manual():  # modo manual entre 2 jugadores
    candidatos1 = crear_lista()  # posibles codigos del jugador 1, vistos desde afuera
    candidatos2 = crear_lista()  # posibles codigos del jugador 2, vistos desde afuera
    isplayer1 = True
    inconsistente = False
    print("PARTIDA:")
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
                break
        while True:
            aciertos1 = input("Aciertos jugador 1: ")

            if not aciertos1.isdigit() or int(aciertos1) < 0 or int(aciertos1) > 3:
                print("error")
            else:
                aciertos1 = int(aciertos1)
                break

        candidatos2 = reducir_lista(candidatos2, intentopl1, aciertos1)
        if len(candidatos2) == 0:
            inconsistente = True
            break

        if aciertos1 == 3:
            exacto1 = input("Aciertos 3! El codigo fue adivinado ? (y/n): ")
            if exacto1 == "Y" or exacto1 == "y":
                break
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
                break

        while True:
            aciertos2 = input("Acierto jugador 2: ")

            if not aciertos2.isdigit() or  int(aciertos2) < 0 or int(aciertos2) > 3:
                print("error")
            else:
                aciertos2 = int(aciertos2)
                break

        candidatos1 = reducir_lista(candidatos1, intentopl2, aciertos2)

        if len(candidatos1) == 0:
            inconsistente = True
            break

        if aciertos2 == 3:
            exacto2 = input("Aciertos 3! El codigo fue adivinado ? (y/n): ")
            if exacto2 == "Y" or exacto2 == "y":
                isplayer1 = False
                break
    ##################################################################################
    if inconsistente:
        print("Partida inconsistente! Se detecto una contradiccion")
    elif isplayer1:
        print("El jugador 1 ha ganado la partida!")
    else:
        print("El jugador 2 ha ganado la partida!")


def computadora():
    listaorigen = crear_lista()
    numerocpu = generacion()
    print(numerocpu)
    cpuintento = []
    listacpu = []
    isfirstround = True
    isplayer1 = True
    inconsistente = False
    print("PARTIDA:")
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
                break
        aciertos1 = verificar(numerocpu, intentopl1)

        print("Aciertos Jugador:", aciertos1)
        if aciertos1 == 3:
            if ganaroperder(numerocpu, intentopl1):
                break

        # candidatos2 = reducir_lista(candidatos2, intentopl1, aciertos1)
        # if len(candidatos2) == 0:
        #   inconsistente  = True
        #  break

        ##################################################################################

        if not isfirstround:
            while True:
                i = random.randint(0, len(listacpu)-1)
                guess = listacpu[i]
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
    ##################################################################################
    if inconsistente:
        print("Partida inconsistente! Se detecto una contradiccion")
    elif isplayer1:
        print("El jugador 1 ha ganado la partida!")
    else:
        print("La Computadora ha ganado la partida!")

manual()