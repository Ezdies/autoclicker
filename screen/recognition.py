import cv2
import os

def find_element(template_path, screen_path):
    try:
        if not os.path.exists(template_path):
            raise FileNotFoundError(f"Nie znaleziono szablonu: {template_path}")
        if not os.path.exists(screen_path):
            raise FileNotFoundError(f"Nie znaleziono zrzutu ekranu: {screen_path}")

        screen = cv2.imread(screen_path)
        template = cv2.imread(template_path)

        if screen is None or template is None:
            raise FileNotFoundError("Błąd wczytywania obrazu.")

        result = cv2.matchTemplate(screen, template, cv2.TM_CCOEFF_NORMED)
        _, max_val, _, max_loc = cv2.minMaxLoc(result)

        if max_val >= 0.8:
            return max_loc
        return None
    except Exception as e:
        print(f"Błąd w find_element: {e}")
        return None
