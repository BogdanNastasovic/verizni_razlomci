import math
import tkinter as tk
from tkinter import messagebox

def continued_fraction(x, max_terms=10, tol=1e-12):
    """
    Funkcija koja računa koeficijente kontinuiranog razlomka (continued fraction)
    za zadati broj x.
    """
    a = []
    for _ in range(max_terms):
        integer_part = int(math.floor(x))
        a.append(integer_part)
        frac_part = x - integer_part
        if abs(frac_part) < tol:
            break
        x = 1 / frac_part
    return a

def calculate_cf():
    """Računa i prikazuje rezultat u GUI-ju."""
    expr = entry.get().strip()
    if expr.lower() in {"q", "exit"}:
        root.destroy()
        return

    try:
        # Ograničavamo eval na samo math funkcije
        x = eval(expr, {"__builtins__": None, "math": math})
    except Exception as e:
        messagebox.showerror("Greška", f"Nevažeći unos: {e}")
        return

    cf = continued_fraction(x)
    if len(cf) == 1:
        result = f"[{cf[0]}]"
    else:
        result = f"[{cf[0]}; {', '.join(map(str, cf[1:]))}]"

    result_label.config(text=result)

def clear_input():
    """Briše unos i rezultat."""
    entry.delete(0, tk.END)
    result_label.config(text="")

# Glavni prozor
root = tk.Tk()
root.title("Kontinuirani razlomci")
root.geometry("400x250")
root.resizable(False, False)

# Naslov
title_label = tk.Label(root, text="Alat za izračunavanje kontinuiranih razlomaka", font=("Arial", 12, "bold"))
title_label.pack(pady=10)

# Polje za unos izraza
entry = tk.Entry(root, width=30, font=("Arial", 12))
entry.pack(pady=5)
entry.insert(0, "2**0.5")  # Početni primer

# Dugmad
button_frame = tk.Frame(root)
button_frame.pack(pady=5)

calc_button = tk.Button(button_frame, text="Izračunaj", command=calculate_cf, font=("Arial", 10))
calc_button.grid(row=0, column=0, padx=5)

clear_button = tk.Button(button_frame, text="Obriši", command=clear_input, font=("Arial", 10))
clear_button.grid(row=0, column=1, padx=5)

exit_button = tk.Button(button_frame, text="Izađi", command=root.destroy, font=("Arial", 10))
exit_button.grid(row=0, column=2, padx=5)

# Labela za rezultat
result_label = tk.Label(root, text="", font=("Courier", 12))
result_label.pack(pady=15)

# Uputstvo
info_label = tk.Label(root, text="Koristi ** umesto ^ za stepen. Primer: 2**(1/2) = 2^(1/2) = Koren broja 2. \n Ostalo: math.pi (broj pi), math.e (broj e)", font=("Arial", 10))
info_label.pack(pady=5)

root.mainloop()
