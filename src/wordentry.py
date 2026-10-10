from tkinter import *

class WordEntry(Frame):
    """Singe entry with word translation and description"""

    def __init__(self, parent, word, translation, description):
        super().__init__(parent)

        self.config(bg='purple')

        self._make_entry(word, translation, description)


    def _make_entry(self, word, translation, description):
        for i in [word, translation, description]:
            Label(self, text=i, font=('Helvetica', 14)).pack(side=LEFT)


    def place_self(self):
        self.pack(fill='x', anchor='n')
