import tkinter as tk
import tkinter.font as font
from tkinter import ttk
from tkinter import *

try:
    from ctypes import windll
    windll.shcore.SetProcessDpiAwareness(1)
except:
    pass


# Create the master object

master = tk.Tk()
master.title("VetHelper3000")
master.geometry("")

# Weight & Calculate Button Frame

WC = Frame(master)

# Medicine Frame
Frame = Frame(master)

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

tk.Label(WC, text="Weight in kg: ").grid(row=0, column=0)

# Amount entry

e1 = tk.Entry(WC, textvariable=weight_value).grid(row=0, column=1)

# Calc Button

calc_button = ttk.Button(WC,
                         text="Calculate",
                         command=lambda:[calculate_med1(),
                                         calculate_med2(),
                                         calculate_med3()]
).grid(row=0, column=2, padx=10)

# Medicine and Amount widgets

GM_Label = tk.Label(Frame, text=" | General Medications | ").grid(row=2, column=0)
Dosage = tk.Label(Frame, text="Dosage | ").grid(row=2, column=1)
Species = tk.Label(Frame, text="Species | ").grid(row=2, column=2)
MGperKG = tk.Label(Frame, text="mg/kg | ").grid(row=2, column=3)
Unit = tk.Label(Frame, text="Unit | ").grid(row=2, column=4)
Route = tk.Label(Frame, text="Route | ").grid(row=2, column=5)
Frequency = tk.Label(Frame, text="Frequency | ").grid(row=2, column=6)
Duration = tk.Label(Frame, text="Duration | ").grid(row=2, column=7)
Used_For = tk.Label(Frame, text="Used for | ").grid(row=2, column=8)

Activyl_Plus = tk.Label(Frame, text="Activyl Plus (dogs only, 8+ Weeks)").grid(row=3, column=0)
Activyl_Plus_Dosage = tk.Label(Frame, textvariable=f"{dose_value2}").grid(row=3, column=1)
Activyl_Species = tk.Label(Frame, text="Dogs").grid(row=3, column=2)
Activyl_MGperKG = tk.Label(Frame, text="").grid(row=3, column=3)
Activyl_Unit = tk.Label(Frame, text="").grid(row=3, column=4)
Activyl_Route = tk.Label(Frame, text="Tropical").grid(row=3, column=5)
Activyl_Frequency = tk.Label(Frame, text="SID").grid(row=3, column=6)
Activyl_Duration = tk.Label(Frame, text="Once a month").grid(row=3, column=7)
Activyl_Used_For = tk.Label(Frame, text="Flea & Tick Preventative").grid(row=3, column=8)

Albon_50mg_1 = tk.Label(Frame, text="Albon (50mg/ml) Day 1").grid(row=4, column=0)
Albon_50mg_1_Dosage = tk.Label(Frame, textvariable=f"{dose_value3}").grid(row=4, column=1)
Albon_50mg_1_Species = tk.Label(Frame, text="").grid(row=4, column=2)
Albon_50mg_1_MGperKG = tk.Label(Frame, text="55").grid(row=4, column=3)
Albon_50mg_1_Unit = tk.Label(Frame, text="ml").grid(row=4, column=4)
Albon_50mg_1_Route = tk.Label(Frame, text="PO").grid(row=4, column=5)
Albon_50mg_1_Frequency = tk.Label(Frame, text="SID").grid(row=4, column=6)
Albon_50mg_1_Duration = tk.Label(Frame, text="Day 1").grid(row=4, column=7)
Albon_50mg_1_Used_For = tk.Label(Frame, text="Second option for Coccidia").grid(row=4, column=8)

Albon_50mg_2_10 = tk.Label(Frame, text="Albon (50mg/ml) Days 2-10").grid(row=5, column=0)
Albon_50mg_2_10_Dosage = tk.Label(Frame, textvariable=f"{dose_value3}").grid(row=5, column=1)
Albon_50mg_2_10_Species = tk.Label(Frame, text="").grid(row=5, column=2)
Albon_50mg_2_10_MGperKG = tk.Label(Frame, text="27.5").grid(row=5, column=3)
Albon_50mg_2_10_Unit = tk.Label(Frame, text="ml").grid(row=5, column=4)
Albon_50mg_2_10_Route = tk.Label(Frame, text="PO").grid(row=5, column=5)
Albon_50mg_2_10_Frequency = tk.Label(Frame, text="SID").grid(row=5, column=6)
Albon_50mg_2_10_Duration = tk.Label(Frame, text="Days 2-10").grid(row=5, column=7)
Albon_50mg_2_10_Used_For = tk.Label(Frame, text="2nd option for Coccidia").grid(row=5, column=8)

Albon_500mg_1 = tk.Label(Frame, text="Albon (500mg tablets) Day 1").grid(row=6, column=0)
Albon_500mg_1_Dosage = tk.Label(Frame, textvariable=f"{dose_value3}").grid(row=6, column=1)
Albon_500mg_1_Species = tk.Label(Frame, text="").grid(row=6, column=2)
Albon_500mg_1_MGperKG = tk.Label(Frame, text="55").grid(row=6, column=3)
Albon_500mg_1_Unit = tk.Label(Frame, text="mg").grid(row=6, column=4)
Albon_500mg_1_Route = tk.Label(Frame, text="PO").grid(row=6, column=5)
Albon_500mg_1_Frequency = tk.Label(Frame, text="SID").grid(row=6, column=6)
Albon_500mg_1_Duration = tk.Label(Frame, text="Day 1").grid(row=6, column=7)
Albon_500mg_1_Used_For = tk.Label(Frame, text="Second option for Coccidia").grid(row=6, column=8)

Albon_500mg_2_10 = tk.Label(Frame, text="Albon (500mg tablets) Days 2-10").grid(row=7, column=0)
Albon_500mg_2_10_Dosage = tk.Label(Frame, textvariable=f"{dose_value3}").grid(row=7, column=1)
Albon_500mg_2_10_Species = tk.Label(Frame, text="").grid(row=7, column=2)
Albon_500mg_2_10_MGperKG = tk.Label(Frame, text="28").grid(row=7, column=3)
Albon_500mg_2_10_Unit = tk.Label(Frame, text="mg").grid(row=7, column=4)
Albon_500mg_2_10_Route = tk.Label(Frame, text="PO").grid(row=7, column=5)
Albon_500mg_2_10_Frequency = tk.Label(Frame, text="SID").grid(row=7, column=6)
Albon_500mg_2_10_Duration = tk.Label(Frame, text="Days 2-10").grid(row=7, column=7)
Albon_500mg_2_10_Used_For = tk.Label(Frame, text="2nd option for Coccidia").grid(row=7, column=8)

