import tkinter as tk
import tkinter.ttk as ttk
from PIL import ImageTk, Image
import requests
from io import BytesIO
import cv2

class MovieResultApp:
    def __init__(self, master=None, article=None):
        # build ui
        self.result_window = tk.Tk() if master is None else tk.Toplevel(master)
        self.frame2 = ttk.Frame(self.result_window)
        self.label5 = ttk.Label(self.frame2)
        self.label5.configure(anchor='center', font='{Arial} 24 {}', foreground='#8000ff', padding='5')
        self.label5.configure(text=article['title'], width='800')
        self.label5.pack(side='top')
        self.separator1 = ttk.Separator(self.frame2)
        self.separator1.configure(orient='vertical')
        self.separator1.pack(expand='true', side='top')
        self.poster = ttk.Label(self.frame2)
        response = requests.get(article['urlToImage'])
        self.poster_png = Image.open(BytesIO(response.content))
        self.poster_png = self.poster_png.resize((320,240), Image.NEAREST)
        self.poster_png = ImageTk.PhotoImage(self.poster_png)
        #cv2.imshow('Test', self.poster_png)
        self.poster.configure(font='TkDefaultFont', image=self.poster_png)
        self.poster.pack(pady='10', side='top')
        self.text1 = tk.Text(self.frame2)
        self.text1.configure( borderwidth='0', font='{Arial} 10 {}', height='10')
        self.text1.configure(padx='20', state='disabled', undo='false', width='800', pady=20)
        self.text1.configure(wrap='word')
        _text_ = article['description']
        self.text1.configure(state='normal')
        self.text1.insert('0.0', _text_)
        self.text1.configure(state='disabled')
        self.text1.pack(side='top')
        self.label7 = ttk.Label(self.frame2)
        self.label7.configure(font='{Arial} 12 {bold}', justify='left', text=f'Author : {article["author"]}', width='800')
        self.label7.pack(padx='20', pady='10', side='top')
        self.label8 = ttk.Label(self.frame2)
        self.label8.configure(font='{Arial} 12 {}', foreground='#008040', text=f'URL : {article["url"]}', width='800')
        self.label8.pack(padx='20', pady='10', side='top')
        self.btn_close = ttk.Button(self.frame2)
        self.btn_close.configure(text='Close')
        self.btn_close.pack(pady='5', side='top')
        self.btn_close.configure(command=self.close_result_window)
        self.frame2.configure(height='670', width='800')
        self.frame2.pack(side='top')
        self.result_window.configure(height='200', width='200')
        self.result_window.geometry('800x670')

        # Main widget
        self.mainwindow = self.result_window

    def close_result_window(self):
        self.result_window.destroy()

    def run(self):
        self.mainwindow.mainloop()

if __name__ == '__main__':
    app = MovieResultApp()
    app.run()

