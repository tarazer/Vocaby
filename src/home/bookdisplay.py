from tkinter import *
from tkinter import messagebox
import math

from .bookframe import BookFrame

class BookDisplay(Frame):
    """Box that holds and manages all Books 
    in Homecontent on Homepage"""

    def __init__(self, parent, pagemanager, database, wordpage):
        super().__init__(parent, bg='lime')
        self.pm = pagemanager
        self.db = database
        self.wp = wordpage
        
        self.active_list = []
        self.deleted_list = []

        for values in self.db.get_books():
            self.place_book(values)

        self.prev_columns = 1
        self.prev_rows = 1
        self.prev_length = 1


    def addBook(self, values):
        """UI Stuff when new book is added"""
        
        # Book Frame db entry and creating visual of book frame        
        self.db.insert_new_values('books', values)

        full_values = self.db.get_newest_entry('books')
        self.place_book(full_values)
        self.load_books()


    def delete_book(self, book_frame):
        result = messagebox.askyesno(message="Are you sure you want to delete this book?", 
        default='no', 
        icon='warning', 
        detail="This action cannot be undone.")
        
        if result == True:
            id = book_frame.id 
            
            self.db.delete_id_from_table('books', id)
            self.active_list.remove(book_frame)
            self.deleted_list.append(book_frame)
            
        self.load_books()


    def openBook(self, event):
        id = event.widget.master.id
        self.pm.show_page('list')
        self.wp.load(id)


    def place_book(self, values): 
        """Create book using values without placing it"""
        id =            values[0]
        title =         values[1]
        language =      values[2]
        description =   values[3]

        book_frame = BookFrame(self, title, language, description, id)
        self.active_list.append(book_frame)


    def load_books(self):
        rows, columns = self.get_dimensions(len(self.active_list))
        row = column = 0

        # Delete removed books
        for widget in self.deleted_list[:]:
            self.deleted_list.remove(widget)
            widget.destroy()

        if columns != self.prev_columns or rows != self.prev_rows or len(self.active_list) != self.prev_length:
            print('reload')
            for book in self.active_list:
                if column >= columns:
                    row += 1
                    column = 0

                book.grid(row=row, column=column,padx=(0, 20), pady=(0,20)) 
                column += 1

            self.prev_columns = columns
            self.prev_rows = rows
            self.prev_length = len(self.active_list)


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

        
