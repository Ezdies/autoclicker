import os
from config import ADB_PATH, SCREENSHOT_PATH

def capture_screen():
    try:
        os.system(f"{ADB_PATH} exec-out screencap -p > {SCREENSHOT_PATH}")
        if not os.path.exists(SCREENSHOT_PATH):
            raise FileNotFoundError(f"Zrzut ekranu nie został zapisany w: {SCREENSHOT_PATH}")
        return SCREENSHOT_PATH
    except Exception as e:
        raise RuntimeError(f"Nie udało się wykonać zrzutu ekranu: {e}")
