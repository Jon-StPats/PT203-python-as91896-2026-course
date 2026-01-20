"""
08 — Mini POS Scaffold (CLI) — Foundation for the assessment

Goal:
- Bring everything together into a working ordering system.
- This is a strong starting point for src/main.py.

Run:
- python lessons/08_mini_pos_scaffold.py
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
    print("Type DONE to finish.\n")

def get_valid_code(menu: dict) -> str:
    allowed = set(menu.keys())
    while True:
        code = input("Enter item code (or DONE): ").strip().upper()
        if code == "DONE" or code in allowed:
            return code
        print("Invalid code. Try again.")

def calculate_total(menu: dict, order: list[str]) -> float:
    total = 0.0
    for code in order:
        total += menu[code]["price"]
    return total

def format_receipt(menu: dict, order: list[str]) -> str:
    lines = ["Receipt:"]
    for code in order:
        item = menu[code]
        lines.append(f"- {item['name']} ${item['price']:.2f}")
    lines.append(f"Total: ${calculate_total(menu, order):.2f}")
    return "\\n".join(lines)

def main():
    order = []

    print_menu(MENU)

    # --- TODO 1 ---
    # Loop: ask for item codes using get_valid_code and append to order.
    # Stop when the user enters DONE.

    # --- TODO 2 ---
    # If the order is empty, print "No items ordered" and exit.

    # --- TODO 3 ---
    # Print the receipt using format_receipt.

    # --- EXTENSION (Excellence-friendly) ---
    # Add quantities:
    # - store order as list of dicts: [{"code":"A1","qty":2}, ...]
    # - update total and receipt formatting

if __name__ == "__main__":
    main()
