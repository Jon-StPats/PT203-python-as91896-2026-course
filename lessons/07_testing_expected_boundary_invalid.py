"""
07 — Testing (Expected / Boundary / Invalid)

Goal:
- Design meaningful tests
- Record tests in docs/TESTING.md
- Learn what boundary + invalid tests look like

Run:
- python lessons/07_testing_expected_boundary_invalid.py
"""

MENU = {
    "A1": {"name": "Muffin", "price": 4.50},
    "B2": {"name": "Juice", "price": 3.00},
}

def calculate_total(menu: dict, order_codes: list[str]) -> float:
    total = 0.0
    for code in order_codes:
        total += menu[code]["price"]
    return total

print("Expected test: order ['A1'] should total 4.50")
print("Actual:", calculate_total(MENU, ["A1"]))

print("\nBoundary test: empty order [] should total 0.00")
print("Actual:", calculate_total(MENU, []))

# --- TODO 1 (Expected) ---
# Add a test for ['A1','B2'] and check the total is 7.50

# --- TODO 2 (Boundary) ---
# Add a test for a large order (e.g., 10 items) and check it still works.

# --- TODO 3 (Invalid) ---
# What happens if order_codes contains an invalid code like 'X9'?
# Try it and write what happens.

# --- EXTENSION ---
# Modify calculate_total so it handles invalid codes safely:
# - If code not in menu, skip it (or raise a friendly error)
# Then re-test the invalid case.
