from tkinter import *

class WordForm(Frame):
    """Form for adding new words"""

    def __init__(self, wordpage, pagemanager, database):
        super().__init__(wordpage.master)
        self.wp = wordpage
        self.pm = pagemanager
        self.db = database

        self.config(bg='cyan')

        self._make_word_entry()
        self._make_translation_entry()
        self._make_description_entry()
        self._make_add_button()


    def _make_word_entry(self):
        self.word_entry = Entry(self, 
            font=('Helvetica', 12))

        self.word_entry.place(anchor='w', rely=0.5, relx=0.025 ,relwidth=0.2) 


    def _make_translation_entry(self):
        self.translation_entry = Entry(self, 
            font=('Helvetica', 12))

        self.translation_entry.place(anchor='w', rely=0.5, relx=0.25, relwidth=0.2) 


    def _make_description_entry(self):
        self.description_entry = Entry(self, 
            font=('Helvetica', 12))

        self.description_entry.place(anchor='w', rely=0.5, relx=0.475, relwidth=0.35)


    def _make_add_button(self):
        AddBtn = Button(self,
            font=('Helvetica', 12),
            text='Add',
            command=lambda:self.wp.add_word(self.get_values()))

        AddBtn.place(anchor='w', rely=0.5, relx=0.85, relwidth=0.125)


    def get_values(self):
        word = self.word_entry.get()
        translation = self.translation_entry.get()
        description = self.description_entry.get()

        self.clear_form()

        return [word, translation, description]


    def clear_form(self):
        self.word_entry.delete(0, END)
        self.translation_entry.delete(0, END)
        self.description_entry.delete(0, END)


    def place_self(self):
        self.place(
            relwidth=0.7,
            height=60,
            relx=0.5,
            rely=1,
            y=-10,
            anchor='s')