Amoxicillin_under7LB = tk.Label(Frame, text="Amoxicillin (50 mg/ml) 7 lbs and under").grid(row=8, column=0)
Amoxicillin_under7LB_Dosage = tk.Label(Frame, textvariable=f"{dose_value2}").grid(row=8, column=1)
Amoxicillin_under7LB_Species = tk.Label(Frame, text="cats/dogs").grid(row=8, column=2)
Amoxicillin_under7LB_MGperKG = tk.Label(Frame, text="11").grid(row=8, column=3)
Amoxicillin_under7LB_Unit = tk.Label(Frame, text="ml").grid(row=8, column=4)
Amoxicillin_under7LB_Route = tk.Label(Frame, text="PO").grid(row=8, column=5)
Amoxicillin_under7LB_Frequency = tk.Label(Frame, text="BID").grid(row=8, column=6)
Amoxicillin_under7LB_Duration = tk.Label(Frame, text="10 Days").grid(row=8, column=7)
Amoxicillin_under7LB_Used_For = tk.Label(Frame, text="Antibiotic").grid(row=8, column=8)

Amoxicillin_over7LB = tk.Label(Frame, text="Amoxicillin (100, 250, 500 mg tablets) over 7 lbs").grid(row=9, column=0)
Amoxicillin_over7LB_Dosage = tk.Label(Frame, textvariable=f"{dose_value2}").grid(row=9, column=1)
Amoxicillin_over7LB_Species = tk.Label(Frame, text="cats/dogs").grid(row=9, column=2)
Amoxicillin_over7LB_MGperKG = tk.Label(Frame, text="11").grid(row=9, column=3)
Amoxicillin_over7LB_Unit = tk.Label(Frame, text="mg").grid(row=9, column=4)
Amoxicillin_over7LB_Route = tk.Label(Frame, text="PO").grid(row=9, column=5)
Amoxicillin_over7LB_Frequency = tk.Label(Frame, text="BID").grid(row=9, column=6)
Amoxicillin_over7LB_Duration = tk.Label(Frame, text="10 Days").grid(row=9, column=7)
Amoxicillin_over7LB_Used_For = tk.Label(Frame, text="Antibiotic").grid(row=9, column=8)

Azithromycin = tk.Label(Frame, text="Azithromycin (40 mg/ml)").grid(row=10, column=0)
Azithromycin_Dosage = tk.Label(Frame, textvariable=f"{dose_value2}").grid(row=10, column=1)
Azithromycin_Species = tk.Label(Frame, text="").grid(row=10, column=2)
Azithromycin_MGperKG = tk.Label(Frame, text="5").grid(row=10, column=3)
Azithromycin_Unit = tk.Label(Frame, text="ml").grid(row=10, column=4)
Azithromycin_Route = tk.Label(Frame, text="PO").grid(row=10, column=5)
Azithromycin_Frequency = tk.Label(Frame, text="SID").grid(row=10, column=6)
Azithromycin_Duration = tk.Label(Frame, text="10 Days").grid(row=10, column=7)
Azithromycin_Used_For = tk.Label(Frame, text="URI (feline) - second choice; round up").grid(row=10, column=8)

Baytril_tablets = tk.Label(Frame, text="Baytril (tablets)").grid(row=11, column=0)
Baytril_tablets_Dosage = tk.Label(Frame, textvariable=f"{dose_value2}").grid(row=11, column=1)
Baytril_tablets_Species = tk.Label(Frame, text="dogs").grid(row=11, column=2)
Baytril_tablets_MGperKG = tk.Label(Frame, text="10").grid(row=11, column=3)
Baytril_tablets_Unit = tk.Label(Frame, text="mg").grid(row=11, column=4)
Baytril_tablets_Route = tk.Label(Frame, text="PO").grid(row=11, column=5)
Baytril_tablets_Frequency = tk.Label(Frame, text="SID").grid(row=11, column=6)
Baytril_tablets_Duration = tk.Label(Frame, text="As directed by DVM").grid(row=11, column=7)
Baytril_tablets_Used_For = tk.Label(Frame, text="Antibiotic, uses only if directed by DVM").grid(row=11, column=8)

Baytril_22point7 = tk.Label(Frame, text="Baytril (22.7 mg/ml)").grid(row=12, column=0)
Baytril_22point7_Dosage = tk.Label(Frame, textvariable=f"{dose_value2}").grid(row=12, column=1)
Baytril_22point7_Species = tk.Label(Frame, text="dogs").grid(row=12, column=2)
Baytril_22point7_MGperKG = tk.Label(Frame, text="5").grid(row=12, column=3)
Baytril_22point7_Unit = tk.Label(Frame, text="ml").grid(row=12, column=4)
Baytril_22point7_Route = tk.Label(Frame, text="IM").grid(row=12, column=5)
Baytril_22point7_Frequency = tk.Label(Frame, text="SID").grid(row=12, column=6)
Baytril_22point7_Duration = tk.Label(Frame, text="As directed by DVM").grid(row=12, column=7)
Baytril_22point7_Used_For = tk.Label(Frame, text="Antibiotic, use only if directed by DVM").grid(row=12, column=8)

Baytril_100 = tk.Label(Frame, text="Baytril 100mg").grid(row=13, column=0)
Baytril_100_Dosage = tk.Label(Frame, textvariable=f"{dose_value2}").grid(row=13, column=1)
Baytril_100_Species = tk.Label(Frame, text="cats").grid(row=13, column=2)
Baytril_100_MGperKG = tk.Label(Frame, text="5").grid(row=13, column=3)
Baytril_100_Unit = tk.Label(Frame, text="ml").grid(row=13, column=4)
Baytril_100_Route = tk.Label(Frame, text="IM").grid(row=13, column=5)
Baytril_100_Frequency = tk.Label(Frame, text="SID").grid(row=13, column=6)
Baytril_100_Duration = tk.Label(Frame, text="5 days").grid(row=13, column=7)
Baytril_100_Used_For = tk.Label(Frame, text="Antibiotic for severe URI if intolerant of oral meds; round down").grid(row=13, column=8)

