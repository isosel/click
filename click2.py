# Author: Cherouise Mickael
# Date: 2023-02-08
# Description: A piece of code to simulate click, record a sequence of click and to replay it, v2
import keyboard
import time
import win32api
import win32con

clicks = []
recording = False

def on_press_f2(key):
    if key.name == 'f2':
        x, y = win32api.GetCursorPos()
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x, y, 0, 0)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x, y, 0, 0)
        
def on_press_w(key):
    global recording
    if not recording and keyboard.is_pressed("w"):
        recording = True
    elif recording and not keyboard.is_pressed("w"):
        recording = False
        
def on_press_x(key):
    global clicks
    if keyboard.is_pressed("x"):
        for click in clicks:
            x, y, t = click
            time.sleep(t)
            win32api.SetCursorPos((x, y))
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x, y, 0, 0)
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x, y, 0, 0)

keyboard.on_press_key("f2", on_press_f2)
keyboard.on_press_key("w", on_press_w)
keyboard.on_press_key("x", on_press_x)

while True:
    if recording:
        x, y = win32api.GetCursorPos()
        t = time.time()
        clicks.append((x, y, t))
    time.sleep(0.1)