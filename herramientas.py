import random
import os
import json
from datetime import datetime

def limpiar(): #limpia la terminal
    os.system("cls")
def fin_de_partida(ganador, consultasganador, incosistente=False):#Arma la Interfaz del fin de partida
    limpiar()
    print("="*50)
    titulo = "FIN DE LA PARTIDA"
    print(titulo.center(50))
    print("="*50)
    print()
    if not incosistente:
        print(f"Ganador: {ganador}")
        print(f"Turnos utilizados: {len(consultasganador)}")
        print()
        input("Presione ENTER para continuar...")
    else:
        print("Partida Finalizada! Se ha detectado una inconsistencia")
        print()
        input("Presione ENTER para continuar...")
def interfaz(nombre1, nombre2, consultas1, aciertos1, consultas2, aciertos2, turnoactual, iscomputer=False): #Arma la Interfaz de la partida
    limpiar()
    print("="*50)
    titulo = "CODIGO SECRETO"
    print(titulo.center(50))
    print("="*50)
    print()
    if not iscomputer:
        print(f"Jugador 1 ({nombre1})".ljust(30) + f"Jugador 2 ({nombre2})")
    else:
        print(f"Jugador 1 ({nombre1})".ljust(30))

    totalturnos = max(len(consultas1), len(consultas2))
    for i in range(totalturnos):
        if i < len(consultas1):
            columna_izq = f"{consultas1[i]} -> {aciertos1[i]}"
        else:
            columna_izq = ""

        if i < len(consultas2):
            columna_der = f"{consultas2[i]} -> {aciertos2[i]}"
        else:
            columna_der = ""
        if not iscomputer:
            print(columna_izq.ljust(30) + columna_der)
        else:
            print(columna_izq)
    print("-" * 50)
    print(f"Turno actual: {turnoactual}")
def menu_principal(): #Muestra el menu principal y devuelve la opcion elegida
    while True:
        limpiar()
        print("="*50)
        titulo = "MENU"
        print(titulo.center(50))
        print("="*50)
        print()
        print("1. Jugar entre personas")
        print("2. Jugar contra la computadora")
        print("3. Ver historial de partidas")
        print("4. Ver estadisticas")
        print("5. Salir")
        print()
        opcion = input("Ingrese el numero de la opcion: ")

        if opcion not in ("1", "2", "3", "4", "5"):
            print("error")
            input("Presione ENTER para continuar...")
        else:
            return int(opcion)
def submenu_personas(): #Muestra el submenu de "Jugar entre personas" y devuelve la opcion elegida
    while True:
        limpiar()
        print("="*50)
        titulo = "CODIGO SECRETO"
        print(titulo.center(50))
        print("="*50)
        print()
        print("1. Modo Automatico")
        print("2. Modo Manual")
        print("3. Volver al menu principal")
        print()
        opcion = input("Ingrese el numero de la opcion: ")

        if opcion not in ("1", "2", "3"):
            print("error")
            input("Presione ENTER para continuar...")
        else:
            return int(opcion)
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
def nombres(is2player = False): #Guarda los nombres de los jugadores
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
def generar_archivo(jugador1, jugador2, modo, turnos, ganador, dificultad=None):
    fecha = datetime.now()

    partida = {
        "jugador1": jugador1,
        "jugador2": jugador2,
        "fecha": str(fecha),
        "ganador": ganador,
        "turnos": turnos,
        "modo": modo
    }

    if dificultad is not None:
        partida["dificultad"] = dificultad

    if os.path.exists("partida.json"):
        archivo = open("partida.json", "r")
        historial = json.load(archivo)
        archivo.close()
    else:
        historial = []

    historial.append(partida)

    archivo = open("partida.json", "w")
    json.dump(historial, archivo)
    archivo.close()