Cephalexin_250_500mg_tablets = tk.Label(Frame, text="Cephalexin_250_500mg_tablets").grid(row=14, column=0)
Cephalexin_250_500mg_tablets_Dosage = tk.Label(Frame, textvariable=f"{dose_value2}").grid(row=14, column=1)
Cephalexin_250_500mg_tablet_Species = tk.Label(Frame, text="dogs").grid(row=14, column=2)
Cephalexin_250_500mg_tablets_MGperKG = tk.Label(Frame, text="22").grid(row=14, column=3)
Cephalexin_250_500mg_tablets_Unit = tk.Label(Frame, text="mg").grid(row=14, column=4)
Cephalexin_250_500mg_tablets_Route = tk.Label(Frame, text="PO").grid(row=14, column=5)
Cephalexin_250_500mg_tablets_Frequency = tk.Label(Frame, text="BID").grid(row=14, column=6)
Cephalexin_250_500mg_tablets_Duration = tk.Label(Frame, text="14 days").grid(row=14, column=7)
Cephalexin_250_500mg_tablets_Used_For = tk.Label(Frame, text="Skin - pyoderma in dogs").grid(row=14, column=8)

Cerenia_10mg = tk.Label(Frame, text="Cerenia (10 mg/ml)").grid(row=15, column=0)
Cerenia_10mg_Dosage = tk.Label(Frame, textvariable=f"{dose_value2}").grid(row=15, column=1)
Cerenia_10mg_Species = tk.Label(Frame, text="cats/dogs").grid(row=15, column=2)
Cerenia_10mg_MGperKG = tk.Label(Frame, text="1").grid(row=15, column=3)
Cerenia_10mg_Unit = tk.Label(Frame, text="ml").grid(row=15, column=4)
Cerenia_10mg_Route = tk.Label(Frame, text="SQ").grid(row=15, column=5)
Cerenia_10mg_Frequency = tk.Label(Frame, text="SID").grid(row=15, column=6)
Cerenia_10mg_Duration = tk.Label(Frame, text="up to 5 days").grid(row=15, column=7)
Cerenia_10mg_Used_For = tk.Label(Frame, text="Nausea; quick dosing - 0.1 ml/kg").grid(row=15, column=8)

Clindamycin_75_150mg = tk.Label(Frame, text="Clindamycin (75, 150 mg tablets)").grid(row=16, column=0)
Clindamycin_75_150mg_tablets_Dosage = tk.Label(Frame, textvariable=f"{dose_value2}").grid(row=16, column=1)
Clindamycin_75_150mg_tablets_Species = tk.Label(Frame, text="dogs").grid(row=16, column=2)
Clindamycin_75_150mg_tablets_MGperKG = tk.Label(Frame, text="11").grid(row=16, column=3)
Clindamycin_75_150mg_tablets_Unit = tk.Label(Frame, text="mg").grid(row=16, column=4)
Clindamycin_75_150mg_tablets_Route = tk.Label(Frame, text="PO").grid(row=16, column=5)
Clindamycin_75_150mg_tablets_Frequency = tk.Label(Frame, text="BID").grid(row=16, column=6)
Clindamycin_75_150mg_tablets_Duration = tk.Label(Frame, text="10 days").grid(row=16, column=7)
Clindamycin_75_150mg_tablets_Used_For = tk.Label(Frame, text="Antibiotic; round up").grid(row=16, column=8)

Clindamycin_25 = tk.Label(Frame, text="Clindamycin (25 mg/ml) ").grid(row=17, column=0)
Clindamycin_25_Dosage = tk.Label(Frame, textvariable=f"{dose_value2}").grid(row=17, column=1)
Clindamycin_25_Species = tk.Label(Frame, text="cats").grid(row=17, column=2)
Clindamycin_25_MGperKG = tk.Label(Frame, text="11").grid(row=17, column=3)
Clindamycin_25_Unit = tk.Label(Frame, text="ml").grid(row=17, column=4)
Clindamycin_25_Route = tk.Label(Frame, text="PO").grid(row=17, column=5)
Clindamycin_25_Frequency = tk.Label(Frame, text="SID").grid(row=17, column=6)
Clindamycin_25_Duration = tk.Label(Frame, text="10-14 days").grid(row=17, column=7)
Clindamycin_25_Used_For = tk.Label(Frame, text="Antibiotic (Round up)").grid(row=17, column=8)

Clavamox_under7lbs = tk.Label(Frame, text="Clavamox (62.5 mg/ml) 7 lbs and under").grid(row=18, column=0)
Clavamox_under7lbs_Dosage = tk.Label(Frame, textvariable=f"{dose_value2}").grid(row=18, column=1)
Clavamox_under7lbs_Species = tk.Label(Frame, text="cats/dogs").grid(row=18, column=2)
Clavamox_under7lbs_MGperKG = tk.Label(Frame, text="13.75").grid(row=18, column=3)
Clavamox_under7lbs_Unit = tk.Label(Frame, text="ml").grid(row=18, column=4)
Clavamox_under7lbs_Route = tk.Label(Frame, text="PO").grid(row=18, column=5)
Clavamox_under7lbs_Frequency = tk.Label(Frame, text="BID").grid(row=18, column=6)
Clavamox_under7lbs_Duration = tk.Label(Frame, text="10 days").grid(row=18, column=7)
Clavamox_under7lbs_Used_For = tk.Label(Frame, text="Antibiotic").grid(row=18, column=8)

Clavamox_over7lbs = tk.Label(Frame, text="Clavamox (62.5, 125, 250, 375 mg tablets) over 7 lbs").grid(row=19, column=0)
Clavamox_over7lbs_Dosage = tk.Label(Frame, textvariable=f"{dose_value2}").grid(row=19, column=1)
Clavamox_over7lbs_Species = tk.Label(Frame, text="cats/dogs").grid(row=19, column=2)
Clavamox_over7lbs_MGperKG = tk.Label(Frame, text="13.75").grid(row=19, column=3)
Clavamox_over7lbs_Unit = tk.Label(Frame, text="mg").grid(row=19, column=4)
Clavamox_over7lbs_Route = tk.Label(Frame, text="PO").grid(row=19, column=5)
Clavamox_over7lbs_Frequency = tk.Label(Frame, text="BID").grid(row=19, column=6)
Clavamox_over7lbs_Duration = tk.Label(Frame, text="10 days").grid(row=19, column=7)
Clavamox_over7lbs_Used_For = tk.Label(Frame, text="Antibiotic").grid(row=19, column=8)

