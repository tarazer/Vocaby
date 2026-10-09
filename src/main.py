from tkinter import *

from taskbar import Taskbar
from bookform import BookForm
from bookpage import BookPage
import logic

# Initialize Tkinter, create Window and init managers
window = Tk()
window.geometry('800x400')
pagemanager = logic.PageManager()
db = logic.Database()


# Create the container for all Pages, those being Home Page, List Page
container = Frame(window).pack(fill="both", expand=True)


# Creating all accesible Pages and Forms
HomePage = Frame(container)
pagemanager.addPage('home', HomePage)

HomeContent = Frame(HomePage, bg="purple")
pagemanager.addPage('homeC', HomeContent)

ListPage = Frame(container)
pagemanager.addPage('list', ListPage)

bookp = BookPage(ListPage, pagemanager, db)
bookp.place(relx=0.5, rely=0.5, anchor=CENTER, relwidth=0.5, relheight=1)

for page in (HomePage, ListPage):
    page.place(x=0, y=0, relwidth=1, relheight=1)

books = logic.BookBox(HomeContent, pagemanager, db, bookp)
books.place(relwidth=1, 
    relheight=1,
    width=-40,
    y=20,
    anchor='center',
    rely=0.5,
    relx=0.5,
    )

Bookform = BookForm(window, pagemanager, books)
Bookform.place(relx=0.5, rely=0.5, anchor=CENTER, relwidth=0.5)
pagemanager.addPage('bookform', Bookform)


# HomePage & ListPage Widgets
bar = Taskbar(HomePage, pagemanager).pack(fill='x')
HomeContent.pack(fill='both', expand=True)


# Make window update after resize
#window.bind("<Configure>", ???)


# Load saved books from DB
books.loadBooks()


# Show home page and start main loop
pagemanager.show_page('home')
window.mainloop()

db.conn.close()
