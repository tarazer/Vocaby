from tkinter import *

class WordEditorForm(Frame):

    def __init__(self, parent):
        super().__init__(parent, bg='orange')
        self.parent = parent
        
        self._make_entry()
        self._make_buttons()


    def _make_entry(self):
        self.word = Entry(self, font=('Helvetica', 14))
        self.word.place(x=5, rely=0.5, anchor='w', relwidth=0.5, width=-10)
        
        self.translation = Entry(self, font=('Helvetica', 14))
        self.translation.place(relx=0.5, rely=0.5, anchor='w',relwidth=0.4, width=-5)


    def _make_buttons(self):
        delete_btn = Button(self, text='Del', command=self.parent.delete_word)
        delete_btn.place(relx=0.9, rely=0.5, relwidth=0.1, width=-5,anchor='w')


    def clear_entries(self):
        self.word.delete(0, END)
        self.translation.delete(0, END)


    def place_self(self):
        self.place(relwidth=1, height=40)
