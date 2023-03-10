# Author: Cherouise Mickael
# Date: 2023-02-08
# Description: A piece of code to simulate click, record a sequence of click and to replay it, v2
import keyboard
import time
import win32api
import win32con
import random

clicks = []
recording = False
executing = False
def on_press_f2(key):
    if key.name == 'f2':
        x, y = win32api.GetCursorPos()
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x, y, 0, 0)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x, y, 0, 0)
        
def on_press_w(key):
    global recording, clicks
    if not recording and keyboard.is_pressed("w"):
        clicks = []
        recording = True
        print("recording...", flush = True)
    elif recording and keyboard.is_pressed("w"):
        recording = False
        print("not recording.", flush = True)
        
def on_press_x(key):
    global clicks, executing
    if not executing and keyboard.is_pressed("x"):
        executing = True
        for i, click in enumerate(clicks):
            x, y, t = click
            if i > 0:
                sleep_time = clicks[i][2] - clicks[i-1][2]
                sleep_time = sleep_time + random.uniform(-0.1,0.1)
                print(f"Sleep Time = {sleep_time}", flush=True)
                time.sleep(sleep_time)
            win32api.SetCursorPos((x, y))
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x, y, 0, 0)
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x, y, 0, 0)
    executing = False
            
keyboard.on_press_key("f2", on_press_f2)
keyboard.on_press_key("w", on_press_w)
keyboard.on_press_key("x", on_press_x)

while True:
    if recording and (win32api.GetKeyState(win32con.VK_LBUTTON) < 0):
        x, y = win32api.GetCursorPos()
        t = time.time()
        clicks.append((x, y, t))
        while(win32api.GetKeyState(win32con.VK_LBUTTON) < 0):
            print("holded", flush=True)
        print("relached", flush=True)
