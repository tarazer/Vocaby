from tkinter import *
from wordentry import WordEntry


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
        self.current_words = []

        self._back_button()


    def _back_button(self):
        BackBtn = Button(self.parent, 
                    text='back',
                    width=8,
                    height=2,
                    command=lambda:self.pm.hide_page('list'))

        BackBtn.place(x=10, y=10)

        
    def load(self, id):
        self.current_id = id
        print('Loading Book ID:', id)
        self.db.c.execute("""SELECT * FROM books WHERE rowid=(?)""", (id,))
        self.current_book = self.db.c.fetchall()
        
        print(self.current_book)


    def _load_words(self):
        pass


    def add_word(self):
        we = WordEntry(self, )
        we.place_self()
        self.current_words.append(we)


    def place_self(self):
        self.place(
            relx=0.5, 
            rely=1, 
            anchor='s', 
            relwidth=0.6, 
            relheight=1,
            height=-70)