Convenia_80 = tk.Label(Frame, text="Convenia (80 mg/ml)").grid(row=20, column=0)
Convenia_80_Dosage = tk.Label(Frame, textvariable=f"{dose_value2}").grid(row=20, column=1)
Convenia_80_Species = tk.Label(Frame, text="cats/dogs").grid(row=20, column=2)
Convenia_80_MGperKG = tk.Label(Frame, text="8").grid(row=20, column=3)
Convenia_80_Unit = tk.Label(Frame, text="ml").grid(row=20, column=4)
Convenia_80_Route = tk.Label(Frame, text="SQ").grid(row=20, column=5)
Convenia_80_Frequency = tk.Label(Frame, text="Once").grid(row=20, column=6)
Convenia_80_Duration = tk.Label(Frame, text="Once").grid(row=20, column=7)
Convenia_80_Used_For = tk.Label(Frame, text="Antibiotic; quick dosing - 0.1 ml/kg").grid(row=20, column=8)

Doxycycline_50 = tk.Label(Frame, text="Doxycycline (50 mg/ml)").grid(row=21, column=0)
Doxycycline_50_Dosage = tk.Label(Frame, textvariable=f"{dose_value2}").grid(row=21, column=1)
Doxycycline_50_Species = tk.Label(Frame, text="cats").grid(row=21, column=2)
Doxycycline_50_MGperKG = tk.Label(Frame, text="10").grid(row=21, column=3)
Doxycycline_50_Unit = tk.Label(Frame, text="ml").grid(row=21, column=4)
Doxycycline_50_Route = tk.Label(Frame, text="PO").grid(row=21, column=5)
Doxycycline_50_Frequency = tk.Label(Frame, text="SID").grid(row=21, column=6)
Doxycycline_50_Duration = tk.Label(Frame, text="10 days").grid(row=21, column=7)
Doxycycline_50_Used_For = tk.Label(Frame, text="URI (primarily feline, can be used in small puppies)").grid(row=21, column=8)

Doxycycline_100mg_tablets = tk.Label(Frame, text="Doxycycline (100 mg tablets)").grid(row=22, column=0)
Doxycycline_100mg_tablets_Dosage = tk.Label(Frame, textvariable=f"{dose_value2}").grid(row=22, column=1)
Doxycycline_100mg_tablets_Species = tk.Label(Frame, text="dogs").grid(row=22, column=2)
Doxycycline_100mg_tablets_MGperKG = tk.Label(Frame, text="10").grid(row=22, column=3)
Doxycycline_100mg_tablets_Unit = tk.Label(Frame, text="mg").grid(row=22, column=4)
Doxycycline_100mg_tablets_Route = tk.Label(Frame, text="PO").grid(row=22, column=5)
Doxycycline_100mg_tablets_Frequency = tk.Label(Frame, text="SID").grid(row=22, column=6)
Doxycycline_100mg_tablets_Duration = tk.Label(Frame, text="10 days ").grid(row=22, column=7)
Doxycycline_100mg_tablets_Used_For = tk.Label(Frame, text="Kennel Cough").grid(row=22, column=8)

Entyce_cats = tk.Label(Frame, text="Entyce (30 mg/ml) - CATS").grid(row=23, column=0)
Entyce_cats_Dosage = tk.Label(Frame, textvariable=f"{dose_value2}").grid(row=23, column=1)
Entyce_cats_Species = tk.Label(Frame, text="cats").grid(row=23, column=2)
Entyce_cats_MGperKG = tk.Label(Frame, text="2").grid(row=23, column=3)
Entyce_cats_Unit = tk.Label(Frame, text="ml").grid(row=23, column=4)
Entyce_cats_Route = tk.Label(Frame, text="PO").grid(row=23, column=5)
Entyce_cats_Frequency = tk.Label(Frame, text="SID").grid(row=23, column=6)
Entyce_cats_Duration = tk.Label(Frame, text="2-3 days to start, ask a vet").grid(row=23, column=7)
Entyce_cats_Used_For = tk.Label(Frame, text="Anorexia").grid(row=23, column=8)

Entyce_dogs = tk.Label(Frame, text="Entyce (30 mg/ml) - DOGS").grid(row=24, column=0)
Entyce_dogs_Dosage = tk.Label(Frame, textvariable=f"{dose_value2}").grid(row=24, column=1)
Entyce_dogs_Species = tk.Label(Frame, text="dogs").grid(row=24, column=2)
Entyce_dogs_MGperKG = tk.Label(Frame, text="3").grid(row=24, column=3)
Entyce_dogs_Unit = tk.Label(Frame, text="ml").grid(row=24, column=4)
Entyce_dogs_Route = tk.Label(Frame, text="PO").grid(row=24, column=5)
Entyce_dogs_Frequency = tk.Label(Frame, text="SID").grid(row=24, column=6)
Entyce_dogs_Duration = tk.Label(Frame, text="2-3 days to start, ask a vet").grid(row=24, column=7)
Entyce_dogs_Used_For = tk.Label(Frame, text="Anorexia").grid(row=24, column=8)

Famciclovir_250mg = tk.Label(Frame, text="Famciclovir (250 mg tablets)").grid(row=25, column=0)
Famciclovir_250mg_Dosage = tk.Label(Frame, textvariable=f"{dose_value2}").grid(row=25, column=1)
Famciclovir_250mg_Species = tk.Label(Frame, text="cats").grid(row=25, column=2)
Famciclovir_250mg_MGperKG = tk.Label(Frame, text="40").grid(row=25, column=3)
Famciclovir_250mg_Unit = tk.Label(Frame, text="mg").grid(row=25, column=4)
Famciclovir_250mg_Route = tk.Label(Frame, text="PO").grid(row=25, column=5)
Famciclovir_250mg_Frequency = tk.Label(Frame, text="BID").grid(row=25, column=6)
Famciclovir_250mg_Duration = tk.Label(Frame, text="5 days").grid(row=25, column=7)
Famciclovir_250mg_Used_For = tk.Label(Frame, text="Feline URI (only to be Rx by Vet)").grid(row=25, column=8)

Frontline = tk.Label(Frame, text="Frontline - 1 drop/lb for puppies < 8 weeks and kittens <6 weeks").grid(row=26, column=0)
Frontline_Dosage = tk.Label(Frame, textvariable=f"{dose_value2}").grid(row=26, column=1)
Frontline_Species = tk.Label(Frame, text="cats/dogs").grid(row=26, column=2)
Frontline_MGperKG = tk.Label(Frame, text="").grid(row=26, column=3)
Frontline_Unit = tk.Label(Frame, text="drops").grid(row=26, column=4)
Frontline_Route = tk.Label(Frame, text="topical").grid(row=26, column=5)
Frontline_Frequency = tk.Label(Frame, text="SID").grid(row=26, column=6)
Frontline_Duration = tk.Label(Frame, text="Once a month").grid(row=26, column=7)
Frontline_Used_For = tk.Label(Frame, text="Flea preventative").grid(row=26, column=8)

