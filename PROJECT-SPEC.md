Vocaby

1.OVERVIEW
Vocaby is a small lightweight python desktop app. It allows the User to create Vocabulary Lists 
for languages of their choosing. These entries are made entirely by the user and have fields such as word,
translation and description. It also allows for getting a randomized list of vocabulary to practice on.
The app makes it easier for people learning a language to keep track of words they learned and to 
quickly repeat them.


2.FEATURES
User should be able to:
 - Create Language Books which the word lists are in
 - Word entry lists are seperated into multiple pages to make looking at them easier and more visually appealing
 - The Entries inside the List will be sorted alphabetically
 - A random list of entries from a specific time range and a chosen amount of them can be aquired to practice translation
 - When a language with a different writing system is used, phonetic writting can be used, though this has to be scripted 
   for each language seperately. For now only Russian and Spanish are planned


3.UI
 - A loading splashscreen for when the app opens
 - The main page has a task bar at the top with a username, the number of learned words learned and amount of language books. 
   There also is a NEW BOOK button for creating a new language book
 - Under the main page task bar there is a plain area where icons of books with flags on them are displayed. Clicking those 
   brings you to the corresponding languages word list
 - 

4.TECHNICAL REQURIEMENTS
The app will be written in python using the tkinter library. A sqlite3 database will store 
the Word lists locally. There will not be the option to create a account and if the app 
database is deleted the Word list will be lost
