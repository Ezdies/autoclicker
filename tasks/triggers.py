import random
import time  # Dla przykładowych danych

# Funkcja aktywująca trigger
def is_trigger_active(trigger_name):
    if trigger_name == "high_cpu_usage":
        return check_cpu_usage() > 80
    if trigger_name == "low_energy":
        return check_energy_level() < 20
    return False

# Mockowe funkcje dla symulacji
def check_cpu_usage():
    return random.randint(0, 100)  # Symulacja użycia CPU

def check_energy_level():
    return random.randint(0, 100)  # Symulacja poziomu energii

# Uruchamianie scenariuszy na podstawie triggerów
def run_scenario_with_triggers(triggers, run_scenario):
    while True:
        for trigger_name, trigger_data in triggers.items():
            if is_trigger_active(trigger_name):
                print(f"Aktywny trigger: {trigger_name}.")
                run_scenario(trigger_data["scenario"])
                time.sleep(trigger_data["frequency"])
