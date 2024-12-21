import logging
from tasks.manager import run_scenario
from tasks.triggers import run_scenario_with_triggers
from tasks.chains import monitor_trigger_chains

# Konfiguracja logowania
logging.basicConfig(
    filename="logs/autoclicker.log",
    level=logging.ERROR,
    format="%(asctime)s [%(levelname)s] %(message)s"
)

def main():
    try:
        print("Wybierz tryb pracy:")
        print("1. Manualne uruchamianie scenariusza")
        print("2. Automatyczne uruchamianie na podstawie triggerów")
        print("3. Monitorowanie łańcuchów triggerów")

        choice = input("Twój wybór (1/2/3): ").strip()
        if choice == "1":
            print("Dostępne scenariusze: start_and_confirm, cancel_task")
            scenario_name = input("Wybierz scenariusz: ").strip()

            # Uruchom scenariusz zdefiniowany w tasks/manager.py
            success = run_scenario(scenario_name)
            if not success:
                print(f"Scenariusz '{scenario_name}' zakończony niepowodzeniem.")

        elif choice == "2":
            print("Uruchamianie w trybie automatycznym na podstawie triggerów...")
            triggers = {
                "high_cpu_usage": {"scenario": "cancel_task", "frequency": 5},
                "low_energy": {"scenario": "start_and_confirm", "frequency": 10},
            }
            run_scenario_with_triggers(triggers, run_scenario)

        elif choice == "3":
            print("Monitorowanie łańcuchów triggerów...")
            monitor_trigger_chains()

        else:
            print("Nieprawidłowy wybór. Wybierz 1, 2 lub 3.")

    except Exception as e:
        logging.error("Nieznany błąd", exc_info=True)
        print(f"Nieznany błąd: {e}")

if __name__ == "__main__":
    main()
