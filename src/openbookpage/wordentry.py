from tkinter import *

class WordEntry(Frame):
    """Singe entry with word translation and description"""

    def __init__(self, parent, word, translation):
        super().__init__(parent)
        self.parent = parent
        self.config(bg='purple')

        self._make_entry(word, translation)
        self._make_edit_btn()


    def _make_entry(self, word, translation):
        self.word = Label(self, text=word, font=('Helvetica', 14))
        self.word.pack(side=LEFT, padx=(5,0))
        
        self.translation = Label(self, text=translation, font=('Helvetica', 14))
        self.translation.place(relx=0.5, y=5)
       

    def _make_edit_btn(self):
        self.edit_label = Label(self, text='Edit', font=('Helvetica', 14))
        self.edit_label.place(relx=1, anchor='ne', x=-5, y=5, relheight=1, height=-10)

        self.edit_label.bind('<Button-1>', self.parent.delete_entry)


    def place_self(self):
        self.pack(fill='x',anchor='n', ipady=5, ipadx=5)

