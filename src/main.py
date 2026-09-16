from tkinter import *

bg_color = "#ffff33"

window = Tk() # Creates a Window
window.config(bg=bg_color)
window.geometry("800x400")

photo = PhotoImage(file='assets/Helvetica.png')

label = Label(window, 
            text='Text i guess', 
            font=('Arial', 50, 'italic'), 
            bg=bg_color,
            relief=SOLID,
            bd=10,
            padx=50,
            image=photo,
            compound="bottom")

label.place(x=20,y=30)


window.mainloop() # Displays Window and listens for events
