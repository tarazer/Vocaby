from tkinter import *

class Taskbar(Frame):
    """The Taskbar class, has the functions and widgets for the Main page taskbar"""
    def __init__(self, parent):
        super().__init__(parent)

        self.bg_color = '#707070'
        self.height = 90
        self.config(bg=self.bg_color, height=self.height)

        self._make_frames()
        self._make_labels()
        self._make_buttons()


    def _make_labels(self):
        """Initiate all Labels"""
        Label(self, 
            text='TASKBAR', 
            bg=self.bg_color,
            font=('Arial', 24),
        ).place(rely=0.5, relx=0.5, anchor='center')


    def _make_buttons(self):
        """Initiate all Buttons"""

        pass


    def _make_frames(self):
        """Make Frames for task bar"""
        frame_height_multiplier = 0.75
        offset = (self.height - self.height * frame_height_multiplier) / 2
        
        self.left_frame = Frame(self, bg="lightblue", width=100).place(
                                                        x=offset,
                                                        y=offset,
                                                        relheight=frame_height_multiplier)

        right_frame = Frame(self, bg="lightgreen", width=100, padx=offset).place(y=offset, relx=1, x=-offset, anchor='ne', relheight=frame_height_multiplier)
        
