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

Cerenia_10mg = tk.Label(master, text="Cerenia (10 mg/ml)")
Cerenia_10mg_Dosage = tk.Label(master, textvariable=f"{dose_value2}")
Cerenia_10mg_Species = tk.Label(master, text="cats/dogs")
Cerenia_10mg_MGperKG = tk.Label(master, text="1")
Cerenia_10mg_Unit = tk.Label(master, text="ml")
Cerenia_10mg_Route = tk.Label(master, text="SQ")
Cerenia_10mg_Frequency = tk.Label(master, text="SID")
Cerenia_10mg_Duration = tk.Label(master, text="up to 5 days")
Cerenia_10mg_Used_For = tk.Label(master, text="Nausea; quick dosing - 0.1 ml/kg")

Clindamycin_75_150mg = tk.Label(master, text="Clindamycin (75, 150 mg tablets)")
Clindamycin_75_150mg_tablets_Dosage = tk.Label(master, textvariable=f"{dose_value2}")
Clindamycin_75_150mg_tablets_Species = tk.Label(master, text="dogs")
Clindamycin_75_150mg_tablets_MGperKG = tk.Label(master, text="11")
Clindamycin_75_150mg_tablets_Unit = tk.Label(master, text="mg")
Clindamycin_75_150mg_tablets_Route = tk.Label(master, text="PO")
Clindamycin_75_150mg_tablets_Frequency = tk.Label(master, text="BID")
Clindamycin_75_150mg_tablets_Duration = tk.Label(master, text="10 days")
Clindamycin_75_150mg_tablets_Used_For = tk.Label(master, text="Antibiotic; round up")

Clindamycin_25 = tk.Label(master, text="Clindamycin (25 mg/ml) ")
Clindamycin_25_Dosage = tk.Label(master, textvariable=f"{dose_value2}")
Clindamycin_25_Species = tk.Label(master, text="cats")
Clindamycin_25_MGperKG = tk.Label(master, text="11")
Clindamycin_25_Unit = tk.Label(master, text="ml")
Clindamycin_25_Route = tk.Label(master, text="PO")
Clindamycin_25_Frequency = tk.Label(master, text="SID")
Clindamycin_25_Duration = tk.Label(master, text="10-14 days")
Clindamycin_25_Used_For = tk.Label(master, text="Antibiotic (Round up)")

Clavamox_under7lbs = tk.Label(master, text="Clavamox (62.5 mg/ml) 7 lbs and under")
Clavamox_under7lbs_Dosage = tk.Label(master, textvariable=f"{dose_value2}")
Clavamox_under7lbs_Species = tk.Label(master, text="cats/dogs")
Clavamox_under7lbs_MGperKG = tk.Label(master, text="13.75")
Clavamox_under7lbs_Unit = tk.Label(master, text="ml")
Clavamox_under7lbs_Route = tk.Label(master, text="PO")
Clavamox_under7lbs_Frequency = tk.Label(master, text="BID")
Clavamox_under7lbs_Duration = tk.Label(master, text="10 days")
Clavamox_under7lbs_Used_For = tk.Label(master, text="Antibiotic")

Clavamox_over7lbs = tk.Label(master, text="Clavamox (62.5, 125, 250, 375 mg tablets) over 7 lbs")
Clavamox_over7lbs_Dosage = tk.Label(master, textvariable=f"{dose_value2}")
Clavamox_over7lbs_Species = tk.Label(master, text="cats/dogs")
Clavamox_over7lbs_MGperKG = tk.Label(master, text="13.75")
Clavamox_over7lbs_Unit = tk.Label(master, text="mg")
Clavamox_over7lbs_Route = tk.Label(master, text="PO")
Clavamox_over7lbs_Frequency = tk.Label(master, text="BID")
Clavamox_over7lbs_Duration = tk.Label(master, text="10 days")
Clavamox_over7lbs_Used_For = tk.Label(master, text="Antibiotic")

Convenia_80 = tk.Label(master, text="Convenia (80 mg/ml)")
Convenia_80_Dosage = tk.Label(master, textvariable=f"{dose_value2}")
Convenia_80_Species = tk.Label(master, text="cats/dogs")
Convenia_80_MGperKG = tk.Label(master, text="8")
Convenia_80_Unit = tk.Label(master, text="ml")
Convenia_80_Route = tk.Label(master, text="SQ")
Convenia_80_Frequency = tk.Label(master, text="Once")
Convenia_80_Duration = tk.Label(master, text="Once")
Convenia_80_Used_For = tk.Label(master, text="Antibiotic; quick dosing - 0.1 ml/kg")

