from tkinter import *

class WordForm(Frame):
    """Form for adding new words"""

    def __init__(self, parent, pagemanager, database):
        super().__init__(parent)
        self.parent = parent
        self.pm = pagemanager
        self.db = database

        self.config(bg='cyan')


    #def 


    def place_self(self):
        self.place(
            relwidth=0.5,
            height=70,
            relx=0.5,
            rely=1,
            y=-10,
            anchor='s')
