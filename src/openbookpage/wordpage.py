from tkinter import *
from .wordentry import WordEntry
from .word_editor import WordEditorForm


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

        self.current_words = {}
        self.current_id = id
        self.current_inspected_word = None

        
    def load(self, id):
        self.current_id = id
        self._load_words()


    def _load_words(self):
        word_values = self.db.get_words_by_id(self.current_id)

        for word in word_values:
            wordentry = WordEntry(self, word[1], word[2])
            wordentry.place_self()

            self.current_words[wordentry] = word[0]
            wordentry.bind('<Button-1>', self.edit_word)
        

    def add_word(self, values):
        word =          values[0]
        translation =   values[1]
        book_id =       self.current_id

        self.db.insert_new_values('words', [word, translation, book_id])

        wordentry = WordEntry(self, word, translation)
        wordentry.place_self()
        self.current_words[wordentry] = self.db.get_newest_entry('words')[0]
        wordentry.bind('<Button-1>', self.edit_word)


    def clear_page(self):
        self.pm.hide_page('list')
        self.pm.hide_page('editwordform')
        self.wef.place_forget()
        for word in self.current_words:
            word.destroy()

        self.db.delete_removed_words()
        self.current_words.clear()


    def edit_word(self, event):
        w = event.widget
        self.wef.place(x=w.winfo_x(), y=w.winfo_y(),relwidth=1, height=40)
        self.pm.show_page('editwordform')

        self.current_inspected_word = w

        self.wef.clear_entries()
        self.wef.word.insert(0, w.word.cget('text'))
        self.wef.translation.insert(0, w.translation.cget('text'))

        # Bind key to canceling and enter to confirming and unbind after shi is done


    def delete_word(self):
        w = self.current_inspected_word
        if w != None:
            self.db.removed_word_ids.append(self.current_words[w])
            self.wef.clear_entries()
            self.wef.place_forget()
            w.destroy()


    def place_self(self):
        self.place(
            relx=0.5, 
            rely=1, 
            anchor='s', 
            relwidth=0.6, 
            relheight=1,
            height=-70)
