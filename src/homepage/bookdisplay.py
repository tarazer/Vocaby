from tkinter import *
from tkinter import messagebox
import math

from .bookframe import BookFrame

class BookDisplay(Frame):
    """Box that holds and manages all Books 
    in Homecontent on Homepage"""

    def __init__(self, parent, pagemanager, database, wordpage):
        super().__init__(parent)
        self.pm = pagemanager
        self.db = database
        self.wp = wordpage
        
        self.books = {} 

        # For checking if column or amount elements
        # matches previous reload so it doesnt get 
        # reloaded each time screen is resized
        self.prev_columns = None
        self.prev_num = None

        self.config(bg='lime',)


    def addBook(self, values):
        """UI Stuff when new book is added"""
        if values == None: # Guard against empty input
            print('Title is empty')
            return None

        # Book Frame db entry and creating visual of book frame        
        self.db.insert_new_values('books', values)

        #self.db.c.execute("""
        #    SELECT rowid,* 
        #    FROM books 
        #    WHERE rowid = (SELECT MAX(rowid) FROM books)
        #    """)
        full_values = self.db.get_newest_entry('books')
        self.place_book(full_values)
        self.db.book_values.append(full_values)
        self.load_books()


    def delete_book(self, book_frame):
        result = messagebox.askyesno(message="Are you sure you want to delete the book?", default='no', icon='warning', detail="This action cannot be undone.")
        if result == True:
            id = self.books[book_frame]
            self.db.removed_book_ids.append(id)
            book_frame.destroy()

            for book in self.db.book_values:
                if book[0] == id:
                    self.db.book_values.remove(book)


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
        book_values = self.db.book_values
        
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

        
