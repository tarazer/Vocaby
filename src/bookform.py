from tkinter import *
import logic

class BookForm(Frame):
    """Form for creating new books. Pops up when 
    The add book button is clicked"""

    def __init__(self, parent, pagemanager, bookbox):
        super().__init__(parent)
        self.pm = pagemanager
        self.bb = bookbox

        self.config(height=500, bg="green")
        self.pack_propagate(False)

        self.TitleFrame = Frame(self, bg="yellow")
        self.ContentFrame = Frame(self, bg="orange")

        self._make_title()

        self._make_name_entry()
        self._make_description_entry()
        self._make_dropdown()

        self._make_cancel_button()
        self._make_create_button()
        
        self._make_frames()
    

    def _make_title(self):
        Label(self.TitleFrame, 
            text='CREATE NEW BOOK', 
            font=('Helvetica', 24), 
            pady=20,
            ).pack()


    def _make_name_entry(self):
        self.name = Entry(self.ContentFrame, 
            width=20, 
            font=('Helvetica', 18)
            )
        self.name.place(x=10, rely=0.1, anchor='nw')


    def _make_description_entry(self):
        self.Description = Text(self.ContentFrame,
            font=('Helevetica', 12),)
        self.Description.place(relx=0.5, 
            rely=0.5, 
            anchor=CENTER, 
            relwidth=1, 
            width=-20, 
            relheight=0.5,)


    def _make_dropdown(self):
        dropdown_options = {'None': 'no', 'Spanish':'sp', 'Russian': 'rus'}
        self.language_var = StringVar()
        self.language_var.set("None") # default
        dropdown = OptionMenu(self.ContentFrame, 
            self.language_var, 
            *dropdown_options.keys(),)
            
        dropdown.place(relx=1, rely=0.1, anchor='ne', x=-10)

        dropdown.config(font=("Helvetica", 14))
        dropdown["menu"].config(font=("Helvetica", 14)) 


    def _make_cancel_button(self):
        CancelBtn = Button(self.ContentFrame,
            text='Cancel',
            height=2,
            width=8,
            command=self.clear_form,
            ).place(anchor='sw', rely=1, x=10, y=-10)

    
    def _make_create_button(self):
        CreateBtn = Button(self.ContentFrame,
            text='Create',
            height=2,
            width=8,
            command=lambda:self.bb.addBook(self.get_values()),
            ).place(anchor='se', rely=1, relx=1, x=-10, y=-10)


    def _make_frames(self):
        self.TitleFrame.pack(fill='x')
        self.ContentFrame.pack(fill='both', expand=True)


    def get_values(self):
        name = self.name.get()
        language = self.language_var.get()
        description = self.Description.get('1.0', 'end-1c')

        if name == '':
            return None

        self.clear_form()

        return [name, language, description]


    def clear_form(self):
        self.pm.hide_page('bookform')
        self.name.delete(0, END)
        self.Description.delete('1.0', END)
        self.language_var.set('None')
