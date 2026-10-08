from tkinter import *

from taskbar import Taskbar
from bookform import BookForm
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
HomeContent = Frame(HomePage, bg="purple")
ListPage = Frame(container)

for page in (HomePage, ListPage):
    page.place(x=0, y=0, relwidth=1, relheight=1)

books = logic.BookBox(HomeContent, pagemanager, db)
books.place(relwidth=1, 
    relheight=1,
    width=-40,
    y=20,
    anchor='center',
    rely=0.5,
    relx=0.5,
    )
#books.bind("<Configure>", books.loadBooks)


Bookform = BookForm(window, pagemanager, books)
Bookform.place(relx=0.5, rely=0.5, anchor=CENTER, relwidth=0.5)



# Populate Page/Form Manager
pagemanager.addPage('home', HomePage)
pagemanager.addPage('homeC', HomeContent)
pagemanager.addPage('bookform', Bookform)
pagemanager.addPage('list', ListPage)


# HomePage Widgets
bar = Taskbar(HomePage, pagemanager).pack(fill='x')
Label(HomeContent, 
    text='Home Page', 
    font=('Arial', 24)
    ).place(relx=0.5, rely=0.5, anchor=CENTER)
HomeContent.pack(fill='both', expand=True)
# ListPage Widgets
Label(ListPage, 
    text='Page 2', 
    font=('Arial', 24)
    ).place(relx=0.5, rely=0.5, anchor=CENTER)


# Make window update after resize
#window.bind("<Configure>", ???)


# Load saved books from DB
books.loadBooks()


# Show home page and start main loop
pagemanager.show_page('home')
window.mainloop()

db.conn.close()

