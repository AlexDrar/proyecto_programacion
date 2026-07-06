import modos_de_juegos
from herramientas import menu_principal, submenu_personas, limpiar
 
while True:
    opcion = menu_principal()
 
    if opcion == 1:
        substate = submenu_personas()
        if substate == 1:
            modos_de_juegos.automatico()
        elif substate == 2:
            modos_de_juegos.manual()
        else:
            continue 
    elif opcion == 2:
        modos_de_juegos.computadora()
    elif opcion == 3:
        modos_de_juegos.historial()
    elif opcion == 4:
        modos_de_juegos.estadisticas()
    else:
        limpiar()
        print("Gracias por jugar!")
        break
 