Metronidazole_250_500mg_Tablets = tk.Label(Frame, text="Metronidazole (250, 500 mg tablets)").grid(row=27, column=0)
Metronidazole_250_500mg_Tablets_Dosage = tk.Label(Frame, textvariable=f"{dose_value2}").grid(row=27, column=1)
Metronidazole_250_500mg_Tablets_Species = tk.Label(Frame, text="dogs").grid(row=27, column=2)
Metronidazole_250_500mg_Tablets_MGperKG = tk.Label(Frame, text="25").grid(row=27, column=3)
Metronidazole_250_500mg_Tablets_Unit = tk.Label(Frame, text="mg").grid(row=27, column=4)
Metronidazole_250_500mg_Tablets_Route = tk.Label(Frame, text="PO").grid(row=27, column=5)
Metronidazole_250_500mg_Tablets_Frequency = tk.Label(Frame, text="BID").grid(row=27, column=6)
Metronidazole_250_500mg_Tablets_Duration = tk.Label(Frame, text="5 days").grid(row=27, column=7)
Metronidazole_250_500mg_Tablets_Used_For = tk.Label(Frame, text="Diarrhea (round down)").grid(row=27, column=8)

Metronidazole_50 = tk.Label(Frame, text="Metronidazole (50 mg/ml) - can use with small dogs, use dog dose").grid(row=28, column=0)
Metronidazole_50_Dosage = tk.Label(Frame, textvariable=f"{dose_value2}").grid(row=28, column=1)
Metronidazole_50_Species = tk.Label(Frame, text="cats").grid(row=28, column=2)
Metronidazole_50_MGperKG = tk.Label(Frame, text="10").grid(row=28, column=3)
Metronidazole_50_Unit = tk.Label(Frame, text="ml").grid(row=28, column=4)
Metronidazole_50_Route = tk.Label(Frame, text="PO").grid(row=28, column=5)
Metronidazole_50_Frequency = tk.Label(Frame, text="BID").grid(row=28, column=6)
Metronidazole_50_Duration = tk.Label(Frame, text="5 days").grid(row=28, column=7)
Metronidazole_50_Used_For = tk.Label(Frame, text="Diarrhea").grid(row=28, column=8)

Panacur_1 = tk.Label(Frame, text="Panacur (100 mg/ml) - *roundworms, hookworms, whipworms").grid(row=29, column=0)
Panacur_1_Dosage = tk.Label(Frame, textvariable=f"{dose_value2}").grid(row=29, column=1)
Panacur_1_Species = tk.Label(Frame, text="cats/dogs").grid(row=29, column=2)
Panacur_1_MGperKG = tk.Label(Frame, text="50").grid(row=29, column=3)
Panacur_1_Unit = tk.Label(Frame, text="ml").grid(row=29, column=4)
Panacur_1_Route = tk.Label(Frame, text="PO").grid(row=29, column=5)
Panacur_1_Frequency = tk.Label(Frame, text="SID").grid(row=29, column=6)
Panacur_1_Duration = tk.Label(Frame, text="3 days").grid(row=29, column=7)
Panacur_1_Used_For = tk.Label(Frame, text="Roundworms, Hookworms, Whipworms").grid(row=29, column=8)

Panacur_2 = tk.Label(Frame, text="Panacur (100 mg/ml) - *giardia").grid(row=30, column=0)
Panacur_2_Dosage = tk.Label(Frame, textvariable=f"{dose_value2}").grid(row=30, column=1)
Panacur_2_Species = tk.Label(Frame, text="cats/dogs").grid(row=30, column=2)
Panacur_2_MGperKG = tk.Label(Frame, text="50").grid(row=30, column=3)
Panacur_2_Unit = tk.Label(Frame, text="ml").grid(row=30, column=4)
Panacur_2_Route = tk.Label(Frame, text="PO").grid(row=30, column=5)
Panacur_2_Frequency = tk.Label(Frame, text="SID").grid(row=30, column=6)
Panacur_2_Duration = tk.Label(Frame, text="5 days").grid(row=30, column=7)
Panacur_2_Used_For = tk.Label(Frame, text="Giardia").grid(row=30, column=8)

Ponazuril_50 = tk.Label(Frame, text="Ponazuril (50 mg/ml) - only use for very small animals").grid(row=31, column=0)
Ponazuril_50_Dosage = tk.Label(Frame, textvariable=f"{dose_value2}").grid(row=31, column=1)
Ponazuril_50_Species = tk.Label(Frame, text="").grid(row=31, column=2)
Ponazuril_50_MGperKG = tk.Label(Frame, text="50").grid(row=31, column=3)
Ponazuril_50_Unit = tk.Label(Frame, text="ml").grid(row=31, column=4)
Ponazuril_50_Route = tk.Label(Frame, text="PO").grid(row=31, column=5)
Ponazuril_50_Frequency = tk.Label(Frame, text="SID").grid(row=31, column=6)
Ponazuril_50_Duration = tk.Label(Frame, text="3 days; repeat in 10 days").grid(row=31, column=7)
Ponazuril_50_Used_For = tk.Label(Frame, text="Coccidia").grid(row=31, column=8)

Ponazuril_150 = tk.Label(Frame, text="Ponazuril (150 mg/ml)").grid(row=32, column=0)
Ponazuril_150_Dosage = tk.Label(Frame, textvariable=f"{dose_value2}").grid(row=32, column=1)
Ponazuril_150_Species = tk.Label(Frame, text="cats/dogs").grid(row=32, column=2)
Ponazuril_150_MGperKG = tk.Label(Frame, text="50").grid(row=32, column=3)
Ponazuril_150_Unit = tk.Label(Frame, text="ml").grid(row=32, column=4)
Ponazuril_150_Route = tk.Label(Frame, text="PO").grid(row=32, column=5)
Ponazuril_150_Frequency = tk.Label(Frame, text="SID").grid(row=32, column=6)
Ponazuril_150_Duration = tk.Label(Frame, text="3 days; repeat in 10 days").grid(row=32, column=7)
Ponazuril_150_Used_For = tk.Label(Frame, text="Coccidia").grid(row=32, column=8)

