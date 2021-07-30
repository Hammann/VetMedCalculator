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
master.geometry("1600x800")

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

GM_Label = tk.Label(master, text="General Medications")
Dosage = tk.Label(master, text="Dosage")
Species = tk.Label(master, text="Species")
MGperKG = tk.Label(master, text="mg/kg")
Unit = tk.Label(master, text="Unit")
Route = tk.Label(master, text="Route")
Frequency = tk.Label(master, text="Frequency")
Duration = tk.Label(master, text="Duration")
Used_For = tk.Label(master, text="Used for")


 = tk.Label(master, text="")
_Dosage = tk.Label(master, textvariable=f"{dose_value2}")
_Species = tk.Label(master, text="")
_MGperKG = tk.Label(master, text="")
_Unit = tk.Label(master, text="")
_Route = tk.Label(master, text="")
_Frequency = tk.Label(master, text="")
_Duration = tk.Label(master, text="")
_Used_For = tk.Label(master, text="")

Activyl_Plus = tk.Label(master, text="Activyl Plus (dogs only, 8+ Weeks)")
Activyl_Plus_Dosage = tk.Label(master, textvariable=f"{dose_value2}")
Activyl_Species = tk.Label(master, text="Dogs")
Activyl_MGperKG = tk.Label(master, text="")
Activyl_Unit = tk.Label(master, text="")
Activyl_Route = tk.Label(master, text="Tropical")
Activyl_Frequency = tk.Label(master, text="SID")
Activyl_Duration = tk.Label(master, text="Once a month")
Activyl_Used_For = tk.Label(master, text="Flea & Tick Preventative")

Albon_50mg_1 = tk.Label(master, text="Albon (50mg/ml) Day 1")
Albon_50mg_1_Dosage = tk.Label(master, textvariable=f"{dose_value3}")
Albon_50mg_1_Species = tk.Label(master, text="")
Albon_50mg_1_MGperKG = tk.Label(master, text="55")
Albon_50mg_1_Unit = tk.Label(master, text="ml")
Albon_50mg_1_Route = tk.Label(master, text="PO")
Albon_50mg_1_Frequency = tk.Label(master, text="SID")
Albon_50mg_1_Duration = tk.Label(master, text="Day 1")
Albon_50mg_1_Used_For = tk.Label(master, text="Second option for Coccidia")

Albon_50mg_2_10 = tk.Label(master, text="Albon (50mg/ml) Days 2-10")
Albon_50mg_2_10_Dosage = tk.Label(master, textvariable=f"{dose_value3}")
Albon_50mg_2_10_Species = tk.Label(master, text="")
Albon_50mg_2_10_MGperKG = tk.Label(master, text="27.5")
Albon_50mg_2_10_Unit = tk.Label(master, text="ml")
Albon_50mg_2_10_Route = tk.Label(master, text="PO")
Albon_50mg_2_10_Frequency = tk.Label(master, text="SID")
Albon_50mg_2_10_Duration = tk.Label(master, text="Days 2-10")
Albon_50mg_2_10_Used_For = tk.Label(master, text="2nd option for Coccidia")

Albon_500mg_1 = tk.Label(master, text="Albon (500mg tablets) Day 1")
Albon_500mg_1_Dosage = tk.Label(master, textvariable=f"{dose_value3}")
Albon_500mg_1_Species = tk.Label(master, text="")
Albon_500mg_1_MGperKG = tk.Label(master, text="55")
Albon_500mg_1_Unit = tk.Label(master, text="mg")
Albon_500mg_1_Route = tk.Label(master, text="PO")
Albon_500mg_1_Frequency = tk.Label(master, text="SID")
Albon_500mg_1_Duration = tk.Label(master, text="Day 1")
Albon_500mg_1_Used_For = tk.Label(master, text="Second option for Coccidia")

