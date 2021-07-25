import tkinter as tk
import tkinter.font as font
from tkinter import ttk

try:
    from ctypes import windll
    windll.shcore.SetProcessDpiAwareness(1)
except:
    pass

# Create the master object

master = tk.Tk()
master.title("PetHelper3000")
master.geometry("400x800")

# Weight variables

weight_value = tk.StringVar()

# Dose variables

dose_value = tk.StringVar()
dose_value2 = tk.StringVar()
dose_value3 = tk.StringVar()

# Calculations

def calculate_med1(*args):
    try:
        weight = float(weight_value.get())
        dosage = weight * 2
        dose_value.set(f"{dosage:.3f}")
    except ValueError:
        pass

def calculate_med2(*args):
    try:
        weight = float(weight_value.get())
        dosage2 = weight * 10
        dose_value2.set(f"{dosage2:.3f}")
    except ValueError:
        pass

def calculate_med3(*args):
    try:
        weight = float(weight_value.get())
        dosage3 = weight * 100
        dose_value3.set(f"{dosage3:.3f}")
    except ValueError:
        pass

# Font

font.nametofont("TkDefaultFont").configure(size=15)

# Amount Label

tk.Label(master, text="Weight: ").grid(row=0, column=0)

# Amount entry

e1 = tk.Entry(master, textvariable=weight_value)

# Calc Button

calc_button = ttk.Button(master,
                         text="Calculate",
                         command=lambda:[calculate_med1(),
                                         calculate_med2(),
                                         calculate_med3()]
)



# Medicine and Amount widgets

m1 = tk.Label(master, text="Med 1")
a1 = tk.Label(master, textvariable=f"{dose_value}")

m2 = tk.Label(master, text="Med 2")
a2 = tk.Label(master, textvariable=f"{dose_value2}")

m3 = tk.Label(master, text="Med 3")
a3 = tk.Label(master, textvariable=f"{dose_value3}")

m4 = tk.Label(master, text="Med 4")
a4 = tk.Label(master, text="Amount 4")

m5 = tk.Label(master, text="Med 5")
a5 = tk.Label(master, text="Amount 5")

m6 = tk.Label(master, text="Med 6")
a6 = tk.Label(master, text="Amount 6")

m7 = tk.Label(master, text="Med 7")
a7 = tk.Label(master, text="Amount 7")

m8 = tk.Label(master, text="Med 8")
a8 = tk.Label(master, text="Amount 8")

m9 = tk.Label(master, text="Med 9")
a9 = tk.Label(master, text="Amount 9")

m10 = tk.Label(master, text="Med 10")
a10 = tk.Label(master, text="Amount 10")

m11 = tk.Label(master, text="Med 11")
a11 = tk.Label(master, text="Amount 11")

m12 = tk.Label(master, text="Med 12")
a12 = tk.Label(master, text="Amount 12")

m13 = tk.Label(master, text="Med 13")
a13 = tk.Label(master, text="Amount 13")

m14 = tk.Label(master, text="Med 14")
a14 = tk.Label(master, text="Amount 14")

m15 = tk.Label(master, text="Med 15")
a15 = tk.Label(master, text="Amount 15")

m16 = tk.Label(master, text="Med 16")
a16 = tk.Label(master, text="Amount 16")

m17 = tk.Label(master, text="Med 17")
a17 = tk.Label(master, text="Amount 17")

m18 = tk.Label(master, text="Med 18")
a18 = tk.Label(master, text="Amount 18")

m19 = tk.Label(master, text="Med 19")
a19 = tk.Label(master, text="Amount 19")

m20 = tk.Label(master, text="Med 20")
a20 = tk.Label(master, text="Amount 20")

m21 = tk.Label(master, text="Med 21")
a21 = tk.Label(master, text="Amount 21")

m22 = tk.Label(master, text="Med 22")
a22 = tk.Label(master, text="Amount 22")

m23 = tk.Label(master, text="Med 23")
a23 = tk.Label(master, text="Amount 23")

m24 = tk.Label(master, text="Med 24")
a24 = tk.Label(master, text="Amount 24")

m25 = tk.Label(master, text="Med 25")
a25 = tk.Label(master, text="Amount 25")

# Layout

calc_button.grid(column=3, row=0, columnspan=1, sticky="EW")

m1.grid(row=1, column=0)
a1.grid(row=1, column=1)

m2.grid(row=2, column=0)
a2.grid(row=2, column=1)

m3.grid(row=3, column=0)
a3.grid(row=3, column=1)

m4.grid(row=4, column=0)
a4.grid(row=4, column=1)

m5.grid(row=5, column=0)
a5.grid(row=5, column=1)

m6.grid(row=6, column=0)
a6.grid(row=6, column=1)

m7.grid(row=7, column=0)
a7.grid(row=7, column=1)

m8.grid(row=8, column=0)
a8.grid(row=8, column=1)

m9.grid(row=9, column=0)
a9.grid(row=9, column=1)

m10.grid(row=10, column=0)
a10.grid(row=10, column=1)

m11.grid(row=11, column=0)
a11.grid(row=11, column=1)

m12.grid(row=12, column=0)
a12.grid(row=12, column=1)

m13.grid(row=13, column=0)
a13.grid(row=13, column=1)

m14.grid(row=13, column=0)
a14.grid(row=13, column=1)

m15.grid(row=14, column=0)
a15.grid(row=14, column=1)

m16.grid(row=15, column=0)
a16.grid(row=15, column=1)

m17.grid(row=16, column=0)
a17.grid(row=16, column=1)

m18.grid(row=17, column=0)
a18.grid(row=17, column=1)

m19.grid(row=18, column=0)
a19.grid(row=18, column=1)

m20.grid(row=19, column=0)
a20.grid(row=19, column=1)

m21.grid(row=20, column=0)
a21.grid(row=20, column=1)

m22.grid(row=21, column=0)
a22.grid(row=21, column=1)

m23.grid(row=22, column=0)
a23.grid(row=22, column=1)

m24.grid(row=23, column=0)
a24.grid(row=23, column=1)

m25.grid(row=23, column=0)
a25.grid(row=23, column=1)

# winfo_children stands for "widget info children", and gets all the children of a widget.
for child in master.winfo_children():
    child.grid_configure(padx=10, pady=10)

# Medicine to weight ratio calculations

# Pack them using grid
e1.grid(row=0, column=1)

# Keybinds

master.bind("<Return>", calculate_med1)
master.bind("<KP_Enter>", calculate_med1)

# The mainloop
tk.mainloop()
