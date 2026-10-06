from tkinter import *

from taskbar import Taskbar
import logic

# Initialize Tkinter and create Window
window = Tk()
window.geometry('800x400')


# Create the container for all Pages, those being Home Page, List Page
container = Frame(window).pack(fill="both", expand=True)


# Creating all accesible Pages to seperate content
HomePage = Frame(container)
HomeContent = Frame(HomePage, bg="purple")
ListPage = Frame(container)

for page in (HomePage, ListPage):
    page.place(x=0, y=0, relwidth=1, relheight=1)


# HomePage Widgets
bar = Taskbar(HomePage, HomeContent).pack(fill='x')
Label(HomeContent, text='Home Page', font=('Arial', 24)).place(relx=0.5, rely=0.5, anchor=CENTER)
HomeContent.pack(fill='both', expand=True)
# ListPage Widgets
Label(ListPage, text='Page 2', font=('Arial', 24)).place(relx=0.5, rely=0.5, anchor=CENTER)


# Make window update after resize
#window.bind("<Configure>", ???)


# Show home page and start main loop
logic.show_page(HomePage)
window.mainloop()

logic.conn.close()

