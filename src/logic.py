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
#c.execute("""DROP TABLE books""")
c.execute("""
    CREATE TABLE IF NOT EXISTS books (
        id INTEGER PRIMARY KEY,
        name text,
        language text,
        description text
    )""")

conn.commit()


def AddBook(parent, ValueList):
    """UI Stuff when new book is added"""
    if ValueList == None: # Guard against empty input
        print('Title is empty')
        return None

    # Create Visual of book frame
    BookFrame = Frame(parent, bg="red", width=200, height=300)
    BookFrame.pack(side="left", anchor="n", padx=(20,0), pady=(20,0))

    # Book Frame db entry
    c.execute("""
        INSERT INTO books (name, language, description) VALUES (?, ?, ?)
        """, (ValueList))
    conn.commit()

    # Confirm code run
    print("Book added!")






c.execute("SELECT * FROM books")
#print(c.fetchone())
print(c.fetchmany(5))
#c.fetchall()
