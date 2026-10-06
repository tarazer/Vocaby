import sqlite3
from tkinter import *

def show_page(page):
    page.tkraise()





# DB Stuff
conn = sqlite3.connect("books.db")
c = conn.cursor()

#Create Table
c.execute("""
    CREATE TABLE IF NOT EXISTS books (
        id INTEGER PRIMARY KEY,
        name text,
        language text
    )""")

conn.commit()


def AddBook(parent, name_param, language_param):
    """UI Stuff when new book is added"""
    # Create Visual of book frame
    BookFrame = Frame(parent, bg="red", width=200, height=300)
    BookFrame.pack(side="left", anchor="n", padx=(20,0), pady=(20,0))

    # Book Frame db entry
    c.execute("""
        INSERT INTO books (name, language) VALUES (?, ?)
        """, (name_param, language_param))
    conn.commit()

    # Confirm code run
    print("Book added!")


c.execute("SELECT * FROM books")
#print(c.fetchone())
print(c.fetchmany(5))
#c.fetchall()
