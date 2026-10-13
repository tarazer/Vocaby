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


    def show_page(self, page):
        self.pages[page].tkraise()
            

    def hide_page(self, page):
        self.pages[page].lower()


    def openList(self, id):
        pass



class Database():
    """sqlite database"""
    def __init__(self):
        self.conn = sqlite3.connect("books.db")
        self.c = self.conn.cursor()

        #Create Table for books and words
        self.c.execute("""
            CREATE TABLE IF NOT EXISTS books (
                name text,
                language text,
                description text
            )""")

        self.c.execute("""
            CREATE TABLE IF NOT EXISTS words (
                word text,
                translation text,
                description text,
                book_id INTEGER,
                FOREIGN KEY (book_id) REFERENCES books(rowid)
                    ON DELETE CASCADE
                    ON UPDATE CASCADE
            )""")
        
        self.conn.commit()

        # For Book Display
        self.removed_book_ids = []
        self.c.execute("SELECT rowid,* FROM books")      
        self.book_values = self.c.fetchall()


    def insert_new_book(self, valueList):
        self.c.execute("""
            INSERT INTO books (name, language, description) VALUES (?, ?, ?)
            """, (valueList))
        self.conn.commit()


    def delete_removed_books(self):
        for id in self.removed_book_ids:
            self.c.execute("""DELETE FROM books WHERE rowid=(?)""", (id,))
            self.conn.commit()