Praziquantel = tk.Label(Frame, text="Praziquantel - see below").grid(row=33, column=0)
Praziquantel_Dosage = tk.Label(Frame, textvariable=f"{dose_value2}").grid(row=33, column=1)
Praziquantel_Species = tk.Label(Frame, text="cats/dogs").grid(row=33, column=2)
Praziquantel_MGperKG = tk.Label(Frame, text="").grid(row=33, column=3)
Praziquantel_Unit = tk.Label(Frame, text="").grid(row=33, column=4)
Praziquantel_Route = tk.Label(Frame, text="SQ").grid(row=33, column=5)
Praziquantel_Frequency = tk.Label(Frame, text="Once").grid(row=33, column=6)
Praziquantel_Duration = tk.Label(Frame, text="Once").grid(row=33, column=7)
Praziquantel_Used_For = tk.Label(Frame, text="Tapeworms").grid(row=33, column=8)

Pyrantel_Pamoate = tk.Label(Frame, text="Pyrantel Pamoate (50 mg/ml)").grid(row=34, column=0)
Pyrantel_Pamoate_Dosage = tk.Label(Frame, textvariable=f"{dose_value2}").grid(row=34, column=1)
Pyrantel_Pamoate_Species = tk.Label(Frame, text="cats/dogs").grid(row=34, column=2)
Pyrantel_Pamoate_mg_lb = tk.Label(Frame, text="5").grid(row=34, column=3)
Pyrantel_Pamoate_Unit = tk.Label(Frame, text="ml").grid(row=34, column=4)
Pyrantel_Pamoate_Route = tk.Label(Frame, text="PO").grid(row=34, column=5)
Pyrantel_Pamoate_Frequency = tk.Label(Frame, text="Once").grid(row=34, column=6)
Pyrantel_Pamoate_Duration = tk.Label(Frame, text="Repeat in 14 days").grid(row=34, column=7)
Pyrantel_Pamoate_Used_For = tk.Label(Frame, text="Hookworms, Roundworms").grid(row=34, column=8)

Revolution = tk.Label(Frame, text="Revolution - see below").grid(row=35, column=0)
Revolution_Dosage = tk.Label(Frame, textvariable=f"{dose_value2}").grid(row=35, column=1)
Revolution_Species = tk.Label(Frame, text="cats/dogs").grid(row=35, column=2)
Revolution_MGperKG = tk.Label(Frame, text="").grid(row=35, column=3)
Revolution_Unit = tk.Label(Frame, text="").grid(row=35, column=4)
Revolution_Route = tk.Label(Frame, text="topical").grid(row=35, column=5)
Revolution_Frequency = tk.Label(Frame, text="SID").grid(row=35, column=6)
Revolution_Duration = tk.Label(Frame, text="Once").grid(row=35, column=7)
Revolution_Used_For = tk.Label(Frame, text="Ear mites, fleas, other mites").grid(row=35, column=8)


Trazadone_Standard = tk.Label(Frame, text="Trazadone Standard Dose").grid(row=36, column=0)
Trazadone_Standard_Dosage = tk.Label(Frame, textvariable=f"{dose_value2}").grid(row=36, column=1)
Trazadone_Standard_Species = tk.Label(Frame, text="dogs").grid(row=36, column=2)
Trazadone_Standard_MGperKG = tk.Label(Frame, text="7").grid(row=36, column=3)
Trazadone_Standard_Unit = tk.Label(Frame, text="mg").grid(row=36, column=4)
Trazadone_Standard_Route = tk.Label(Frame, text="PO").grid(row=36, column=5)
Trazadone_Standard_Frequency = tk.Label(Frame, text="BID").grid(row=36, column=6)
Trazadone_Standard_Duration = tk.Label(Frame, text="14 days").grid(row=36, column=7)
Trazadone_Standard_Used_For = tk.Label(Frame, text="MUST be started and monitored by a veterinarian.\n  If used for over 4 weeks, must do a tapered withdrawl:\n decrease dose by half for 2 days, then decrease by half again for 2 days, then stop.").grid(row=36, column=8)

Trazadone_High_Dosage = tk.Label(Frame, text="Trazadone High Dose").grid(row=36, column=0)
Trazadone_High_Dosage = tk.Label(Frame, textvariable=f"{dose_value2}").grid(row=36, column=1)
Trazadone_High_Dosage_Species = tk.Label(Frame, text="dogs").grid(row=37, column=2)
Trazadone_High_Dosage_MGperKG = tk.Label(Frame, text="10").grid(row=37, column=3)
Trazadone_High_Dosage_Unit = tk.Label(Frame, text="mg").grid(row=37, column=4)
Trazadone_High_Dosage_Route = tk.Label(Frame, text="PO").grid(row=37, column=5)
Trazadone_High_Dosage_Frequency = tk.Label(Frame, text="BID-TID").grid(row=37, column=6)
Trazadone_High_Dosage_Duration = tk.Label(Frame, text="14 days").grid(row=37, column=7)
Trazadone_High_Dosage_Used_For = tk.Label(Frame, text="MUST be started and monitored by a veterinarian.\n  If used for over 4 weeks, must do a tapered withdrawl:\n decrease dose by half for 2 days, then decrease by half again for 2 days, then stop.").grid(row=36, column=8)

Pain_Medications = tk.Label(Frame, text="Pain Medications").grid(row=38, column=0)
Pain_Dosage = tk.Label(Frame, text="Dosage").grid(row=38, column=1)
Pain_Species = tk.Label(Frame, text="Species").grid(row=38, column=2)
Pain_MGperKG = tk.Label(Frame, text="mg/kg").grid(row=38, column=3)
Pain_Unit = tk.Label(Frame, text="Unit").grid(row=38, column=4)
Pain_Route = tk.Label(Frame, text="Route").grid(row=38, column=5)
Pain_Frequency = tk.Label(Frame, text="Frequency").grid(row=38, column=6)
Pain_Duration = tk.Label(Frame, text="Duration").grid(row=38, column=7)
Pain_Used_For = tk.Label(Frame, text="Used for").grid(row=38, column=8)

