import pyautogui
import time

def automation_pyautogui():
    # Wait for a few seconds before starting
    time.sleep(5)

    # Move the mouse to coordinates (x, y)
    pyautogui.moveTo(100, 100)

    # Click the left mouse button
    pyautogui.click()

    # Type text
    pyautogui.write("Hello, world!")

    # Press the Enter key
    pyautogui.press("enter")

    # Perform a key combination (Ctrl+C)
    pyautogui.hotkey("ctrl", "c")

if __name__ == "__main__":
    automation_pyautogui()