Doxycycline_50 = tk.Label(master, text="Doxycycline (50 mg/ml)")
Doxycycline_50_Dosage = tk.Label(master, textvariable=f"{dose_value2}")
Doxycycline_50_Species = tk.Label(master, text="cats")
Doxycycline_50_MGperKG = tk.Label(master, text="10")
Doxycycline_50_Unit = tk.Label(master, text="ml")
Doxycycline_50_Route = tk.Label(master, text="PO")
Doxycycline_50_Frequency = tk.Label(master, text="SID")
Doxycycline_50_Duration = tk.Label(master, text="10 days")
Doxycycline_50_Used_For = tk.Label(master, text="URI (primarily feline, can be used in small puppies)")

Doxycycline_100mg_tablets = tk.Label(master, text="Doxycycline (100 mg tablets)")
Doxycycline_100mg_tablets_Dosage = tk.Label(master, textvariable=f"{dose_value2}")
Doxycycline_100mg_tablets_Species = tk.Label(master, text="dogs")
Doxycycline_100mg_tablets_MGperKG = tk.Label(master, text="10")
Doxycycline_100mg_tablets_Unit = tk.Label(master, text="mg")
Doxycycline_100mg_tablets_Route = tk.Label(master, text="PO")
Doxycycline_100mg_tablets_Frequency = tk.Label(master, text="SID")
Doxycycline_100mg_tablets_Duration = tk.Label(master, text="10 days ")
Doxycycline_100mg_tablets_Used_For = tk.Label(master, text="Kennel Cough")

Entyce_cats = tk.Label(master, text="Entyce (30 mg/ml) - CATS")
Entyce_cats_Dosage = tk.Label(master, textvariable=f"{dose_value2}")
Entyce_cats_Species = tk.Label(master, text="cats")
Entyce_cats_MGperKG = tk.Label(master, text="2")
Entyce_cats_Unit = tk.Label(master, text="ml")
Entyce_cats_Route = tk.Label(master, text="PO")
Entyce_cats_Frequency = tk.Label(master, text="SID")
Entyce_cats_Duration = tk.Label(master, text="2-3 days to start, ask a vet")
Entyce_cats_Used_For = tk.Label(master, text="Anorexia")

Entyce_dogs = tk.Label(master, text="Entyce (30 mg/ml) - DOGS")
Entyce_dogs_Dosage = tk.Label(master, textvariable=f"{dose_value2}")
Entyce_dogs_Species = tk.Label(master, text="dogs")
Entyce_dogs_MGperKG = tk.Label(master, text="3")
Entyce_dogs_Unit = tk.Label(master, text="ml")
Entyce_dogs_Route = tk.Label(master, text="PO")
Entyce_dogs_Frequency = tk.Label(master, text="SID")
Entyce_dogs_Duration = tk.Label(master, text="2-3 days to start, ask a vet")
Entyce_dogs_Used_For = tk.Label(master, text="Anorexia")

Famciclovir_250mg = tk.Label(master, text="Famciclovir (250 mg tablets)")
Famciclovir_250mg_Dosage = tk.Label(master, textvariable=f"{dose_value2}")
Famciclovir_250mg_Species = tk.Label(master, text="cats")
Famciclovir_250mg_MGperKG = tk.Label(master, text="40")
Famciclovir_250mg_Unit = tk.Label(master, text="mg")
Famciclovir_250mg_Route = tk.Label(master, text="PO")
Famciclovir_250mg_Frequency = tk.Label(master, text="BID")
Famciclovir_250mg_Duration = tk.Label(master, text="5 days")
Famciclovir_250mg_Used_For = tk.Label(master, text="Feline URI (only to be Rx by Vet)")

Frontline = tk.Label(master, text="Frontline - 1 drop/lb for puppies < 8 weeks and kittens <6 weeks")
Frontline_Dosage = tk.Label(master, textvariable=f"{dose_value2}")
Frontline_Species = tk.Label(master, text="cats/dogs")
Frontline_MGperKG = tk.Label(master, text="")
Frontline_Unit = tk.Label(master, text="drops")
Frontline_Route = tk.Label(master, text="topical")
Frontline_Frequency = tk.Label(master, text="SID")
Frontline_Duration = tk.Label(master, text="Once a month")
Frontline_Used_For = tk.Label(master, text="Flea preventative")

Metronidazole_250_500mg_Tablets = tk.Label(master, text="Metronidazole (250, 500 mg tablets)")
Metronidazole_250_500mg_Tablets_Dosage = tk.Label(master, textvariable=f"{dose_value2}")
Metronidazole_250_500mg_Tablets_Species = tk.Label(master, text="dogs")
Metronidazole_250_500mg_Tablets_MGperKG = tk.Label(master, text="25")
Metronidazole_250_500mg_Tablets_Unit = tk.Label(master, text="mg")
Metronidazole_250_500mg_Tablets_Route = tk.Label(master, text="PO")
Metronidazole_250_500mg_Tablets_Frequency = tk.Label(master, text="BID")
Metronidazole_250_500mg_Tablets_Duration = tk.Label(master, text="5 days")
Metronidazole_250_500mg_Tablets_Used_For = tk.Label(master, text="Diarrhea (round down)")

