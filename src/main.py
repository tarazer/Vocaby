from tkinter import *

from homepage.taskbar import Taskbar
from homepage.bookform import BookForm
from homepage.bookdisplay import BookDisplay

from openbookpage.wordform import WordForm
from openbookpage.wordpage import WordPage
from openbookpage.openbook_ui import UI_OpenBook

import logic
from platformdirs import user_data_path



DATA_DIR = user_data_path("VocabApp")
DATA_DIR.mkdir(parents=True, exist_ok=True)
DB_PATH = DATA_DIR / "vocaby.db"


def on_resize(event):
    """Runs after window has been resized 
    and then calls - to update layout"""
    if hasattr(window, 'after_id') and window.after_id is not None:
        window.after_cancel(window.after_id)
    
    window.after_id = window.after(50, UpdateLayout)

def UpdateLayout():
    book_display.load_books()


# Initialize Tkinter, create Window and init managers
window = Tk()
window.geometry('800x400')
pagemanager = logic.PageManager()
db = logic.Database(DB_PATH)


# Creating Main Pages
HomePage = Frame(window)
pagemanager.addPage('home', HomePage)
HomePage.place(x=0, y=0, relwidth=1, relheight=1)

OpenBookPage = Frame(window)
pagemanager.addPage('list', OpenBookPage)
OpenBookPage.place(x=0, y=0, relwidth=1, relheight=1)


# HomePage Widgets
taskbar = Taskbar(HomePage, pagemanager).pack(fill='x')
HomeContent = Frame(HomePage, bg="purple")
HomeContent.pack(fill='both', expand=True)

# OpenWordpage Widgets
wordpage = WordPage(OpenBookPage, pagemanager, db)
wordpage.place_self()

book_display = BookDisplay(HomeContent, pagemanager, db, wordpage)
book_display.place_self()


# Create Forms
book_creation_form = BookForm(window, pagemanager, book_display)
book_creation_form.place(relx=0.5, rely=0.5, anchor=CENTER, relwidth=0.5)
pagemanager.addPage('bookform', book_creation_form)

word_creation_form = WordForm(wordpage, pagemanager, db)
word_creation_form.place_self()
pagemanager.addPage('wordform', word_creation_form)


# Prepare for app start and start main loop
book_display.load_books()
book_display.bind('<Configure>', on_resize)
pagemanager.show_page('home')

window.mainloop()

# Clean up after app closed
db.delete_removed_books()
db.conn.close()
