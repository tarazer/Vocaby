from tkinter import *

from taskbar import Taskbar
from bookform import BookForm
from bookdisplay import BookDisplay
from wordform import WordForm
from wordpage import WordPage
import logic

# Initialize Tkinter, create Window and init managers
window = Tk()
window.geometry('800x400')
pagemanager = logic.PageManager()
db = logic.Database()


# Creating Main Pages
HomePage = Frame(window)
pagemanager.addPage('home', HomePage)

ListPage = Frame(window)
pagemanager.addPage('list', ListPage)

for page in (HomePage, ListPage):
    page.place(x=0, y=0, relwidth=1, relheight=1)


# HomePage & ListPage Widgets
bar = Taskbar(HomePage, pagemanager).pack(fill='x')
HomeContent = Frame(HomePage, bg="purple")
HomeContent.pack(fill='both', expand=True)

wordpage = WordPage(ListPage, pagemanager, db)
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
#pagemanager.hide_page('wordform') # hide word form
pagemanager.show_page('home')

window.mainloop()

db.conn.close()
