"""
03 — Functions and Abstraction (advanced technique)

Goal:
- Use functions to reduce repetition.
- Make code easier to read and modify.

Run:
- python lessons/03_functions_and_abstraction.py
"""

# --- Example ---
def add(a: int, b: int) -> int:
    return a + b

print("Example add:", add(3, 4))

# --- Example: print menu function ---
def print_menu(menu: dict) -> None:
    print("\nMENU")
    for code, info in menu.items():
        print(f"{code}: {info['name']} - ${info['price']:.2f}")

menu = {
    "A1": {"name": "Muffin", "price": 4.50},
    "B2": {"name": "Juice", "price": 3.00},
}
print_menu(menu)

# --- TODO 1 ---
# Write a function get_item_cost(menu, code) that returns the price for a code.
# Then test it by printing the cost of "A1".

# --- TODO 2 ---
# Write a function calculate_total(menu, order_codes) that returns the total cost.
# Example: order_codes = ["A1", "B2"]

# --- TODO 3 ---
# Write a function format_receipt(menu, order_codes) that returns a multi-line string.
# Example output:
# Receipt:
# - Muffin $4.50
# - Juice $3.00
# Total: $7.50

# --- EXTENSION ---
# Modify calculate_total so it can handle quantities.
# Idea: store order as list of dicts like:
# [{"code": "A1", "qty": 2}, {"code":"B2","qty":1}]