Metronidazole_50 = tk.Label(master, text="Metronidazole (50 mg/ml) - can use with small dogs, use dog dose")
Metronidazole_50_Dosage = tk.Label(master, textvariable=f"{dose_value2}")
Metronidazole_50_Species = tk.Label(master, text="cats")
Metronidazole_50_MGperKG = tk.Label(master, text="10")
Metronidazole_50_Unit = tk.Label(master, text="ml")
Metronidazole_50_Route = tk.Label(master, text="PO")
Metronidazole_50_Frequency = tk.Label(master, text="BID")
Metronidazole_50_Duration = tk.Label(master, text="5 days")
Metronidazole_50_Used_For = tk.Label(master, text="Diarrhea")

Panacur_1 = tk.Label(master, text="Panacur (100 mg/ml) - *roundworms, hookworms, whipworms")
Panacur_1_Dosage = tk.Label(master, textvariable=f"{dose_value2}")
Panacur_1_Species = tk.Label(master, text="cats/dogs")
Panacur_1_MGperKG = tk.Label(master, text="50")
Panacur_1_Unit = tk.Label(master, text="ml")
Panacur_1_Route = tk.Label(master, text="PO")
Panacur_1_Frequency = tk.Label(master, text="SID")
Panacur_1_Duration = tk.Label(master, text="3 days")
Panacur_1_Used_For = tk.Label(master, text="Roundworms, Hookworms, Whipworms")

Panacur_2 = tk.Label(master, text="Panacur (100 mg/ml) - *giardia")
Panacur_2_Dosage = tk.Label(master, textvariable=f"{dose_value2}")
Panacur_2_Species = tk.Label(master, text="cats/dogs")
Panacur_2_MGperKG = tk.Label(master, text="50")
Panacur_2_Unit = tk.Label(master, text="ml")
Panacur_2_Route = tk.Label(master, text="PO")
Panacur_2_Frequency = tk.Label(master, text="SID")
Panacur_2_Duration = tk.Label(master, text="5 days")
Panacur_2_Used_For = tk.Label(master, text="Giardia")

Ponazuril_50 = tk.Label(master, text="Ponazuril (50 mg/ml) - only use for very small animals")
Ponazuril_50_Dosage = tk.Label(master, textvariable=f"{dose_value2}")
Ponazuril_50_Species = tk.Label(master, text="")
Ponazuril_50_MGperKG = tk.Label(master, text="50")
Ponazuril_50_Unit = tk.Label(master, text="ml")
Ponazuril_50_Route = tk.Label(master, text="PO")
Ponazuril_50_Frequency = tk.Label(master, text="SID")
Ponazuril_50_Duration = tk.Label(master, text="3 days; repeat in 10 days")
Ponazuril_50_Used_For = tk.Label(master, text="Coccidia")

Ponazuril_150 = tk.Label(master, text="Ponazuril (150 mg/ml)")
Ponazuril_150_Dosage = tk.Label(master, textvariable=f"{dose_value2}")
Ponazuril_150_Species = tk.Label(master, text="cats/dogs")
Ponazuril_150_MGperKG = tk.Label(master, text="50")
Ponazuril_150_Unit = tk.Label(master, text="ml")
Ponazuril_150_Route = tk.Label(master, text="PO")
Ponazuril_150_Frequency = tk.Label(master, text="SID")
Ponazuril_150_Duration = tk.Label(master, text="3 days; repeat in 10 days")
Ponazuril_150_Used_For = tk.Label(master, text="Coccidia")

Praziquantel = tk.Label(master, text="Praziquantel - see below")
Praziquantel_Dosage = tk.Label(master, textvariable=f"{dose_value2}")
Praziquantel_Species = tk.Label(master, text="cats/dogs")
Praziquantel_MGperKG = tk.Label(master, text="")
Praziquantel_Unit = tk.Label(master, text="")
Praziquantel_Route = tk.Label(master, text="SQ")
Praziquantel_Frequency = tk.Label(master, text="Once")
Praziquantel_Duration = tk.Label(master, text="Once")
Praziquantel_Used_For = tk.Label(master, text="Tapeworms")

Pyrantel_Pamoate = tk.Label(master, text="Pyrantel Pamoate (50 mg/ml)")
Pyrantel_Pamoate_Dosage = tk.Label(master, textvariable=f"{dose_value2}")
Pyrantel_Pamoate_Species = tk.Label(master, text="cats/dogs")
Pyrantel_Pamoate_mg_lb = tk.Label(master, text="5")
Pyrantel_Pamoate_Unit = tk.Label(master, text="ml")
Pyrantel_Pamoate_Route = tk.Label(master, text="PO")
Pyrantel_Pamoate_Frequency = tk.Label(master, text="Once")
Pyrantel_Pamoate_Duration = tk.Label(master, text="Repeat in 14 days")
Pyrantel_Pamoate_Used_For = tk.Label(master, text="Hookworms, Roundworms")

