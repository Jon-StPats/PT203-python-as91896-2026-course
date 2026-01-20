"""
02 — Collections and Data Models (menu data)

Goal:
- Store menu data in a way that is easy to extend.
- Separate "data" (menu) from "logic" (program steps).

Run:
- python lessons/02_collections_and_data_models.py
"""

# --- Example 1: simple list menu (OK but limited) ---
menu_list = ["A1 Muffin $4.50", "B2 Juice $3.00", "C3 Pie $5.50"]
print("List menu (simple):")
for line in menu_list:
    print("-", line)

print("\n---")

# --- Example 2: dictionary menu (better) ---
# Key = code, Value = another dict with name + price
menu = {
    "A1": {"name": "Muffin", "price": 4.50},
    "B2": {"name": "Juice", "price": 3.00},
    "C3": {"name": "Pie", "price": 5.50},
}

print("Dictionary menu (better):")
for code in menu:
    print(f"{code}: {menu[code]['name']} - ${menu[code]['price']:.2f}")

# --- TODO 1 ---
# Add TWO more items to the menu dictionary.

# --- TODO 2 ---
# Create a function called print_menu(menu_dict) that prints the menu neatly.

# --- TODO 3 ---
# Create an order list and append a chosen item code to it (e.g. "A1").
# Print the order list.

# --- EXTENSION (Excellence-friendly) ---
# Change the menu so items also include a "category" (e.g. "drink", "food")
# Example: {"name": "Juice", "price": 3.0, "category": "drink"}
# Then print only the "drink" items.
