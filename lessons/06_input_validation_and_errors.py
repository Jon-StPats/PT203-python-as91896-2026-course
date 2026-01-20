"""
06 — Input Validation and Error Handling (Excellence pathway)

Goal:
- Prevent crashing
- Keep asking until input is valid
- Use try/except for numeric inputs

Run:
- python lessons/06_input_validation_and_errors.py
"""

MENU = {
    "A1": {"name": "Muffin", "price": 4.50},
    "B2": {"name": "Juice", "price": 3.00},
    "C3": {"name": "Pie", "price": 5.50},
}

def get_valid_code(menu: dict) -> str:
    """Returns a valid code from MENU (keeps asking until valid)."""
    allowed = set(menu.keys())
    while True:
        code = input("Enter item code (or DONE): ").strip().upper()
        if code == "DONE":
            return code
        if code in allowed:
            return code
        print("Invalid code. Try again.")

def get_int(prompt: str) -> int:
    while True:
        text = input(prompt).strip()
        try:
            return int(text)
        except ValueError:
            print("Please enter a whole number.")

def main():
    print("Validation demo.\n")

    # --- Example: valid menu code loop ---
    order = []
    while True:
        code = get_valid_code(MENU)
        if code == "DONE":
            break
        order.append(code)

    print("Order codes:", order)

    # --- Example: safe int input ---
    qty = get_int("Enter a quantity (whole number): ")
    print("Quantity:", qty)

    # --- TODO 1 ---
    # Modify get_int so it rejects numbers <= 0.

    # --- TODO 2 ---
    # Add quantities to the order.
    # Idea: store order as list of dicts:
    # [{"code": "A1", "qty": 2}, ...]

    # --- EXTENSION ---
    # Add a confirmation step:
    # "Are you sure? (y/n)" with validation (only accept y or n).
    # If "n", allow them to continue ordering.

if __name__ == "__main__":
    main()
