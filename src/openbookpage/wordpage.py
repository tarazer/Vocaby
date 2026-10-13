from tkinter import *
from .wordentry import WordEntry


class WordPage(Frame):
    """The Frame that holds the actual words and 
    translations for books of the Home Page"""

    def __init__(self, parent, pagemanager, database):
        super().__init__(parent)
        self.parent = parent
        self.pm = pagemanager
        self.db = database

        self.config(bg='grey')

        self.words = {}

        self.current_book = ''
        self.current_id = None
        self.current_words = []

        self._back_button()
        self._make_book_label()


    def _back_button(self):
        BackBtn = Button(self.parent, 
                    text='back',
                    width=8,
                    height=2,
                    command=self._clear_page)

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

        self._load_words()


    def _load_words(self):
        self.db.c.execute("""SELECT rowid,* FROM words WHERE book_id=(?)""", (self.current_id,))
        word_info = self.db.c.fetchall()

        for word in word_info:
            wordentry = WordEntry(self, word[1], word[2])
            wordentry.place_self()
            self.current_words.append(wordentry)

            self.words[wordentry] = word[0]
        

    def add_word(self, valueList):
        word =          valueList[0]
        translation =   valueList[1]
        book_id =       self.current_id
        
        valueList.append(self.current_id)
        self.db.c.execute("""
            INSERT INTO words
            VALUES (?,?,?)
        """, (word, translation, book_id))

        self.db.conn.commit()

        self.db.c.execute("""
            SELECT rowid
            FROM books 
            WHERE rowid = (SELECT MAX(rowid) FROM books)
            """)

        wordentry = WordEntry(self, word, translation)
        wordentry.place_self()
        self.words[wordentry] = self.db.c.fetchone()
        self.current_words.append(wordentry)


    def _clear_page(self):
        self.pm.hide_page('list')
        for word in self.current_words:
            word.destroy()

        self.db.delete_removed_words()
        self.current_words.clear()
        self.words.clear()


    def delete_entry(self, event):
        we = event.widget.master
        self.db.removed_word_ids.append(self.words[we])
        we.destroy()


    def place_self(self):
        self.place(
            relx=0.5, 
            rely=1, 
            anchor='s', 
            relwidth=0.6, 
            relheight=1,
            height=-70)
