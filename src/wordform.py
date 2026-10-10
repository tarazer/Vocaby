from tkinter import *

class WordForm(Frame):
    """Form for adding new words"""

    def __init__(self, parent, pagemanager, database):
        super().__init__(parent)
        self.parent = parent
        self.pm = pagemanager
        self.db = database

        self.config(bg='cyan')

        self._make_title_entry()
        self._make_translation_entry()
        self._make_description_entry()
        self._make_add_button()


    def _make_title_entry(self):
        title_entry = Entry(self, 
            font=('Helvetica', 12))

        title_entry.place(anchor='w', rely=0.5, relx=0.025 ,relwidth=0.2) 


    def _make_translation_entry(self):
        title_entry = Entry(self, 
            font=('Helvetica', 12))

        title_entry.place(anchor='w', rely=0.5, relx=0.25, relwidth=0.2) 


    def _make_description_entry(self):
        title_entry = Entry(self, 
            font=('Helvetica', 12))

        title_entry.place(anchor='w', rely=0.5, relx=0.475, relwidth=0.35)


    def _make_add_button(self):
        AddBtn = Button(self,
            font=('Helvetica', 12),
            text='Add')

        AddBtn.place(anchor='w', rely=0.5, relx=0.85, relwidth=0.125) 


    def place_self(self):
        self.place(
            relwidth=0.7,
            height=60,
            relx=0.5,
            rely=1,
            y=-10,
            anchor='s')