Albon_500mg_2_10 = tk.Label(master, text="Albon (500mg tablets) Days 2-10")
Albon_500mg_2_10_Dosage = tk.Label(master, textvariable=f"{dose_value3}")
Albon_500mg_2_10_Species = tk.Label(master, text="")
Albon_500mg_2_10_MGperKG = tk.Label(master, text="28")
Albon_500mg_2_10_Unit = tk.Label(master, text="mg")
Albon_500mg_2_10_Route = tk.Label(master, text="PO")
Albon_500mg_2_10_Frequency = tk.Label(master, text="SID")
Albon_500mg_2_10_Duration = tk.Label(master, text="Days 2-10")
Albon_500mg_2_10_Used_For = tk.Label(master, text="2nd option for Coccidia")

Amoxicillin_under7LB = tk.Label(master, text="Amoxicillin (50 mg/ml) 7 lbs and under")
Amoxicillin_under7LB_Dosage = tk.Label(master, textvariable=f"{dose_value2}")
Amoxicillin_under7LB_Species = tk.Label(master, text="cats/dogs")
Amoxicillin_under7LB_MGperKG = tk.Label(master, text="11")
Amoxicillin_under7LB_Unit = tk.Label(master, text="ml")
Amoxicillin_under7LB_Route = tk.Label(master, text="PO")
Amoxicillin_under7LB_Frequency = tk.Label(master, text="BID")
Amoxicillin_under7LB_Duration = tk.Label(master, text="10 Days")
Amoxicillin_under7LB_Used_For = tk.Label(master, text="Antibiotic")

Amoxicillin_over7LB = tk.Label(master, text="Amoxicillin (100, 250, 500 mg tablets) over 7 lbs")
Amoxicillin_over7LB_Dosage = tk.Label(master, textvariable=f"{dose_value2}")
Amoxicillin_over7LB_Species = tk.Label(master, text="cats/dogs")
Amoxicillin_over7LB_MGperKG = tk.Label(master, text="11")
Amoxicillin_over7LB_Unit = tk.Label(master, text="mg")
Amoxicillin_over7LB_Route = tk.Label(master, text="PO")
Amoxicillin_over7LB_Frequency = tk.Label(master, text="BID")
Amoxicillin_over7LB_Duration = tk.Label(master, text="10 Days")
Amoxicillin_over7LB_Used_For = tk.Label(master, text="Antibiotic")

Azithromycin = tk.Label(master, text="Azithromycin (40 mg/ml)")
Azithromycin_Dosage = tk.Label(master, textvariable=f"{dose_value2}")
Azithromycin_Species = tk.Label(master, text="")
Azithromycin_MGperKG = tk.Label(master, text="5")
Azithromycin_Unit = tk.Label(master, text="ml")
Azithromycin_Route = tk.Label(master, text="PO")
Azithromycin_Frequency = tk.Label(master, text="SID")
Azithromycin_Duration = tk.Label(master, text="10 Days")
Azithromycin_Used_For = tk.Label(master, text="URI (feline) - second choice; round up")

Baytril_tablets = tk.Label(master, text="Baytril (tablets)")
Baytril_tablets_Dosage = tk.Label(master, textvariable=f"{dose_value2}")
Baytril_tablets_Species = tk.Label(master, text="dogs")
Baytril_tablets_MGperKG = tk.Label(master, text="10")
Baytril_tablets_Unit = tk.Label(master, text="mg")
Baytril_tablets_Route = tk.Label(master, text="PO")
Baytril_tablets_Frequency = tk.Label(master, text="SID")
Baytril_tablets_Duration = tk.Label(master, text="As directed by DVM")
Baytril_tablets_Used_For = tk.Label(master, text="Antibiotic, uses only if directed by DVM")

Baytril_22point7 = tk.Label(master, text="Baytril (22.7 mg/ml)")
Baytril_22point7_Dosage = tk.Label(master, textvariable=f"{dose_value2}")
Baytril_22point7_Species = tk.Label(master, text="dogs")
Baytril_22point7_MGperKG = tk.Label(master, text="5")
Baytril_22point7_Unit = tk.Label(master, text="ml")
Baytril_22point7_Route = tk.Label(master, text="IM")
Baytril_22point7_Frequency = tk.Label(master, text="SID")
Baytril_22point7_Duration = tk.Label(master, text="As directed by DVM")
Baytril_22point7_Used_For = tk.Label(master, text="Antibiotic, use only if directed by DVM")

