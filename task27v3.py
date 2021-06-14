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
from tkinter import font

conn = sqlite3.connect('voting.db')
cur = conn.cursor()

main_window = tk.Tk()
voting_window = None
result_window = None
main_window.geometry("1200x800")
main_window.title("Voting App")
main_window.columnconfigure([0,1], weight=1)
voted = None
style = ttk.Style(main_window)
#print(style.theme_names()) #('winnative', 'clam', 'alt', 'default', 'classic', 'vista', 'xpnative')
style.theme_use('winnative')
#main_window.rowconfigure([0,1,2,3,4,5,6,7], weight=1, minsize=55)

lbl_app_name = tk.Label(main_window, text="Voting App", font=('Times New Roman', 30), fg='purple')
lbl_app_name.grid(row=0, column=0, columnspan=2, pady=80)


# Results
def show_results():
    global result_window
    result_window = tk.Tk()
    result_window.geometry("800x600")
    result_window.title("Results")
    style = ttk.Style(result_window)
    style.configure("mystyle.Treeview", highlightthickness=0, bd=0, font=('Calibri', 15)) # Modify the font of the body
    style.configure("mystyle.Treeview.Heading", font=('Calibri', 15,'bold'),lightcolor="#cecece", bordercolor="#cecece",
                darkcolor="#ececec", borderwidth=1) # Modify the font of the headings
    #style.layout("mystyle.Treeview", [('mystyle.Treeview.treearea', {'sticky': 'nswe'})]) # Remove the borders
    #style = ttk.Style(result_window)
    #print(style.theme_names()) #('winnative', 'clam', 'alt', 'default', 'classic', 'vista', 'xpnative')
    #style.theme_use('clam')

    lbl_section_name = tk.Label(result_window, text="Results", font=('Times New Roman', 25), fg='red')
    lbl_section_name.pack(pady=60)

    results = cur.execute("SELECT * FROM `candidates`")
    res = ttk.Treeview(result_window, columns=('id','name', 'votes'), displaycolumns=('id','name', 'votes'), show='headings', style='mystyle.Treeview')
    # res.column('id', anchor='w',stretch='true',width='40',minwidth='20')
    # res.column('name', anchor='w',stretch='true',width='250',minwidth='80')
    res.column('votes', anchor='center')
    res.heading('id', anchor='w',text='ID')
    res.heading('name', anchor='w',text='Candidate Name')
    res.heading('votes', anchor='center',text='No. of Votes')
    res.pack()
    
    for row in results:
        res.insert('', 'end', text='', values=(row[0],row[1], row[2]), tags=('tbl_row',))
        res.tag_configure('tbl_row', background='yellow')
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
    voting_window.geometry("600x600")
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