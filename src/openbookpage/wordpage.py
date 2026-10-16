from tkinter import *
from .wordentry import WordEntry
from .word_editor import WordEditorForm
import math


class WordPage(Frame):
    """The Frame that holds the actual words and 
    translations for books of the Home Page. 
    Is managed by openbook ui"""

    def __init__(self, parent, pagemanager, database):
        super().__init__(parent, bg='grey')
        self.parent = parent
        self.pm = pagemanager
        self.db = database

        self.wef = WordEditorForm(self)
        pagemanager.addPage('editwordform', self.wef)

        self.word_values = []
        self.word_entries = []
        self.current_id = None
        self.current_inspected_word = None
        self.current_page = 1

        self.rows = 0


    def make_entries(self):
        rows = self.winfo_height() // 40 - 2
        
        if rows > self.rows: # More rows then previously
            for _ in range(rows-self.rows):
                wordentry = WordEntry(self)
                wordentry.place_self()
                self.word_entries.append(wordentry)
                wordentry.bind('<Button-1>', self.edit_word)

        elif rows < self.rows: # less rows then previously
            for _ in range(self.rows - rows):
                we = self.word_entries.pop()
                we.clear()
                we.destroy()

        self.rows = rows


    def calc_page(self):
        pages = math.ceil(len(self.word_values) / self.rows)
        if pages <= 0:
            pages = 1

        self.pages = pages


    def load(self, id):
        self.current_id = id
        self.word_values = self.db.get_words_by_id(self.current_id)

        self.make_entries()
        self.calc_page()
        self._insert_words()


    def _insert_words(self):
        rows = self.rows
        page = self.current_page
    
        values = self.word_values[(page-1) * rows:page * rows]

        for index, we in enumerate(self.word_entries[0:len(values)]): 
            # len is fail save if values is smaller than ammount of rows, 
            # otherwise index error
            we.insert_labels(values[index])


    def clear_page(self):
        self.pm.hide_page('list')
        self.pm.hide_page('editwordform')
        self.wef.place_forget()

        for we in self.word_entries:
            we.clear()

        self.current_page = 1





            
    def add_word(self, values):
        word =          values[0]
        translation =   values[1]
        book_id =       self.current_id

        self.db.insert_new_values('words', [word, translation, book_id])
        self.word_values.append(self.db.get_newest_entry('words'))
        self.load(self.current_id)


    def edit_word(self, event):
        w = event.widget
        self.wef.place(x=w.winfo_x(), y=w.winfo_y(),relwidth=1, height=40)
        self.pm.show_page('editwordform')

        self.current_inspected_word = w

        self.wef.clear_entries()
        self.wef.word.insert(0, w.word.cget('text'))
        self.wef.translation.insert(0, w.translation.cget('text'))

        self.wef.bind_all('<Return>', self.confirm)
        # Bind key to canceling and enter to confirming and unbind after shi is done


    def delete_word(self):
        w = self.current_inspected_word
        if w != None:
            self.db.delete_id_from_table('words', w.id)
            w.clear()            
            self.wef.clear_entries()
            self.wef.place_forget()
            self.load(self.current_id)

        self.current_inspected_word = None


    def confirm(self, event):
        w = self.current_inspected_word

        word = self.wef.word.get()
        translation = self.wef.translation.get()

        values = [w.id, word, translation, w.book_id]
        w.insert_labels(values)
        self.db.update_values_by_id('words', [word, translation], w.id)
        print('triggered')


    def place_self(self):
        self.place(
            relx=0.5, 
            rely=1, 
            anchor='s', 
            relwidth=0.6, 
            relheight=1,
            height=-70)