Carprofen_25_75_100_Tablets = tk.Label(Frame, text="Carprofen (25, 75, 100 mg tablets)").grid(row=39, column=0)
Carprofen_25_75_100_Tablets_Dosage = tk.Label(Frame, textvariable=f"{dose_value2}").grid(row=39, column=1)
Carprofen_25_75_100_Tablets_Species = tk.Label(Frame, text="dogs").grid(row=39 , column=2)
Carprofen_25_75_100_Tablets_MGperKG = tk.Label(Frame, text="4.4").grid(row=39 , column=3)
Carprofen_25_75_100_Tablets_Unit = tk.Label(Frame, text="mg").grid(row=39, column=4)
Carprofen_25_75_100_Tablets_Route = tk.Label(Frame, text="PO").grid(row=39, column=5)
Carprofen_25_75_100_Tablets_Frequency = tk.Label(Frame, text="SID").grid(row=39, column=6)
Carprofen_25_75_100_Tablets_Duration = tk.Label(Frame, text="3 days").grid(row=39, column=7)
Carprofen_25_75_100_Tablets_Used_For = tk.Label(Frame, text="").grid(row=39, column=8)

Carprofen_50 = tk.Label(Frame, text="Carprofen (50 mg/ml) (if given at time of surgery)").grid(row=39, column=0)
Carprofen_50_Dosage = tk.Label(Frame, textvariable=f"{dose_value2}").grid(row=39, column=1)
Carprofen_50_Species = tk.Label(Frame, text="").grid(row=40, column=2)
Carprofen_50_MGperKG = tk.Label(Frame, text="").grid(row=40, column=3)
Carprofen_50_Unit = tk.Label(Frame, text="").grid(row=40, column=4)
Carprofen_50_Route = tk.Label(Frame, text="").grid(row=40, column=5)
Carprofen_50_Frequency = tk.Label(Frame, text="").grid(row=40, column=6)
Carprofen_50_Duration = tk.Label(Frame, text="").grid(row=40, column=7)
Carprofen_50_Used_For = tk.Label(Frame, text="").grid(row=40, column=8)

Gabapentin = tk.Label(Frame, text="Gabapentin").grid(row=41, column=0)
Gabapentin_Dosage = tk.Label(Frame, textvariable=f"{dose_value2}").grid(row=41, column=1)
Gabapentin_Species = tk.Label(Frame, text="cats/dogs").grid(row=41, column=2)
Gabapentin_MGperKG = tk.Label(Frame, text="10").grid(row=41, column=3)
Gabapentin_Unit = tk.Label(Frame, text="mg").grid(row=41, column=4)
Gabapentin_Route = tk.Label(Frame, text="PO").grid(row=41, column=5)
Gabapentin_Frequency = tk.Label(Frame, text="BID").grid(row=41, column=6)
Gabapentin_Duration = tk.Label(Frame, text="ASK DVM").grid(row=41, column=7)
Gabapentin_Used_For = tk.Label(Frame, text="Do not use unless requested by DVM").grid(row=41, column=8)

Ketoprofen = tk.Label(Frame, text="Ketoprofen (diluted to 0.4 mg/ml)").grid(row=42, column=0)
Ketoprofen_Dosage = tk.Label(Frame, textvariable=f"{dose_value2}").grid(row=42, column=1)
Ketoprofen_Species = tk.Label(Frame, text="cats").grid(row=42, column=2)
Ketoprofen_MGperKG = tk.Label(Frame, text="1.1").grid(row=42, column=3)
Ketoprofen_Unit = tk.Label(Frame, text="ml").grid(row=42, column=4)
Ketoprofen_Route = tk.Label(Frame, text="SQ").grid(row=42, column=5)
Ketoprofen_Frequency = tk.Label(Frame, text="Once").grid(row=42, column=6)
Ketoprofen_Duration = tk.Label(Frame, text="At time of sx").grid(row=42, column=7)
Ketoprofen_Used_For = tk.Label(Frame, text="Painful when diluted in sterile water - must be fully anesthetized").grid(row=42, column=8)

Meloxicam_Loading_Cat = tk.Label(Frame, text="Meloxicam ORAL (1.5 mg/ml) (cats) - Loading dose").grid(row=43, column=0)
Meloxicam_Loading_Cat_Dosage = tk.Label(Frame, textvariable=f"{dose_value2}").grid(row=43, column=1)
Meloxicam_Loading_Cat_Species = tk.Label(Frame, text="cats").grid(row=43, column=2)
Meloxicam_Loading_Cat_MGperKG = tk.Label(Frame, text="0.1").grid(row=43, column=3)
Meloxicam_Loading_Cat_Unit = tk.Label(Frame, text="ml").grid(row=43, column=4)
Meloxicam_Loading_Cat_Route = tk.Label(Frame, text="PO").grid(row=43, column=5)
Meloxicam_Loading_Cat_Frequency = tk.Label(Frame, text="SID").grid(row=43, column=6)
Meloxicam_Loading_Cat_Duration = tk.Label(Frame, text="1st dose").grid(row=43, column=7)
Meloxicam_Loading_Cat_Used_For = tk.Label(Frame, text="Do not use unless requested by DVM").grid(row=43, column=8)

Meloxicam_Maintenance_Cat = tk.Label(Frame, text="Meloxicam ORAL (1.5 mg/ml) (cats) - Maintenance dose").grid(row=44, column=0)
Meloxicam_Maintenance_Cat_Dosage = tk.Label(Frame, textvariable=f"{dose_value2}").grid(row=44, column=1)
Meloxicam_Maintenance_Cat_Species = tk.Label(Frame, text="cats").grid(row=44, column=2)
Meloxicam_Maintenance_Cat_MGperKG = tk.Label(Frame, text="0.05").grid(row=44, column=3)
Meloxicam_Maintenance_Cat_Unit = tk.Label(Frame, text="ml").grid(row=44, column=4)
Meloxicam_Maintenance_Cat_Route = tk.Label(Frame, text="PO").grid(row=44, column=5)
Meloxicam_Maintenance_Cat_Frequency = tk.Label(Frame, text="SID").grid(row=44, column=6)
Meloxicam_Maintenance_Cat_Duration = tk.Label(Frame, text="Following doses").grid(row=44, column=7)
Meloxicam_Maintenance_Cat_Used_For = tk.Label(Frame, text="Do not use unless requested by DVM").grid(row=44, column=8)

