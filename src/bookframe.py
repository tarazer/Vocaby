from tkinter import *

class BookFrame(Frame):
    """Frame that holds info on Book in UI"""

    def __init__(self, parent, title, language, description):
        super().__init__(parent)
        self.parent = parent
        self.pack_propagate(False)

        self.config(bg='white', width=200, height=300)
        colorcode = {'None': 'red','Spanish': 'orange','Russian': 'blue'}

        # Child Wigets of book_frame
        self._make_title_label(title)
        self._make_language_frame(language, colorcode)
        self._make_description_label(description)
        self._make_delete_button()


    def _make_title_label(self, title):
        title_label = Label(self, 
            text=title, 
            width=22)

        title_label.pack(pady=(5,0))


    def _make_language_frame(self, language, colorcode):
        language_frame = Frame(self, 
            bg=colorcode[language], 
            width=180, 
            height=90, 
            cursor='hand2')
            
        language_frame.pack(pady=(5,0))
        language_frame.bind('<Button-1>', self.parent.openBook)


    def _make_description_label(self, description):
        description_label = Label(self, 
            text=description, 
            width=22, 
            wraplength=170)

        description_label.pack(pady=(5,0))


    def _make_delete_button(self):
        delete_btn = Button(self, 
            text='Delete', 
            command=lambda:self.parent.delete_book(self))

        delete_btn.place(
            anchor='se',
            relx=1,
            rely=1,
            x=-5,
            y=-5
        )


