import pyautogui
import pygetwindow as gw
import time

def focus_window(keyword):
    windows = gw.getWindowsWithTitle(keyword)
    if windows:
        windows[0].activate()
        return True
    return False

def perform_action(command):
    if "click" in command and "double" not in command:
        pyautogui.click()
    elif "double click" in command:
        pyautogui.doubleClick()
    elif "right click" in command:
        pyautogui.rightClick()
    elif "scroll down" in command:
        pyautogui.scroll(-800)
    elif "scroll up" in command:
        pyautogui.scroll(800)
    elif "screenshot" in command:
        name = f"screenshot_{int(time.time())}.png"
        pyautogui.screenshot(name)
        print("Screenshot saved:", name)
    else:
        print("Unrecognized action.")
