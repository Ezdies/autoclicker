from tasks.buttons import buttons
from screen.recognition import find_element
from screen.capture import capture_screen
from automation.clicker import click

# Funkcja obsługująca kliknięcie przycisku
def click_button(button_name):
    if button_name not in buttons:
        print(f"Błąd: Nie znaleziono przycisku '{button_name}'.")
        return False

    button = buttons[button_name]
    template_path = button["template"]

    # Zrób zrzut ekranu
    screen_path = capture_screen()

    # Znajdź przycisk
    location = find_element(template_path, screen_path)
    if location is None:
        print(f"Nie znaleziono przycisku '{button_name}' na ekranie.")
        return False

    # Kliknij przycisk
    click(*location)
    print(f"Kliknięto przycisk '{button_name}'.")
    return True

# Definicja scenariuszy
scenarios = {
    "start_and_confirm": [
        {"button": "start_task", "description": "Rozpoczęcie zadania"},
        {"button": "confirm_task", "description": "Potwierdzenie zadania"}
    ],
    "cancel_task": [
        {"button": "cancel_task", "description": "Anulowanie zadania"}
    ]
}

# Funkcja uruchamiająca scenariusz
def run_scenario(scenario_name):
    if scenario_name not in scenarios:
        print(f"Błąd: Scenariusz '{scenario_name}' nie istnieje.")
        return False

    scenario = scenarios[scenario_name]
    for step in scenario:
        button_name = step["button"]
        description = step.get("description", f"Kliknij {button_name}")

        print(f"Akcja: {description}")
        success = click_button(button_name)
        if not success:
            print(f"Przerwano scenariusz: nie udało się wykonać '{button_name}'.")
            return False

    print("Scenariusz zakończony sukcesem.")
    return True
