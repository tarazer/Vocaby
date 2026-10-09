from tkinter import *


class BookPage(Frame):
    """The Frame that holds the actual words and 
    translations for books of the Home Page"""

    def __init__(self, parent, pagemanager, database):
        super().__init__(parent)
        self.pm = pagemanager
        self.db = database

        self.config(bg='grey')

        self.current_book = ''
        self.current_table = None

        self._back_button()


    def _back_button(self):
        BackBtn = Button(self.pm.pages['list'], 
                    text='back',
                    width=8,
                    height=2,
                    command=lambda:self.pm.hide_page('list'))

        BackBtn.place(x=10, y=10)

        
    def load(self):
        print('Loading Book ID:', self.pm.book_id)
        self.db.c.execute("""SELECT * FROM books WHERE id IS ...""", self.pm.book_id)
        self.current_book = self.db.c.fetchall()
        
        print(self.current_book)