Meloxicam_Loading_Dog_Dosage = tk.Label(Frame, text="Meloxicam ORAL (1.5 mg/ml) (dogs) - Loading dose").grid(row=45, column=0)
Meloxicam_Loading_Dog_Dosage = tk.Label(Frame, textvariable=f"{dose_value2}").grid(row=45, column=1)
Meloxicam_Loading_Dog_Species = tk.Label(Frame, text="dogs").grid(row=45, column=2)
Meloxicam_Loading_Dog_MGperKG = tk.Label(Frame, text="0.2").grid(row=45, column=3)
Meloxicam_Loading_Dog_Unit = tk.Label(Frame, text="ml").grid(row=45, column=4)
Meloxicam_Loading_Dog_Route = tk.Label(Frame, text="PO").grid(row=45, column=5)
Meloxicam_Loading_Dog_Frequency = tk.Label(Frame, text="SID").grid(row=45, column=6)
Meloxicam_Loading_Dog_Duration = tk.Label(Frame, text="1st dose").grid(row=45, column=7)
Meloxicam_Loading_Dog_Used_For = tk.Label(Frame, text="pain").grid(row=45, column=8)

Meloxicam_Maintenance_Dog_Dosage = tk.Label(Frame, text="Meloxicam ORAL (1.5 mg/ml) (dogs) - Maintenance dose").grid(row=46, column=0)
Meloxicam_Maintenance_Dog_Dosage_Dosage = tk.Label(Frame, textvariable=f"{dose_value2}").grid(row=46, column=1)
Meloxicam_Maintenance_Dog_Dosage_Species = tk.Label(Frame, text="dogs").grid(row=46, column=2)
Meloxicam_Maintenance_Dog_Dosage_MGperKG = tk.Label(Frame, text="0.1").grid(row=46, column=3)
Meloxicam_Maintenance_Dog_Dosage_Unit = tk.Label(Frame, text="ml").grid(row=46, column=4)
Meloxicam_Maintenance_Dog_Dosage_Route = tk.Label(Frame, text="PO").grid(row=46, column=5)
Meloxicam_Maintenance_Dog_Dosage_Frequency = tk.Label(Frame, text="SID").grid(row=46, column=6)
Meloxicam_Maintenance_Dog_Dosage_Duration = tk.Label(Frame, text="Following doses").grid(row=46, column=7)
Meloxicam_Maintenance_Dog_Dosage_Used_For = tk.Label(Frame, text="pain").grid(row=46, column=8)

Tramadol_Min = tk.Label(Frame, text="Tramadol (50 mg tablet) - minimum dose").grid(row=47, column=0)
Tramadol_Min_Dosage = tk.Label(Frame, textvariable=f"{dose_value2}").grid(row=47, column=1)
Tramadol_Min_Species = tk.Label(Frame, text="dogs").grid(row=47, column=2)
Tramadol_Min_MGperKG = tk.Label(Frame, text="4").grid(row=47, column=3)
Tramadol_Min_Unit = tk.Label(Frame, text="mg").grid(row=47, column=4)
Tramadol_Min_Route = tk.Label(Frame, text="PO").grid(row=47, column=5)
Tramadol_Min_Frequency = tk.Label(Frame, text="BID").grid(row=47, column=6)
Tramadol_Min_Duration = tk.Label(Frame, text="Ask DVM").grid(row=47, column=7)
Tramadol_Min_Used_For = tk.Label(Frame, text="Double to 8 mg/kg for typical dose; round up in general").grid(row=47, column=8)

Tramadol_Max = tk.Label(Frame, text="Tramadol (50 mg tablet) - maximum dose").grid(row=48, column=0)
Tramadol_Max_Dosage = tk.Label(Frame, textvariable=f"{dose_value2}").grid(row=48, column=1)
Tramadol_Max_Species = tk.Label(Frame, text="dogs").grid(row=48 , column=2)
Tramadol_Max_MGperKG = tk.Label(Frame, text="10").grid(row=48 , column=3)
Tramadol_Max_Unit = tk.Label(Frame, text="mg").grid(row=48, column=4)
Tramadol_Max_Route = tk.Label(Frame, text="PO").grid(row=48, column=5)
Tramadol_Max_Frequency = tk.Label(Frame, text="BID").grid(row=48, column=6)
Tramadol_Max_Duration = tk.Label(Frame, text="Ask DVM").grid(row=48, column=7)
Tramadol_Max_Used_For = tk.Label(Frame, text="Round down").grid(row=48, column=8)

Buprenorphine = tk.Label(Frame, text="Buprenorphine (0.3 mg/ml)").grid(row=49, column=0)
Buprenorphine_Dosage = tk.Label(Frame, textvariable=f"{dose_value2}").grid(row=49, column=1)
Buprenorphine_Species = tk.Label(Frame, text="cats/dogs").grid(row=49, column=2)
Buprenorphine_MGperKG = tk.Label(Frame, text="0.02").grid(row=49, column=3)
Buprenorphine_Unit = tk.Label(Frame, text="ml").grid(row=49, column=4)
Buprenorphine_Route = tk.Label(Frame, text="PO").grid(row=49, column=5)
Buprenorphine_Frequency = tk.Label(Frame, text="BID-TID").grid(row=49, column=6)
Buprenorphine_Duration = tk.Label(Frame, text="Ask DVM").grid(row=49, column=7)
Buprenorphine_Used_For = tk.Label(Frame, text="pain").grid(row=49, column=8)

Buprenorphine_3 = tk.Label(Frame, text="Buprenorphine SR (3 mg/ml)").grid(row=50, column=0)
Buprenorphine_3_Dosage = tk.Label(Frame, textvariable=f"{dose_value2}").grid(row=50, column=1)
Buprenorphine_3_Species = tk.Label(Frame, text="cats").grid(row=50, column=2)
Buprenorphine_3_MGperKG = tk.Label(Frame, text="0.12").grid(row=50, column=3)
Buprenorphine_3_Unit = tk.Label(Frame, text="ml").grid(row=50, column=4)
Buprenorphine_3_Route = tk.Label(Frame, text="SQ").grid(row=50, column=5)
Buprenorphine_3_Frequency = tk.Label(Frame, text="q3 days").grid(row=50, column=6)
Buprenorphine_3_Duration = tk.Label(Frame, text="Ask DVM").grid(row=50, column=7)
Buprenorphine_3_Used_For = tk.Label(Frame, text="pain").grid(row=50, column=8)

# winfo_children stands for "widget info children", and gets all the children of a widget.
for child in master.winfo_children():
    child.grid_configure(padx=10, pady=10)

# Medicine to weight ratio calculations

# Keybinds

master.bind("<Return>", calculate_med1)
master.bind("<KP_Enter>", calculate_med1)

# Scrollbars

# The mainloop
tk.mainloop()
