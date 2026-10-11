from tkinter import *
import math

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

        self.prev_columns = None
        self.prev_num = None

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
        self.load_books()


    def delete_book(self, book_frame):
        id = self.books[book_frame]
        self.db.c.execute("""DELETE FROM books WHERE rowid=(?)""", (id,))
        self.db.conn.commit()

        book_frame.destroy()        


    def place_book(self, values, row=0, column=0):
        id =            values[0]
        title =         values[1]
        language =      values[2]
        description =   values[3]

        book_frame = BookFrame(self, title, language, description)

        # Place Bookframe and assign itself as key to a id value
        book_frame.grid(row=row, column=column,padx=(0, 20), pady=(0,20))   
        self.books[book_frame] = id


    def openBook(self, event):
        id = self.books[event.widget.master]
        self.pm.show_page('list')
        self.wp.load(id)


    def load_books(self, event=None):
        self.db.c.execute("SELECT rowid,* FROM books")
        book_values = self.db.c.fetchall()

        rows, columns = self.get_dimensions(len(book_values))
        row = column = 0

        if columns != self.prev_columns:
            for book in self.winfo_children():
                book.destroy()
        

        if columns != self.prev_columns or len(book_values) != self.prev_num:
        
            for values in book_values:
                if column >= columns:
                    row+=1
                    column = 0
                self.place_book(values, row, column)
                column+=1

        self.prev_columns = columns
        self.prev_num = len(book_values)
        self.prev_num = len(book_values)


    def get_dimensions(self, num_elements):
        """Get amount of columns fit and how many rows 
        it needs with current display width"""
        self.master.update()
        width = self.winfo_width()

        columns = width // 220
        if columns < 1:
            columns = 1
        rows = math.ceil(num_elements / columns)
        
        return rows, columns


    def place_self(self):
        self.place(relwidth=1, 
            relheight=1,
            width=-40,
            y=20,
            anchor='center',
            rely=0.5,
            relx=0.5,)

        
