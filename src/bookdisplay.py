from tkinter import *

from bookframe import BookFrame

class BookDisplay(Frame):
    """Box that holds and manages all Books 
    in Homecontent on Homepage"""

    def __init__(self, parent, pagemanager, database, wordpage):
        super().__init__(parent)
        self.pm = pagemanager
        self.db = database
        self.wp = wordpage

        self.books = {}

        self.config(bg='lime',)


    def addBook(self, valueList):
        """UI Stuff when new book is added"""
        if valueList == None: # Guard against empty input
            print('Title is empty')
            return None

        # Book Frame db entry and creating visual of book frame        
        self.db.c.execute("""
            INSERT INTO books (name, language, description) VALUES (?, ?, ?)
            """, (valueList))
        self.db.conn.commit()

        self.db.c.execute("""
            SELECT rowid,* 
            FROM books 
            WHERE rowid = (SELECT MAX(rowid) FROM books)
            """)
        FullList = self.db.c.fetchone()
        self.place_book(FullList)


    def delete_book(self, book_frame):
        id = self.books[book_frame]
        self.db.c.execute("""DELETE FROM books WHERE rowid=(?)""", (id,))
        self.db.conn.commit()

        book_frame.destroy()        


    def place_book(self, values):
        id =            values[0]
        title =         values[1]
        language =      values[2]
        description =   values[3]

        book_frame = BookFrame(self, title, language, description)

        # Place Bookframe and assign itself as key to a id value
        book_frame.pack(side=LEFT, anchor='n', padx=(0, 20))   
        self.books[book_frame] = id


    def openBook(self, event):
        id = self.books[event.widget.master]
        self.pm.show_page('list')
        self.wp.load(id)


    def load_books(self):
        self.db.c.execute("SELECT rowid,* FROM books")
        book_values = self.db.c.fetchall()

        for values in book_values:
            self.place_book(values)


    def place_self(self):
        self.place(relwidth=1, 
            relheight=1,
            width=-40,
            y=20,
            anchor='center',
            rely=0.5,
            relx=0.5,)
