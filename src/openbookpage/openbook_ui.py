from tkinter import *

class UI_OpenBook:
    """Has the UI elements for the OpenBookPage"""
    def __init__(self, parent, database, pagemanager, wordpage):
        self.pm = pagemanager
        self.db = database
        self.parent = parent
        self.wp = wordpage

        self.current_book = ''
        self.current_id = None

        self._make_back_button()
        self._make_book_label()


    def _make_back_button(self):
        BackBtn = Button(self.parent, 
                    text='back',
                    width=8,
                    height=2,
                    command=self.wp.clear_page)

        BackBtn.place(x=10, y=10)


    def _make_book_label(self):
        self.book_label = Label(self.parent,
                        text=self.current_book,
                        bg='green',
                        font=('Helvetica', 14),)

        self.book_label.place(y=20, relx=0.5, anchor='n')


    def load(self, id):
        self.current_id = id
        self.current_book = self.db.get_book_by_id(id)
        self.book_label.config(text=self.current_book)

        self.wp.load(id)
