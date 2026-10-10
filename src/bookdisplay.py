from tkinter import *


class BookDisplay(Frame):
    """Box that holds and manages all Books 
    in Homecontent on Homepage"""

    def __init__(self, parent, pagemanager, database, wordpage):
        super().__init__(parent)
        self.pm = pagemanager
        self.db = database
        self.wp = wordpage

        self.books = {}

        self.config(bg='lime',)


    def addBook(self, valueList):
        """UI Stuff when new book is added"""
        if valueList == None: # Guard against empty input
            print('Title is empty')
            return None

        # Book Frame db entry and creating visual of book frame        
        self.db.c.execute("""
            INSERT INTO books (name, language, description) VALUES (?, ?, ?)
            """, (valueList))
        self.db.conn.commit()

        self.db.c.execute("SELECT rowid,* FROM books WHERE rowid = (SELECT MAX(rowid) FROM books)")
        FullList = self.db.c.fetchone()
        self.place_book(FullList)
        

    def place_book(self, values):
        id =            values[0]
        title =         values[1]
        language =      values[2]
        description =   values[3]

        colorcode = {'None': 'red','Spanish': 'orange','Russian': 'blue'}

        book_frame = Frame(self, bg='white', width=200, height=300, cursor='hand2')
        book_frame.pack_propagate(False)

        # Child Wigets of book_frame
        Label(book_frame, text=title, width=22).pack(pady=(5,0))
        LangFrame = Frame(book_frame, bg=colorcode[language], width=180, height=90).pack(pady=(5,0))
        Label(book_frame, text=description, width=22, wraplength=170).pack(pady=(5,0))

        # Place Bookframe and assign itself as key to a id value
        book_frame.pack(side=LEFT, anchor='n', padx=(0, 20))   
        self.books[book_frame] = id

        # Bind openBook to frame and all its children so wherever clicked, it triggers
        book_frame.bind('<Button-1>', self.openBook)
        for child in book_frame.winfo_children():
            child.bind('<Button-1>', self.openBook)


    def openBook(self, event):
        try:
            id = self.books[event.widget]
        except:
            id = self.books[event.widget.master]
        self.pm.show_page('list')
        self.wp.load(id)
        


    def load_books(self):
        self.db.c.execute("SELECT rowid,* FROM books")
        book_values = self.db.c.fetchall()

        for values in book_values:
            self.place_book(values)


    def place_self(self):
        self.place(relwidth=1, 
            relheight=1,
            width=-40,
            y=20,
            anchor='center',
            rely=0.5,
            relx=0.5,)
