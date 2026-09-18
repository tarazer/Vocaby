from tkinter import *
import sqlite3

from taskbar import Taskbar

def show_page(page):
    page.tkraise()

# Initialize Tkinter and create Window
window = Tk()
window.geometry('800x400')

# Create the container for all Pages, those being Home Page, List Page
container = Frame(window)
container.pack(fill="both", expand=True)

# Creating all accesible Pages to seperate content
HomePage = Frame(container)
ListPage = Frame(container)
for page in (HomePage, ListPage):
    page.place(x=0, y=0, relwidth=1, relheight=1)


# 
bar = Taskbar(HomePage).pack(fill='x')
HomeContent = Frame(HomePage, bg="purple")
HomeContent.pack(fill='both', expand=True)

Label(HomeContent, text='Home Page', font=('Arial', 24)).place(relx=0.5, rely=0.5, anchor=CENTER)
Label(ListPage, text='Page 2', font=('Arial', 24)).place(relx=0.5, rely=0.5, anchor=CENTER)



# Show home page and start main loop
show_page(HomePage)
window.mainloop()


