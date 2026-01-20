"""
05 — Program Structure (Merit pathway)

Goal:
- Keep main() small and readable.
- Use functions for separate jobs:
  - display menu
  - get user choice
  - update order
  - calculate total
  - print summary

Run:
- python lessons/05_program_structure_modules.py
"""

MENU = {
    "A1": {"name": "Muffin", "price": 4.50},
    "B2": {"name": "Juice", "price": 3.00},
    "C3": {"name": "Pie", "price": 5.50},
}

def print_menu(menu: dict) -> None:
    print("\nMENU")
    for code, info in menu.items():
        print(f"{code}: {info['name']} - ${info['price']:.2f}")

def get_choice(prompt: str) -> str:
    return input(prompt).strip().upper()

def add_to_order(order: list, code: str) -> None:
    order.append(code)

def calculate_total(menu: dict, order: list) -> float:
    total = 0.0
    for code in order:
        total += menu[code]["price"]
    return total

def main():
    order = []
    print_menu(MENU)

    # --- TODO 1 ---
    # Ask the user for ONE item code and add it to the order.

    # --- TODO 2 ---
    # Print the order list.

    # --- TODO 3 ---
    # Calculate and print the total.

    # --- EXTENSION ---
    # Add a loop so the user can add multiple items until they type "DONE".

if __name__ == "__main__":
    main()
