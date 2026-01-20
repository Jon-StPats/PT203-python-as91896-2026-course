"""
01 — Review Core Skills (fast)

Goal:
- Quickly review the basics you need for the assessment:
  variables, input/output, if, loops, lists/dicts.

Run:
- python lessons/01_review_core_skills.py
"""

print("Review: variables, input/output, if, loops, collections\n")

# --- Examples ---
name = "Sam"     # str
year = 12        # int
print(f"{name} is in Year {year}.")

# Example: selection
answer = input("Type 'y' to continue: ").strip().lower()
if answer == "y":
    print("Continuing...")
else:
    print("Stopping (but the program still runs).")

# Example: loop + list
numbers = [1, 2, 3]
total = 0
for n in numbers:
    total += n
print("Total of list:", total)

# Example: dictionary
item = {"name": "Muffin", "price": 4.50}
print("Item:", item["name"], "costs", item["price"])

# --- TODO 1 ---
# Ask the user for their name and favourite food.
# Print a friendly message using an f-string.

# --- TODO 2 ---
# Ask the user for a whole number.
# Print "Even" or "Odd" using %.

# --- TODO 3 ---
# Create a list of 3 menu items (strings) and print them one per line.

# --- EXTENSION ---
# Create a dictionary that maps an item code (like "A1") to a price.
# Print the price of one code.
