import sqlite3
from tkinter import *


class PageManager:
    """Manage windows and forms"""
    def __init__(self):
        self.pages = {}
        

    def addPage(self, key, value):
        self.pages[key] = value


    def show_page(self, page):
        self.pages[page].tkraise()

    def hide_page(self, page):
        self.pages[page].lower()


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


    def insert_new_values(self, table, values):
        query = f"INSERT INTO {table} VALUES (?, ?, ?)"
        self.c.execute(query, (values))
        self.conn.commit()    


    def update_values_by_id(self, table, values, id):
        query = f"UPDATE {table} SET word=(?), translation=(?)  WHERE rowid={id}"
        self.c.execute(query, (values))
        self.conn.commit()


    def delete_removed_books(self):
        for id in self.removed_book_ids:
            self.c.execute("""DELETE FROM books WHERE rowid=(?)""", (id,))
            self.conn.commit()


    def delete_id_from_table(self, table, id):
        query = f"DELETE FROM {table} WHERE rowid=(?)"
        self.c.execute(query, (id,))
        self.conn.commit()


    def get_book_by_id(self, id):
        self.c.execute("""SELECT rowid,* FROM books WHERE rowid=(?)""", (id,))
        return self.c.fetchone()


    def get_words_by_id(self, id):
        self.c.execute("""
                            SELECT rowid,* 
                            FROM words 
                            WHERE book_id=(?)""", (id,))

        return self.c.fetchall()


    def get_newest_entry(self, table):
        query = f"""    
                    SELECT rowid,* 
                    FROM {table} 
                    WHERE rowid = (SELECT MAX(rowid) FROM {table})
                    """
        self.c.execute(query)
        
        return self.c.fetchone()
