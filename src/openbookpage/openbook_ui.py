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

        self._make_pageback_button()
        self._make_pageforth_button()


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


    def _make_pageback_button(self):
        self.pageback_btn = Button(self.parent, 
                                text='B', 
                                width=3, 
                                height=3, 
                                command=self.pageback)

        self.pageback_btn.place(relx=0.15, rely=0.5, anchor=CENTER)


    def _make_pageforth_button(self):
        self.pageforth_btn = Button(self.parent, 
                                text='F', 
                                width=3, 
                                height=3, 
                                command=self.pageforth)

        self.pageforth_btn.place(relx=0.85, rely=0.5, anchor=CENTER)
                

    def pageforth(self):
        page = self.wp.current_page + 1
        if page > self.wp.max_page:
            page = self.wp.current_page
        self.wp.current_page = page
        self.wp.load(self.wp.current_id)


    def pageback(self):
        page = self.wp.current_page - 1
        if page <= 0:
            page = 1
        self.wp.current_page = page        
        self.wp.load(self.wp.current_id)


    def load(self, id):
        self.current_id = id
        self.current_book = self.db.get_book_by_id(id)[1]
        print(self.current_book)
        self.book_label.config(text=self.current_book)
