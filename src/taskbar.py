from tkinter import *
import logic

class Taskbar(Frame):
    """The Taskbar class, has the functions and widgets for the Main page taskbar"""
    def __init__(self, parent, pagemanager):
        super().__init__(parent)
        self.pm = pagemanager

        self.bg_color = '#707070'
        self.height = 90
        self.config(bg=self.bg_color, height=self.height)

        # Frames for UI Elemets left and right
        self.left_frame = Frame(self)
        self.right_frame = Frame(self)
        
        self._make_labels()
        self._make_buttons()
        self._make_frames()
        
        
    def _make_labels(self):
        """Create and Initiate all Labels"""
        Label(self, 
            text='TASKBAR', 
            bg=self.bg_color,
            font=('Arial', 24),
        ).place(rely=0.5, relx=0.5, anchor='center')


    def _make_buttons(self):
        """Create and Initiate all Buttons"""
        AddBook_Btn = Button(self.right_frame, 
            text='Add Book', 
            command=lambda: self.pm.show_page('bookform')
            )

        for btn in [AddBook_Btn]:
            btn.config(width=10)
            btn.pack(side='left', fill='y', padx=(5,0))

      
    def _make_frames(self):
        """Style previously created Frames for task bar"""
        # Creation and styling is seperated, since if i place 
        # it while creating im unable to add widgets into it
        frame_height_multiplier = 0.75
        offset = (self.height - self.height * frame_height_multiplier) / 2
        
        self.left_frame.config(bg="lightblue")
        self.left_frame.place(
                            x=offset,
                            y=offset,
                            relheight=frame_height_multiplier)

        self.right_frame.config(bg="lightgreen")
        self.right_frame.place(y=offset, relx=1, x=-offset, anchor='ne', relheight=frame_height_multiplier)

