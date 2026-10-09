import sqlite3
from tkinter import *


class PageManager:
    """Manage windows and forms"""
    def __init__(self):
        self.pages = {}
        

    def addPage(self, key, value):
        self.pages[key] = value


    def show_pages(self): # for debugging
        print(self.pages)


    def show_page(self, page, id=None):
        if id == None:
            self.pages[page].tkraise()    
        else:
            self.pages[page].tkraise()
            Label(self.pages['list'], 
                text=id,
                font=('Helvetica', 18)
                ).place(relx=0.5, rely=0.5, anchor=CENTER)
            # Func that loads words for ListPage
            
        

    def hide_page(self, page):
        self.pages[page].lower()


    def openList(self, id):
        pass



class Database():
    """sqlite database"""
    def __init__(self):
        self.conn = sqlite3.connect("books.db")
        self.c = self.conn.cursor()

        #Create Table
        self.c.execute("""
            CREATE TABLE IF NOT EXISTS books (
                id INTEGER PRIMARY KEY,
                name text,
                language text,
                description text
            )""")
        
        self.conn.commit()
    



class BookBox(Frame):
    """Box that holds and manages all Books 
    in Homecontent on Homepage"""

    def __init__(self, parent, pagemanager, database):
        super().__init__(parent)
        self.pm = pagemanager
        self.db = database

        self.books = {}

        self.config(
            bg='lime',
            )


    def addBook(self, valueList):
        """UI Stuff when new book is added"""
        if valueList == None: # Guard against empty input
            print('Title is empty')
            return None

        # Create Visual of book frame
        self.placeBook(valueList)

        # Book Frame db entry
        self.db.c.execute("""
            INSERT INTO books (name, language, description) VALUES (?, ?, ?)
            """, (valueList))
        self.db.conn.commit()
        

    def placeBook(self, values):
        id = values[0]
        title = values[1]
        language = values[2]
        description = values[3]

        colorcode = {
            'None': 'red',
            'Spanish': 'orange',
            'Russian': 'blue'
        }

        BookFrame = Frame(self, bg='white', width=200, height=300, cursor='hand2')
        BookFrame.pack_propagate(False)

        Title = Label(BookFrame, text=title)
        Title.pack(anchor='n', pady=5)
        LangFrame = Frame(BookFrame, bg=colorcode[language], width=180, height=90)
        LangFrame.pack()
        Label(BookFrame, text=description, wraplength=180).pack(pady=5)
        
        BookFrame.pack(side=LEFT, anchor='n', padx=(0, 20))   

        self.books[BookFrame] = id

        BookFrame.bind('<Button-1>', self.openBook)
        for c in BookFrame.winfo_children():
            c.bind('<Button-1>', self.openBook)


    def openBook(self, event):
        try:
            id = self.books[event.widget]
        except:
            id = self.books[event.widget.master]
        self.pm.show_page('list', id)


    def loadBooks(self):
        self.db.c.execute("SELECT * FROM books")
        books = self.db.c.fetchall()

        for b in books:
            self.placeBook(b)

        print(self.books)



            
#print(c.fetchone())
#print(c.fetchmany(5))
#c.fetchall()
