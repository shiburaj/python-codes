"""
Problem Statement:  WAP to make a Windows App which can calculate
                    BMI (Body Mass Index) when provided with height
                    in centimeters and Weight in Kgs. Refer the
                    Image below for sample design.
                    Category	BMI range - kg/m2
                    Severe Thinness	< 16
                    Moderate Thinness	16 - 17
                    Mild Thinness	17 - 18.5
                    Normal	18.5 - 25
                    Overweight	25 - 30
                    Obese Class I	30 - 35
                    Obese Class II	35 - 40
                    Obese Class III	> 40

Author:             Prof. Shiburaj
"""
import tkinter as tk
from tkinter import StringVar


window = tk.Tk()
window.geometry("800x600")
window.title("BMI Calculator")
window.columnconfigure([0,1,2], weight=1, minsize=55)
window.rowconfigure([0,1,2], weight=1, minsize=20)
weight = StringVar()
height = StringVar()
weight.set(0)

lbl_head = tk.Label(window, text="BMI Calculator",
                            font=('Arial', 26),
                            fg="red"
                    ).grid(row=0, column=0, columnspan=3)

frm_input = tk.Frame(window, relief=tk.RAISED, borderwidth=2)\
                .grid(row=1, column=0, padx=5, pady=5)
frm_output = tk.Frame(window, relief=tk.RAISED, borderwidth=2)\
                .grid(row=1, column=1, padx=5, pady=5)


lbl_height = tk.Label(frm_input, text="Height", font=('Times', 20))\
            .grid(row=1, column=0,sticky="e", padx=30)

ent_height = tk.Spinbox(frm_input, font=('Times', 20), from_=100.0, to=250.0, textvariable=height)\
            .grid(row=1, column=1,sticky="w")
lbl_weight = tk.Label(frm_input, text="Weight", font=('Times', 20))\
            .grid(row=2, column=0,sticky="e", padx=30)
ent_weight = tk.Entry(frm_input, font=('Times', 20), textvariable=weight)\
            .grid(row=2, column=1,sticky="w")

def calculate_bmi():
    global height,weight
    h = float(height.get())/100
    w = float(weight.get())
    bmi = w / (h * h)
    lbl_bmi_txt = tk.Label(frm_output, text="BMI", fg="green", font=('Times', 23)) \
        .grid(row=1, column=2)
    lbl_bmi_val = tk.Label(frm_output, text="45.56", bg="green", fg="white", font=('Times', 33), padx=50, pady=20)
    lbl_bmi_val.grid(row=2, column=2)
    lbl_bmi_val['text'] = round(bmi, 2)
    bmi_status = tk.Label(frm_output, text=get_bmi_status(bmi), bg="orange", fg="white", font=('Times', 16), padx=20, pady=10)
    bmi_status.grid(row=3, column=2)

def get_bmi_status(bmi):
    if bmi < 16:
        return "Severe Thinness"
    elif bmi < 17:
        return "Moderate Thinness"
    elif bmi < 18.5:
        return "Mild Thinness"
    elif bmi < 25:
        return "Normal"
    elif bmi < 30:
        return "Overweight"
    elif bmi < 35:
        return "Obese Class I"
    elif bmi < 40:
        return "Obese Class II"
    else:
        return "Obese Class III"


btn_calc = tk.Button(frm_input, text="Calculate", font=('Times', 20), command=calculate_bmi, bg="#3471eb", fg="white")\
            .grid(row=4, column=1,sticky="w", pady=30)



window.mainloop()