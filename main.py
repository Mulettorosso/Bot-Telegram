import time
import pyperclip
import pyautogui

time.sleep(5)
f = open("spam","r")

for char in f:
    pyperclip.copy(char)
    pyautogui.hotkey('command', 'v', interval=0.02)
    pyautogui.typewrite("\n")
