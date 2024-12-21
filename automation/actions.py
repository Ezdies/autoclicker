from automation.clicker import click

def perform_task(location):
    # Wykonanie kliknięcia w zadanej lokalizacji
    click(*location)
    print("Task został wykonany.")
