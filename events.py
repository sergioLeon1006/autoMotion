# keyboard_listener.py
from pynput import keyboard
import threading

class KeyboardListener:
    def __init__(self):
        self.running = True
        self.listener = None

    def on_press(self, key):
        try:
            if key == keyboard.Key.esc:
                print("Tecla ESC detectada. Terminando...")
                self.running = False
        except Exception as e:
            print(f'Error al procesar la tecla: {e}')

    def start_listener(self):
        # Configurar el listener de teclas
        self.listener = keyboard.Listener(on_press=self.on_press)
        self.listener.start()

    def stop_listener(self):
        if self.listener:
            self.listener.stop()