Revolution = tk.Label(master, text="Revolution - see below")
Revolution_Dosage = tk.Label(master, textvariable=f"{dose_value2}")
Revolution_Species = tk.Label(master, text="cats/dogs")
Revolution_MGperKG = tk.Label(master, text="")
Revolution_Unit = tk.Label(master, text="")
Revolution_Route = tk.Label(master, text="topical")
Revolution_Frequency = tk.Label(master, text="SID")
Revolution_Duration = tk.Label(master, text="Once")
Revolution_Used_For = tk.Label(master, text="Ear mites, fleas, other mites")


Trazadone_Standard = tk.Label(master, text="Trazadone Standard Dose")
Trazadone_Standard_Dosage = tk.Label(master, textvariable=f"{dose_value2}")
Trazadone_Standard_Species = tk.Label(master, text="dogs")
Trazadone_Standard_MGperKG = tk.Label(master, text="7")
Trazadone_Standard_Unit = tk.Label(master, text="mg")
Trazadone_Standard_Route = tk.Label(master, text="PO")
Trazadone_Standard_Frequency = tk.Label(master, text="BID")
Trazadone_Standard_Duration = tk.Label(master, text="14 days")
Trazadone_Standard_Used_For = tk.Label(master, text="MUST be started and monitored by a veterinarian.  If used for over 4 weeks, must do a tapered withdrawl: decrease dose by half for 2 days, then decrease by half again for 2 days, then stop.")

Trazadone_High_Dosage = tk.Label(master, text="Trazadone High Dose")
Trazadone_High_Dosage = tk.Label(master, textvariable=f"{dose_value2}")
Trazadone_High_Dosage_Species = tk.Label(master, text="dogs")
Trazadone_High_Dosage_MGperKG = tk.Label(master, text="10")
Trazadone_High_Dosage_Unit = tk.Label(master, text="mg")
Trazadone_High_Dosage_Route = tk.Label(master, text="PO")
Trazadone_High_Dosage_Frequency = tk.Label(master, text="BID-TID")
Trazadone_High_Dosage_Duration = tk.Label(master, text="14 days")
Trazadone_High_Dosage_Used_For = tk.Label(master, text="MUST be started and monitored by a veterinarian.  If used for over 4 weeks, must do a tapered withdrawl: decrease dose by half for 2 days, then decrease by half again for 2 days, then stop.")

Pain_Medications = tk.Label(master, text="Pain Medications")
Pain_Dosage = tk.Label(master, text="Dosage")
Pain_Species = tk.Label(master, text="Species")
Pain_MGperKG = tk.Label(master, text="mg/kg")
Pain_Unit = tk.Label(master, text="Unit")
Pain_Route = tk.Label(master, text="Route")
Pain_Frequency = tk.Label(master, text="Frequency")
Pain_Duration = tk.Label(master, text="Duration")
Pain_Used_For = tk.Label(master, text="Used for")

Carprofen_25_75_100_Tablets = tk.Label(master, text="Carprofen (25, 75, 100 mg tablets)")
Carprofen_25_75_100_Tablets_Dosage = tk.Label(master, textvariable=f"{dose_value2}")
Carprofen_25_75_100_Tablets_Species = tk.Label(master, text="dogs")
Carprofen_25_75_100_Tablets_MGperKG = tk.Label(master, text="4.4")
Carprofen_25_75_100_Tablets_Unit = tk.Label(master, text="mg")
Carprofen_25_75_100_Tablets_Route = tk.Label(master, text="PO")
Carprofen_25_75_100_Tablets_Frequency = tk.Label(master, text="SID")
Carprofen_25_75_100_Tablets_Duration = tk.Label(master, text="3 days")
Carprofen_25_75_100_Tablets_Used_For = tk.Label(master, text="")

Carprofen_50 = tk.Label(master, text="Carprofen (50 mg/ml) (if given at time of surgery)")
Carprofen_50_Dosage = tk.Label(master, textvariable=f"{dose_value2}")
Carprofen_50_Species = tk.Label(master, text="")
Carprofen_50_MGperKG = tk.Label(master, text="")
Carprofen_50_Unit = tk.Label(master, text="")
Carprofen_50_Route = tk.Label(master, text="")
Carprofen_50_Frequency = tk.Label(master, text="")
Carprofen_50_Duration = tk.Label(master, text="")
Carprofen_50_Used_For = tk.Label(master, text="")

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
