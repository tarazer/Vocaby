from tkinter import *

class WordEntry(Frame):
    """Singe entry with word translation and description"""

    def __init__(self, parent, word, translation):
        super().__init__(parent, bg='purple')
        self.parent = parent

        self._make_entry(word, translation)


    def _make_entry(self, word, translation):
        self.word = Label(self, text=word, font=('Helvetica', 14))
        self.word.pack(side=LEFT, padx=(5,0))
        
        self.translation = Label(self, text=translation, font=('Helvetica', 14))
        self.translation.place(relx=0.5, y=5)


    def place_self(self):
        self.pack(fill='x',anchor='n', ipady=5, ipadx=5)

