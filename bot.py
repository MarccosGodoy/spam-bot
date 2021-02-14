import pyautogui
import time

with open("spam.txt", "r") as f:
    time.sleep(5)
    for words in f:
        print(words)
        pyautogui.typewrite(words)
        pyautogui.press("enter")
        time.sleep(3)
