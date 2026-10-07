from tkinter import *
import logic

class BookForm(Frame):
    """Form for creating new books. Pops up when 
    The add book button is clicked"""

    def __init__(self, parent, pagemanager):
        super().__init__(parent)
        self.pm = pagemanager

        self.config(height=500, bg="green")
        self.pack_propagate(False)

        self.TitleFrame = Frame(self, bg="yellow")
        self.ContentFrame = Frame(self, bg="orange")

        self._make_labels()
        self._make_text()
        self._make_buttons()
        self._make_frames()
    

    def _make_labels(self):
        Label(self.TitleFrame, 
            text='CREATE NEW BOOK', 
            font=('Helvetica', 24), 
            pady=20,
            ).pack()


    def _make_buttons(self):
        CancelBtn = Button(self.ContentFrame,
            text='Cancel',
            height=2,
            width=8,
            command=lambda:self.pm.hide_page('bookform'),
            ).place(anchor='sw', rely=1, x=10, y=-10)

        CreateBtn = Button(self.ContentFrame,
            text='Create',
            height=2,
            width=8,
            command=lambda:logic.AddBook(self.pm.pages['homeC'], self.get_values()),
            ).place(anchor='se', rely=1, relx=1, x=-10, y=-10)

        dropdown_options = ['None', 'Spanish', 'Russian']
        var = StringVar()
        var.set("None") # default
        dropdown = OptionMenu(self.ContentFrame, 
            var, 
            *dropdown_options,
            )
        dropdown.place(relx=1, rely=0.1, anchor='e', x=-10)
        dropdown.config(font=("Helvetica", 14))
        dropdown["menu"].config(font=("Helvetica", 14)) 
            

    def _make_text(self):
        self.Title = Entry(self.ContentFrame, 
            width=10, 
            font=('Helvetica', 18)
            )
        self.Title.place(relx=0.5, rely=0.1, anchor=CENTER, relwidth=0.5)

        self.Description = Text(self.ContentFrame,
            font=('Helevetica', 12),
            )
        self.Description.place(relx=0.5, rely=0.5, anchor=CENTER, relwidth=1, width=-20, relheight=0.5,)


    def _make_frames(self):
        self.TitleFrame.pack(fill='x')
        self.ContentFrame.pack(fill='both', expand=True)


    def get_values(self):
        title = self.Title.get()
        description = self.Description.get('1.0', 'end-1c')

        if title == '':
            return None
        print(len(title))
        return [title, description]
