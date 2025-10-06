# circumference_calculator.py
import math

def circumference_from_radius(r: float) -> float:
    return 2 * math.pi * r

def circumference_from_diameter(d: float) -> float:
    return math.pi * d

def get_positive_number(prompt: str) -> float:
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                print("Please enter a number greater than 0.")
                continue
            return value
        except ValueError:
            print("Invalid input — please enter a numeric value.")

def main():
    print("Circumference Calculator")
    print("------------------------")
    print("Choose input type:")
    print("1. Radius")
    print("2. Diameter")
    choice = input("Enter 1 or 2: ").strip()

    if choice == "1":
        r = get_positive_number("Enter radius: ")
        c = circumference_from_radius(r)
        print(f"Circumference = 2 × π × {r} = {c:.6f}")
    elif choice == "2":
        d = get_positive_number("Enter diameter: ")
        c = circumference_from_diameter(d)
        print(f"Circumference = π × {d} = {c:.6f}")
    else:
        print("Invalid choice. Please run the program again and enter 1 or 2.")

if __name__ == "__main__":
    main()
