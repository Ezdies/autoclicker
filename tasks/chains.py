from tasks.triggers import is_trigger_active
from tasks.manager import run_scenario
import time

# Definicja łańcuchów triggerów
trigger_chains = {
    "cpu_and_energy": {
        "triggers": ["high_cpu_usage", "low_energy"],
        "scenarios": ["cancel_task", "start_and_confirm"],
        "reset_on_fail": True,
        "frequency": 5
    }
}

# Monitorowanie łańcucha triggerów
def monitor_trigger_chains():
    active_states = {chain: 0 for chain in trigger_chains}

    while True:
        for chain_name, chain_data in trigger_chains.items():
            triggers = chain_data["triggers"]
            scenarios = chain_data["scenarios"]
            frequency = chain_data["frequency"]
            reset_on_fail = chain_data.get("reset_on_fail", True)

            current_index = active_states[chain_name]

            if current_index < len(triggers):
                current_trigger = triggers[current_index]
                if is_trigger_active(current_trigger):
                    print(f"Aktywny trigger '{current_trigger}' w łańcuchu '{chain_name}'.")
                    run_scenario(scenarios[current_index])
                    active_states[chain_name] += 1
                elif reset_on_fail:
                    print(f"Trigger '{current_trigger}' nieaktywny. Resetuję łańcuch '{chain_name}'.")
                    active_states[chain_name] = 0

            if active_states[chain_name] == len(triggers):
                print(f"Łańcuch '{chain_name}' zakończony sukcesem.")
                active_states[chain_name] = 0

        time.sleep(frequency)
