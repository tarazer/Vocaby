from tkinter import *


class WordPage(Frame):
    """The Frame that holds the actual words and 
    translations for books of the Home Page"""

    def __init__(self, parent, pagemanager, database):
        super().__init__(parent)
        self.parent = parent
        self.pm = pagemanager
        self.db = database

        self.config(bg='grey')

        self.current_book = ''
        self.current_id = None

        self._back_button()
        self._add_word_button()


    def _back_button(self):
        BackBtn = Button(self.parent, 
                    text='back',
                    width=8,
                    height=2,
                    command=lambda:self.pm.hide_page('list'))

        BackBtn.place(x=10, y=10)


    def _add_word_button(self):
        AddWordBtn = Button(self.parent,
                    text='Add Word',
                    width=8,
                    height=2,
                    command=lambda:print('adding word'))

        AddWordBtn.place(relx=1, x=-10, y=10, anchor='ne')

        
    def load(self, id):
        self.current_id = id
        print('Loading Book ID:', id)
        self.db.c.execute("""SELECT * FROM books WHERE rowid=(?)""", (id,))
        self.current_book = self.db.c.fetchall()
        
        print(self.current_book)


    def _load_words(self):
        pass


    def place_self(self):
        self.place(
            relx=0.5, 
            rely=0.5, 
            anchor=CENTER, 
            relwidth=0.5, 
            relheight=1)
