# Author: Cherouise Mickael
# Date: 2023-02-08
# Description: A piece of code to simulate click, record a sequence of click and to replay it 

import keyboard
import pyautogui
import win32api
import win32con
import time

recording = False
sequence = []

def on_press_w(key):
    print(f"{key.name} pressed", flush=True)
    global recording
    if key.name == "w":
        if recording:
            recording = False
        else:
            recording = True
            sequence.clear()

def on_press_x(key):
    print(f"{key.name} pressed", flush=True)
    global sequence
    if key.name == "x":
        for pos in sequence:
            pyautogui.click(*pos[0:2], interval=pos[2])

def on_press_f2(key):
    print(f"{key.name} pressed", flush=True)
    if key.name == "f2":
        x, y = win32api.GetCursorPos()
        pyautogui.click(x, y)

keyboard.on_press(on_press_w)
keyboard.on_press(on_press_x)
keyboard.on_press(on_press_f2)

start = time.time()
while True:
    if recording:
        pos = pyautogui.position()
        sequence.append((pos, time.time()-start))
    keyboard.wait()
    time.sleep(0.1)
