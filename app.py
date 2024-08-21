import pyautogui
import subprocess
import psutil
import pygetwindow as gw
import time
import random

#app =  Excel

# Función para mover el mouse por la pantalla de manera aleatoria
def move_mouse_randomly():
    screen_width, screen_height = pyautogui.size()
    for _ in range(10):
        x = random.randint(0, screen_width)
        y = random.randint(0, screen_height)
        pyautogui.moveTo(x, y, duration=0.5)
        time.sleep(0.1)  # Reduzca el tiempo de espera para mayor sensibilidad


# Función para verificar si Excel está abierto
def is_excel_open():
    for proc in psutil.process_iter(['name']):
        if proc.info['name'] == 'EXCEL.EXE':
            return True
    return False


# Función para activar la ventana de Excel
def activate_excel_window():
    excel_windows = gw.getWindowsWithTitle('Excel')  # Buscar ventanas de Excel
    if excel_windows:
        excel_windows[0].activate()
        return True
    return False


# Función para escribir texto en Excel
def write_to_excel(text):
    if not is_excel_open():
        # Usar el comando start para abrir Excel
        subprocess.Popen(['start', 'excel'], shell=True)

    while not activate_excel_window():
        time.sleep(0.5)

    time.sleep(2)  # Esperar un poco para asegurarse de que Excel esté listo

    pyautogui.hotkey('ctrl', 'home')  # Moverse a la celda A1
    time.sleep(0.5)

    pyautogui.typewrite(text, interval=0.1)