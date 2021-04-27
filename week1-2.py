def main():
    print_actions()
    action = get_action()
    if action == 1:
        run_cel_to_fah()
        main()
    elif action == 2:
        run_fah_to_cel()
        main()
    elif action == 3:
        print("Have a nice day!")
    else:
        print("Error, please enter numeric input")
        main()

def print_actions():
    print("-----")
    print("1. Compute Celsius temperature to Fahrenheit temperature")
    print("2. Compute Fahrenheit temperature to Celsius temperature")
    print("3. Exit")
    print("-----")

def get_action() -> int:
    try:
        return int(input("Enter a action: "))
    except:
        print("Error, please enter a action")
        return get_action()

def run_cel_to_fah():
    celsius_value = get_numeric_value("Enter Celsius  temperature: ")
    fahrenheit_value = celsius_value * 9 / 5 + 32
    print("Fahrenheit temperature: ", fahrenheit_value)
    
def run_fah_to_cel():
    fahrenheit_value = get_numeric_value("Enter Fahrenheit temperature: ")
    celsius_value = (fahrenheit_value - 32) * 5 / 9
    print("Celsius temperature: ", celsius_value)

def get_numeric_value(msg: str) -> float:
    try:
        return float(input(msg))
    except:
        print("Error, please enter numeric input")
        return get_numeric_value(msg)

main()