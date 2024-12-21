import logging
from tasks.manager import run_scenario

# Konfiguracja logowania
logging.basicConfig(
    filename="logs/autoclicker.log",
    level=logging.ERROR,
    format="%(asctime)s [%(levelname)s] %(message)s"
)

def main():
    try:
        print("Dostępne scenariusze: start_and_confirm, cancel_task")
        scenario_name = input("Wybierz scenariusz: ").strip()

        # Uruchom scenariusz zdefiniowany w tasks/manager.py
        success = run_scenario(scenario_name)
        if not success:
            print(f"Scenariusz '{scenario_name}' zakończony niepowodzeniem.")

    except Exception as e:
        logging.error("Nieznany błąd", exc_info=True)
        print(f"Nieznany błąd: {e}")

if __name__ == "__main__":
    main()
