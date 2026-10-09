from tkinter import *
import logic

class Taskbar(Frame):
    """The Taskbar class, has the functions and widgets for the Main page taskbar"""
    def __init__(self, parent, pagemanager):
        super().__init__(parent, bg='#707070', height=90)
        self.pm = pagemanager
        self.pack_propagate(False)

        # Frames for UI Elemets left and right
        self.left_frame = Frame(self)
        self.right_frame = Frame(self)
        
        self._make_labels()
        self._addbook_btn()
        self._make_frames()
        
        
    def _make_labels(self):
        """Create and Initiate all Labels"""
        pass


    def _addbook_btn(self):
        AddBook_Btn = Button(self.right_frame, 
            text='Add Book',
            width=10, height=3,
            command=lambda: self.pm.show_page('bookform'))

        AddBook_Btn.pack(side='left', fill='y', padx=(5,20))

      
    def _make_frames(self):
        """Style previously created Frames for task bar"""
        
        self.left_frame.config(bg="lightblue")
        self.left_frame.pack(side=LEFT)

        self.right_frame.config(bg="lightgreen")
        self.right_frame.pack(side=RIGHT)        
