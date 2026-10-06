from utils.printer import print_message

def saludo(name: str):
    """Genera un saludo simple."""
    message = f"¡Hey {name}! ¿Qé tal?"
    print_message(message)

def greet_in_english(name: str):
    """Genera un saludo simple en inglés."""
    message = f"Hello, {name}!"
    print_message(message)