Baytril_100 = tk.Label(master, text="cats")
Baytril_100_Dosage = tk.Label(master, textvariable=f"{dose_value2}")
Baytril_100_Species = tk.Label(master, text="cats")
Baytril_100_MGperKG = tk.Label(master, text="5")
Baytril_100_Unit = tk.Label(master, text="ml")
Baytril_100_Route = tk.Label(master, text="IM")
Baytril_100_Frequency = tk.Label(master, text="SID")
Baytril_100_Duration = tk.Label(master, text="5 days")
Baytril_100_Used_For = tk.Label(master, text="Antibiotic, use only if directed by DVM for severe URI, intolerant of oral meds; round down")

Cephalexin_250_500mg_tablets = tk.Label(master, text="Cephalexin_250_500mg_tablets")
Cephalexin_250_500mg_tablets_Dosage = tk.Label(master, textvariable=f"{dose_value2}")
Cephalexin_250_500mg_tablet_Species = tk.Label(master, text="dogs")
Cephalexin_250_500mg_tablets_MGperKG = tk.Label(master, text="22")
Cephalexin_250_500mg_tablets_Unit = tk.Label(master, text="mg")
Cephalexin_250_500mg_tablets_Route = tk.Label(master, text="PO")
Cephalexin_250_500mg_tablets_Frequency = tk.Label(master, text="BID")
Cephalexin_250_500mg_tablets_Duration = tk.Label(master, text="14 days")
Cephalexin_250_500mg_tablets_Used_For = tk.Label(master, text="Skin - pyoderma in dogs")

 = tk.Label(master, text="")
_Dosage = tk.Label(master, textvariable=f"{dose_value2}")
_Species = tk.Label(master, text="")
_MGperKG = tk.Label(master, text="")
_Unit = tk.Label(master, text="")
_Route = tk.Label(master, text="")
_Frequency = tk.Label(master, text="")
_Duration = tk.Label(master, text="")
_Used_For = tk.Label(master, text="")

 = tk.Label(master, text="")
_Dosage = tk.Label(master, textvariable=f"{dose_value2}")
_Species = tk.Label(master, text="")
_MGperKG = tk.Label(master, text="")
_Unit = tk.Label(master, text="")
_Route = tk.Label(master, text="")
_Frequency = tk.Label(master, text="")
_Duration = tk.Label(master, text="")
_Used_For = tk.Label(master, text="")

 = tk.Label(master, text="")
_Dosage = tk.Label(master, textvariable=f"{dose_value2}")
_Species = tk.Label(master, text="")
_MGperKG = tk.Label(master, text="")
_Unit = tk.Label(master, text="")
_Route = tk.Label(master, text="")
_Frequency = tk.Label(master, text="")
_Duration = tk.Label(master, text="")
_Used_For = tk.Label(master, text="")

 = tk.Label(master, text="")
_Dosage = tk.Label(master, textvariable=f"{dose_value2}")
_Species = tk.Label(master, text="")
_MGperKG = tk.Label(master, text="")
_Unit = tk.Label(master, text="")
_Route = tk.Label(master, text="")
_Frequency = tk.Label(master, text="")
_Duration = tk.Label(master, text="")
_Used_For = tk.Label(master, text="")

 = tk.Label(master, text="")
_Dosage = tk.Label(master, textvariable=f"{dose_value2}")
_Species = tk.Label(master, text="")
_MGperKG = tk.Label(master, text="")
_Unit = tk.Label(master, text="")
_Route = tk.Label(master, text="")
_Frequency = tk.Label(master, text="")
_Duration = tk.Label(master, text="")
_Used_For = tk.Label(master, text="")

 = tk.Label(master, text="")
