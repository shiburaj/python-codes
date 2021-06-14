"""
Problem Statement:  WAP to make a Voting app which allows you to cast
                    your vote as well as show the results.

Given: voting.db with 4 candidates inside the candidates table.
Author:             Prof. Shiburaj
"""
import tkinter as tk
from tkinter import ttk
import sqlite3

conn = sqlite3.connect('voting.db')
cur = conn.cursor()

window = tk.Tk()
window.geometry("1200x800")
window.title("Voting App")
window.columnconfigure([0,1], weight=1)
voted = tk.IntVar(window)
#window.rowconfigure([0,1,2,3,4,5,6,7], weight=1, minsize=55)

lbl_app_name = tk.Label(window, text="Voting App", font=('Times New Roman', 30), fg='purple')
lbl_app_name.grid(row=0, column=0, columnspan=2)

def show_index():
    frm_results.grid_forget()
    frm_voting.grid_forget()
    frm_thank_you.grid_forget()
    frm_index.grid(row=1, column=0, columnspan=2, pady=180)

# Results
def show_results():
    frm_index.grid_forget()
    frm_voting.grid_forget()
    frm_thank_you.grid_forget()
    frm_results.grid(row=1, column=0, columnspan=2)

    lbl_section_name = tk.Label(frm_results, text="Results", font=('Times New Roman', 25), fg='red')
    lbl_section_name.grid(row=1, column=0, columnspan=2, pady=60)

    results = cur.execute("SELECT * FROM `candidates`")
    count = 0
    
    for row in results:
        count += 1
        cand_data = row[1]+" : "+str(row[2])
        tk.Label(frm_results, text=cand_data ,font=('Times New Roman', 22)).grid(row=2+count, column=0, columnspan=2)

    btn_back = tk.Button(frm_results, text="Back", font=('Times New Roman', 20), command=show_index)
    btn_back.grid(row=count+2+1, column=0, pady=30, columnspan=2)

# Cast Vote
def cast_vote():
    frm_index.grid_forget()
    frm_voting.grid_forget()
    frm_results.grid_forget()
    frm_thank_you.grid(row=1, column=0, columnspan=2)
    cur.execute("UPDATE candidates SET votes = votes + 1 WHERE id = "+ str(voted.get()))
    conn.commit()

    lbl_section_name = tk.Label(frm_thank_you, text="Thank you for your Vote", font=('Times New Roman', 25), fg='blue')
    lbl_section_name.grid(row=1, column=0, columnspan=2, pady=60)

    btn_back = tk.Button(frm_thank_you, text="Back", font=('Times New Roman', 20), command=show_index)
    btn_back.grid(row=2, column=0, pady=30, padx=30, columnspan=2)


# Voting
def show_voting():
    frm_index.grid_forget()
    frm_results.grid_forget()
    frm_thank_you.grid_forget()
    frm_voting.grid(row=1, column=0, columnspan=2)

    lbl_section_name = tk.Label(frm_voting, text="Cast your Vote !!!", font=('Times New Roman', 25), fg='blue')
    lbl_section_name.grid(row=1, column=0, columnspan=2, pady=60)
    cur = conn.cursor()
    results = cur.execute("SELECT * FROM candidates")
    count = 0
    
    for row in results:
        count += 1
        ttk.Radiobutton(frm_voting, text=row[1], value=row[0], variable=voted).grid(row=2+count, column=0, columnspan=2,pady=20)

    btn_vote = tk.Button(frm_voting, text="Vote", font=('Times New Roman', 20), command=cast_vote, fg="white", bg="purple", padx=30)
    btn_vote.grid(row=count+2+1, column=0, pady=30, padx=30)
    btn_back = tk.Button(frm_voting, text="Back", font=('Times New Roman', 20), command=show_index)
    btn_back.grid(row=count+2+1, column=1, pady=30, padx=30)


frm_index = tk.Frame(window)
frm_results = tk.Frame(window)
frm_results_inner = tk.Frame(window)
frm_voting = tk.Frame(window)
frm_thank_you = tk.Frame(window)
    
frm_index.grid(row=1, column=0, columnspan=2, pady=180)
btn_cast_vote = tk.Button(frm_index, text="Cast a Vote", font=('Times New Roman', 30), fg='white', bg="red", command=show_voting)
btn_cast_vote.grid(row=1, column=0, padx=30)
btn_show_results = tk.Button(frm_index, text="Show Results", font=('Times New Roman', 30), fg='white', bg="green", command=show_results)
btn_show_results.grid(row=1, column=1, padx=30)



    



window.mainloop()