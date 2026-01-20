"""
09 — Refinement and Flexibility (Excellence)

Goal:
- Make your program easy to change and extend.
- Reduce hard-coding.
- Improve user experience without adding huge complexity.

Run:
- python lessons/09_refinement_and_flexibility.py
"""

MENU = {
    "A1": {"name": "Muffin", "price": 4.50, "category": "food"},
    "B2": {"name": "Juice", "price": 3.00, "category": "drink"},
    "C3": {"name": "Pie", "price": 5.50, "category": "food"},
}

def get_codes(menu: dict) -> list[str]:
    """Derived value: list of valid codes."""
    return list(menu.keys())

def print_menu(menu: dict, category: str | None = None) -> None:
    print("\\nMENU")
    for code, info in menu.items():
        if category is None or info["category"] == category:
            print(f"{code}: {info['name']} - ${info['price']:.2f}")
    print()

print_menu(MENU)
print("Valid codes are derived from the data:", get_codes(MENU))

# --- TODO 1 ---
# Add a function that returns a list of categories (derived from MENU data).

# --- TODO 2 ---
# Allow the user to filter the menu by category (e.g. only "drink").

# --- TODO 3 ---
# Add a constant for a discount (e.g. 10%) and apply it if the user orders 3+ items.

# --- EXTENSION ---
# Implement "remove item from order" (with validation).
# Tip: ask for a code to remove, and only remove if it is in the order list.
