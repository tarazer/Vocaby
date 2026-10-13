from tkinter import *

class WordEntry(Frame):
    """Singe entry with word translation and description"""

    def __init__(self, parent, word, translation, description):
        super().__init__(parent)
        self.config(bg='purple')

        self._make_entry(word, translation, description)


    def _make_entry(self, word, translation, description):
        Label(self, text=word, font=('Helvetica', 14)).pack(side=LEFT, padx=(5,0)) # word 
        Label(self, text=translation, font=('Helvetica', 14)).pack(side=LEFT, padx=(5,0))
        Label(self, text=description, font=('Helvetica', 14)).place(anchor='nw', relx=0.5, y=5)


    def place_self(self):
        self.pack(fill='x',anchor='n', ipady=5, ipadx=5)
