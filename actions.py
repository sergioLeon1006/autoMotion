import random
import time
import pyautogui


def move_mouse_randomly():
    screen_width, screen_height = pyautogui.size()
    for _ in range(10):
        x = random.randint(0, screen_width)
        y = random.randint(0, screen_height)
        pyautogui.moveTo(x, y, duration=0.5)
        time.sleep(0.5)
