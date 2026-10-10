from tkinter import *

class WordEntry(Frame):
    """Singe entry with word translation and description"""

    def __init__(self, parent, word, translation, description):
        super().__init__(parent)
        self.db = database

        self.config(bg='purple')

        self._make_entry(word, translation, description)


    def _make_entry(self, word, translation, description):
        Label(self, text=word).pack()
        Label(self, text=translation).pack()
        Label(self, text=description).pack()


    def place_self(self):
        self.place(relx=0.5, rely=0.5, anchor=CENTER)