_Dosage = tk.Label(master, textvariable=f"{dose_value2}")
_Species = tk.Label(master, text="")
_MGperKG = tk.Label(master, text="")
_Unit = tk.Label(master, text="")
_Route = tk.Label(master, text="")
_Frequency = tk.Label(master, text="")
_Duration = tk.Label(master, text="")
_Used_For = tk.Label(master, text="")

 = tk.Label(master, text="")
_Dosage = tk.Label(master, textvariable=f"{dose_value2}")
_Species = tk.Label(master, text="")
_MGperKG = tk.Label(master, text="")
_Unit = tk.Label(master, text="")
_Route = tk.Label(master, text="")
_Frequency = tk.Label(master, text="")
_Duration = tk.Label(master, text="")
_Used_For = tk.Label(master, text="")

 = tk.Label(master, text="")
_Dosage = tk.Label(master, textvariable=f"{dose_value2}")
_Species = tk.Label(master, text="")
_MGperKG = tk.Label(master, text="")
_Unit = tk.Label(master, text="")
_Route = tk.Label(master, text="")
_Frequency = tk.Label(master, text="")
_Duration = tk.Label(master, text="")
_Used_For = tk.Label(master, text="")

 = tk.Label(master, text="")
_Dosage = tk.Label(master, textvariable=f"{dose_value2}")
_Species = tk.Label(master, text="")
_MGperKG = tk.Label(master, text="")
_Unit = tk.Label(master, text="")
_Route = tk.Label(master, text="")
_Frequency = tk.Label(master, text="")
_Duration = tk.Label(master, text="")
_Used_For = tk.Label(master, text="")

 = tk.Label(master, text="")
_Dosage = tk.Label(master, textvariable=f"{dose_value2}")
_Species = tk.Label(master, text="")
_MGperKG = tk.Label(master, text="")
_Unit = tk.Label(master, text="")
_Route = tk.Label(master, text="")
_Frequency = tk.Label(master, text="")
_Duration = tk.Label(master, text="")
_Used_For = tk.Label(master, text="")

 = tk.Label(master, text="")
_Dosage = tk.Label(master, textvariable=f"{dose_value2}")
_Species = tk.Label(master, text="")
_MGperKG = tk.Label(master, text="")
_Unit = tk.Label(master, text="")
_Route = tk.Label(master, text="")
_Frequency = tk.Label(master, text="")
_Duration = tk.Label(master, text="")
_Used_For = tk.Label(master, text="")



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

GM_Label.grid(row=1, column=0)
Dosage.grid(row=1, column=1)
Species.grid(row=1, column=2)
MGperKG.grid(row=1, column=3)
Unit.grid(row=1, column=4)
Route.grid(row=1, column=5)
Frequency.grid(row=1, column=6)
Duration.grid(row=1, column=7)
Used_For.grid(row=1, column=8)

Activyl_Plus.grid(row=2, column=0)
Activyl_Plus_Dosage.grid(row=2, column=1)
Activyl_Species.grid(row=2, column=2)
Activyl_MGperKG.grid(row=2, column=3)
Activyl_Unit.grid(row=2, column=4)
Activyl_Route.grid(row=2, column=5)
Activyl_Frequency.grid(row=2, column=6)
Activyl_Duration.grid(row=2, column=7)
Activyl_Used_For.grid(row=2, column=8)

#m3.grid(row=3, column=0)
#a3.grid(row=3, column=1)

Albon_50mg_1.grid(row=3, column=0)
Albon_50mg_1_Dosage.grid(row=3, column=1)
Albon_50mg_1_Species.grid(row=3, column=2)
Albon_50mg_1_MGperKG.grid(row=3, column=3)
Albon_50mg_1_Unit.grid(row=3, column=4)
Albon_50mg_1_Route.grid(row=3, column=5)
Albon_50mg_1_Frequency.grid(row=3, column=6)
Albon_50mg_1_Duration.grid(row=3, column=7)
Albon_50mg_1_Used_For.grid(row=3, column=8)

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
