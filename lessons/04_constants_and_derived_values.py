"""
04 — Constants and Derived Values (avoid magic numbers)

Goal:
- Put important values in ONE place (constants).
- Use derived values (like len(...)) instead of hard-coding numbers.

Run:
- python lessons/04_constants_and_derived_values.py
"""

# --- Constants ---
TAX_RATE = 0.15          # 15% tax (example)
MAX_ITEMS = 10           # maximum items per order (example)

# --- Example menu ---
menu = {
    "A1": {"name": "Muffin", "price": 4.50},
    "B2": {"name": "Juice", "price": 3.00},
}

# --- Example: derived value (len) ---
print("Number of menu items:", len(menu))

# --- Example: calculate total with tax ---
subtotal = menu["A1"]["price"] + menu["B2"]["price"]
tax = subtotal * TAX_RATE
total = subtotal + tax
print(f"Subtotal: ${subtotal:.2f} | Tax: ${tax:.2f} | Total: ${total:.2f}")

# --- TODO 1 ---
# Add a constant DISCOUNT_RATE (e.g. 0.10 for 10%).
# Apply it to the subtotal BEFORE tax.

# --- TODO 2 ---
# Ask the user how many items they want to order.
# If it is > MAX_ITEMS, print "Too many items" and stop.

# --- EXTENSION ---
# Make TAX_RATE optional:
# If the user types "student", apply 0% tax.
# Otherwise apply TAX_RATE.
