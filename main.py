import modos_de_juegos
from herramientas import menu_principal, submenu_personas, limpiar
 
while True:
    opcion = menu_principal()
 
    if opcion == 1:
        suboption = submenu_personas()
        if suboption == 1:
            modos_de_juegos.automatico()
        elif suboption == 2:
            modos_de_juegos.manual()
        else:
            continue 
    elif opcion == 2:
        modos_de_juegos.computadora()
    else:
        limpiar()
        print("Gracias por jugar!")
        break
 