import tkinter as tk
import tkinter.ttk as ttk
import requests
import movieresultapp



class MovieMainApp:
    def __init__(self, master=None):
        self.result_labels = []
        # build ui
        self.main_window = tk.Tk() if master is None else tk.Toplevel(master)
        self.frm_search = ttk.Labelframe(self.main_window)
        self.lbl_app_name = ttk.Label(self.frm_search)
        self.lbl_app_name.configure(anchor='center', background='#8000ff', font='{Agency FB} 24 {bold}', foreground='#ffffff')
        self.lbl_app_name.configure(text='News Search', width='800')
        self.lbl_app_name.pack(side='top')
        self.entry2 = ttk.Entry(self.frm_search)
        self.entry2.configure(font='{Arial} 12 {}', justify='center', width='40')
        _text_ = '''search a topic...'''
        self.entry2.delete('0', 'end')
        self.entry2.insert('0', _text_)
        self.entry2.pack(pady='10', side='top')
        self.entry2.bind('<Return>', self.search_movie, add='')
        self.frm_search.configure(height='100', text='Search Movie', width='800')
        self.frm_search.pack(side='top')
        self.results = ttk.Labelframe(self.main_window)
        self.results.configure(height='200', text='Results', width='800')
        self.results.pack(side='top')
        self.main_window.configure(height='200', width='200')
        self.main_window.geometry('800x320')

        # Main widget
        self.mainwindow = self.main_window

    def search_movie(self, event=None):
        for old_lbl in self.result_labels:
            old_lbl.pack_forget()
        url = "https://newsapi.org/v2/everything"

        querystring = {"q":self.entry2.get(),"apiKey":"af30ae0a9c364ea6aab99f4745480cea","pageSize":"5"}

        

        response = requests.request("GET", url, params=querystring)

        articles = response.json()['articles']

        for article in articles:
            lbl = ttk.Label(self.results)
            lbl.configure(background='#e2e2e2', cursor='hand2', padding='5', relief='flat')
            lbl.configure(text=article['title'], width='800')
            lbl.pack(side='top')
            lbl.bind('<Button-1>', lambda event, arg=article: self.get_news_detail(event,arg))
            self.result_labels.append(lbl)
            # self.label4 = ttk.Label(self.results)
            # self.label4.configure(background='#f0f0f0', cursor='hand2', padding='5', text='movie 2')
            # self.label4.configure(width='800')
            # self.label4.pack(side='top')

    def get_news_detail(self,  event=None, article=None):
        app = movieresultapp.MovieResultApp(self.main_window, article=article)

    def run(self):
        self.mainwindow.mainloop()

if __name__ == '__main__':
    app = MovieMainApp()
    app.run()

