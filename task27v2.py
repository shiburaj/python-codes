"""
Problem Statement:  WAP to make a Voting app which allows you to cast
                    your vote as well as show the results.

Given: voting.db with 4 candidates inside the candidates table.
Author:             Prof. Shiburaj
"""
import tkinter as tk
from tkinter import ttk
import sqlite3
from tkinter import messagebox

conn = sqlite3.connect('voting.db')
cur = conn.cursor()

main_window = tk.Tk()
voting_window = None
result_window = None
main_window.geometry("1200x800")
main_window.title("Voting App")
main_window.columnconfigure([0,1], weight=1)
voted = None
#main_window.rowconfigure([0,1,2,3,4,5,6,7], weight=1, minsize=55)

lbl_app_name = tk.Label(main_window, text="Voting App", font=('Times New Roman', 30), fg='purple')
lbl_app_name.grid(row=0, column=0, columnspan=2, pady=80)


# Results
def show_results():
    global result_window
    result_window = tk.Tk()
    result_window.geometry("600x600")
    result_window.title("Results")
    

    lbl_section_name = tk.Label(result_window, text="Results", font=('Times New Roman', 25), fg='red')
    lbl_section_name.pack(pady=60)

    results = cur.execute("SELECT * FROM candidates")
    count = 0
    
    for row in results:
        count += 1
        cand_data = row[1]+" : "+str(row[2])
        tk.Label(result_window, text=cand_data ,font=('Times New Roman', 22)).pack()

    btn_back = tk.Button(result_window, text="Back", font=('Times New Roman', 20), command=result_window.destroy)
    btn_back.pack(pady=50)

# Cast Vote
def cast_vote():
    print(voted.get())
    cur.execute("UPDATE candidates SET votes = votes + 1 WHERE id = "+ str(voted.get()))
    conn.commit()

    voting_window.destroy()

    messagebox.showinfo('Success', 'Thank you for your vote.')


# Voting
def show_voting():

    global voting_window,voted
    voting_window = tk.Tk()
    voting_window.geometry("600x800")
    voting_window.title("New Vote")
    voted = tk.IntVar(voting_window)

    lbl_section_name = tk.Label(voting_window, text="Select Your Candidate", font=('Times New Roman', 25), fg='blue')
    lbl_section_name.pack(pady=50)
    cur = conn.cursor()
    results = cur.execute("SELECT * FROM candidates")
    count = 0
    
    for row in results:
        count += 1
        ttk.Radiobutton(voting_window, text=row[1], value=row[0], variable=voted).pack(pady=20)

    btn_vote = tk.Button(voting_window, text="Vote", font=('Times New Roman', 20), command=cast_vote, fg="white", bg="purple", padx=30)
    btn_vote.pack(pady=30)
    btn_back = tk.Button(voting_window, text="Close", font=('Times New Roman', 20), command=voting_window.destroy)
    btn_back.pack(pady=30)


frm_index = tk.Frame(main_window)
frm_results = tk.Frame(main_window)
frm_results_inner = tk.Frame(main_window)
frm_voting = tk.Frame(main_window)
frm_thank_you = tk.Frame(main_window)
    
frm_index.grid(row=1, column=0, columnspan=2, pady=180)
btn_cast_vote = tk.Button(frm_index, text="Cast a Vote", font=('Times New Roman', 30), fg='white', bg="red", command=show_voting)
btn_cast_vote.grid(row=1, column=0, padx=30)
btn_show_results = tk.Button(frm_index, text="Show Results", font=('Times New Roman', 30), fg='white', bg="green", command=show_results)
btn_show_results.grid(row=1, column=1, padx=30)



    



main_window.mainloop()