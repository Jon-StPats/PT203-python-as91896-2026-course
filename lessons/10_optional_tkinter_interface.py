"""
10 — Optional Tkinter Interface (Excellence extension)

IMPORTANT:
- Tkinter is OPTIONAL.
- A GUI does NOT replace the requirement to show advanced programming techniques.
- Best approach: keep ordering logic in functions, then GUI calls those functions.

Run:
- python lessons/10_optional_tkinter_interface.py
"""

import tkinter as tk

MENU = {
    "A1": {"name": "Muffin", "price": 4.50},
    "B2": {"name": "Juice", "price": 3.00},
    "C3": {"name": "Pie", "price": 5.50},
}

order_codes: list[str] = []

def calculate_total(menu: dict, order: list[str]) -> float:
    total = 0.0
    for code in order:
        total += menu[code]["price"]
    return total

def add_code(code: str, status_label: tk.Label, total_label: tk.Label) -> None:
    code = code.strip().upper()
    if code not in MENU:
        status_label.config(text="Invalid code")
        return
    order_codes.append(code)
    status_label.config(text=f"Added {code}")
    total_label.config(text=f"Total: ${calculate_total(MENU, order_codes):.2f}")

def build_gui():
    root = tk.Tk()
    root.title("Ordering System (Tkinter Demo)")

    tk.Label(root, text="Enter item code (A1/B2/C3):").pack(padx=10, pady=5)

    entry = tk.Entry(root)
    entry.pack(padx=10, pady=5)

    status = tk.Label(root, text="Ready")
    status.pack(padx=10, pady=5)

    total = tk.Label(root, text="Total: $0.00")
    total.pack(padx=10, pady=5)

    def on_add():
        add_code(entry.get(), status, total)
        entry.delete(0, tk.END)

    tk.Button(root, text="Add Item", command=on_add).pack(padx=10, pady=10)

    menu_text = "\\n".join([f"{c}: {MENU[c]['name']} ${MENU[c]['price']:.2f}" for c in MENU])
    tk.Label(root, text="Menu:\\n" + menu_text, justify="left").pack(padx=10, pady=5)

    # --- TODO 1 ---
    # Add a "Clear Order" button that empties order_codes and resets total.

    # --- TODO 2 ---
    # Add a receipt area (Label) that lists chosen items.

    root.mainloop()

if __name__ == "__main__":
    build_gui()
