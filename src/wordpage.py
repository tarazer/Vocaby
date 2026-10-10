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

        self._make_back_button()
        self._make_book_label()


    def _make_back_button(self):
        BackBtn = Button(self.parent, 
                    text='back',
                    width=8,
                    height=2,
                    font=('Helvetica', 12),
                    command=lambda:self.pm.hide_page('list'))

        BackBtn.place(x=10, y=10)


    def _make_book_label(self):
        self.book_label = Label(self.parent, 
            text='',
            bg='green',
            font=('Helvetica', 14),
            height=2,)

        self.book_label.place(relx=0.5, y=12, anchor='n')

        
    def load(self, id):
        self.current_id = id
        print('Loading Book ID:', id)
        self.db.c.execute("""SELECT * FROM books WHERE rowid=(?)""", (id,))
        self.current_book = self.db.c.fetchone()[0]
        
        self.book_label.config(text=self.current_book)
        
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
            height=-80)
