import tkinter as tk
from tkinter import ttk
from tkinter import font
import requests


main_window = tk.Tk()
main_window.geometry("1200x800")
main_window.title("GeoIP Locator")

lbl_app_name = tk.Label(main_window, text="GeoIP Locator", font=('Times', 30), fg="blue")
lbl_app_name.pack()

frm_input = tk.LabelFrame(main_window, text="Enter IP")
frm_input.pack(padx=50, pady=20)

ip_addr = tk.StringVar()
ent_input = tk.Entry(frm_input, font=('Times', 30), textvariable=ip_addr)
ent_input.grid(row=0, column=0)

def get_geoip():

    res = requests.get('http://ip-api.com/json/'+ip_addr.get())
    data = res.json()
    lbl_country['text'] = 'Country : '+data['country']
    lbl_state['text'] = 'State : '+data['regionName']
    lbl_city['text'] = 'City : '+data['city']

btn_find = tk.Button(frm_input, font=('Times', 20), text="Find", command=get_geoip)
btn_find.grid(row=0, column=1, padx=30)

sep = ttk.Separator(main_window, orient='horizontal').pack()

lbl_country = tk.Label(main_window, text="Country : India", font=('Times', 22), fg="green")
lbl_country.pack()
lbl_state = tk.Label(main_window, text="State : MH", font=('Times', 22), fg="green")
lbl_state.pack()
lbl_city = tk.Label(main_window, text="City : MH", font=('Times', 22), fg="green")
lbl_city.pack()


main_window.mainloop()