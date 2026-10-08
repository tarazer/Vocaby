import sqlite3
from tkinter import *


class PageManager:
    """Manage windows and forms"""
    def __init__(self):
        self.pages = {}
        

    def addPage(self, key, value):
        self.pages[key] = value


    def show_pages(self):
        print(self.pages)


    def show_page(self, page):
        self.pages[page].tkraise()    

    def hide_page(self, page):
        self.pages[page].lower()



# DB Stuff
conn = sqlite3.connect("books.db")
c = conn.cursor()

#Create Table
c.execute("""
    CREATE TABLE IF NOT EXISTS books (
        id INTEGER PRIMARY KEY,
        name text,
        language text,
        description text
    )""")

conn.commit()


def LoadBooks(parent):
    c.execute("SELECT * FROM books")
    books = c.fetchall()
    for b in books:
        CreateBookFrame(parent, b[1:4])


def CreateBookFrame(parent, Values):
    title = Values[0]
    language = Values[1]
    description = Values[2]

    colorcode = {
        'None': 'red',
        'Spanish': 'orange',
        'Russian': 'blue'
    }
    
    BookFrame = Frame(parent, bg='white', width=200, height=300)
    BookFrame.pack_propagate(False)

    Title = Label(BookFrame, text=title)
    Title.pack(anchor='n', pady=5)
    LangFrame = Frame(BookFrame, bg=colorcode[language], width=180, height=90, cursor='hand2')
    LangFrame.pack()
    Label(BookFrame, text=description, wraplength=180).pack(pady=5)
    
    BookFrame.pack(side="left", anchor="n", padx=(20,0), pady=(20,0))


def AddBook(parent, ValueList):
    """UI Stuff when new book is added"""
    if ValueList == None: # Guard against empty input
        print('Title is empty')
        return None

    # Create Visual of book frame
    CreateBookFrame(parent, ValueList)

    # Book Frame db entry
    c.execute("""
        INSERT INTO books (name, language, description) VALUES (?, ?, ?)
        """, (ValueList))
    conn.commit()

    # Confirm code run
    print("Book added!")







#print(c.fetchone())
#print(c.fetchmany(5))
#c.fetchall()
