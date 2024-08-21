import time

from actions import move_mouse_randomly
from app import write_to_excel
from events import KeyboardListener

def main():
    # Crear una instancia del listener de teclado
    keyboard_listener = KeyboardListener()
    keyboard_listener.start_listener()

    while keyboard_listener.running:
        # Mover el mouse aleatoriamente
        move_mouse_randomly()
        # Escribir texto en Excel
        write_to_excel("Hola, Excel!")

        # Pausa breve antes de la siguiente iteración del bucle
        time.sleep(1)  # Reduce el intervalo para una detección más rápida

    keyboard_listener.stop_listener()  # Detener el listener de teclado

if __name__ == "__main__":
    main()
