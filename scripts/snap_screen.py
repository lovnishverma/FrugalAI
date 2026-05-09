import pyautogui
import sys
import os
from datetime import datetime


def take_snap():
    path = r"C:\Users\princ\Pictures\Screenshots"
    filename = f"snap_{datetime.now().strftime('%H%M%S')}.png"
    fullpath = os.path.join(path, filename)

    pyautogui.screenshot(fullpath)
    print(f"Screenshot saved: {fullpath}")


if __name__ == "__main__":
    take_snap()
    sys.stdout.flush()
    sys.exit(0)
