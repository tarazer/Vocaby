from tkinter import *

class WordEntry(Frame):
    """Singe entry with word translation and description"""

    def __init__(self, parent):
        super().__init__(parent, bg='purple')
        self.parent = parent

        self.id = None
        self.book_id = None

        self._make_labels()


    def _make_labels(self):
        self.word = Label(self, text='', font=('Helvetica', 14))
        self.word.pack(side=LEFT, padx=(5,0))
        
        self.translation = Label(self, text='', font=('Helvetica', 14))
        self.translation.place(relx=0.5, y=5)


    def insert_labels(self, values):
        self.id = values[0]
        self.book_id = values[3]
        self.w = values[1]
        self.t = values[2]

        self.word.config(text=self.w)
        self.translation.config(text=self.t)


    def clear(self):
        self.id =           None
        self.book_id =      None
        self.word.config(text='')
        self.translation.config(text='')


    def place_self(self):
        self.pack(fill='x',anchor='n', ipady=5, ipadx=5)

