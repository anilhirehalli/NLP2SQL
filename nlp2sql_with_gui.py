#!/usr/bin/python3
import tkinter.filedialog
from tkinter import *
from tkinter.messagebox import *

from nlp2sql import NLP2sql
from speech import audio

class App:
    def __init__(self, root):
        root.title('NLP2SQL')
        root.bind('<Return>', self.parse)

        self.sentence_frame = LabelFrame(root, text="Input Sentence", padx=7, pady=7)#5,5
        self.sentence_frame.pack(fill="both", expand="yes", padx=12, pady=7)#10,5
        self.text_path_label = "No SQL dump selected..."
        self.input_sentence_string = StringVar()
        self.input_sentence_string.set("Enter a sentence...")
        self.input_sentence_entry = Entry(self.sentence_frame, textvariable=self.input_sentence_string, width=50)#50
        self.input_sentence_entry.pack()
        '''self.load_language_button = Button(self.sentence_frame, text="Speak",command=self.speechTotext, width=20)
        self.load_language_button.pack(side="right")
        self.load_import_button = Button(self.sentence_frame, text="import",command=self.import_text, width=20)
        self.load_import_button.pack(side="left")'''
        #self.input_sentence_entry.bind('<Button-1>', self.clearEntry)

        self.database_frame = LabelFrame(root, text="Database Selection", padx=7, pady=7)
        
        self.database_frame.pack(fill="both", expand="yes", padx=12, pady=7)

        self.database_path_label = Label(self.database_frame, text="No SQL dump selected...")
        self.database_path_label.pack(side="left")
        
        self.load_database_button = Button(self.database_frame, text="Check the connection", command=self.find_sql_file,
                                           width=30)
        #print("self.database_frame : "+ str(self.database_frame))
        self.load_database_button.pack(side="right")

        self.language_frame = LabelFrame(root, text="Language Configuration Selection", padx=5, pady=5)
        self.language_frame.pack(fill="both", expand="yes", padx=12, pady=7)

        self.language_path_label = Label(self.language_frame, text="No configuration file selected...")
        self.language_path_label.pack(side="left")

        self.load_language_button = Button(self.language_frame, text="Check configuration file",
                                           command=self.find_csv_file, width=30)
        self.load_language_button.pack(side="right")

        '''self.thesaurus_frame = LabelFrame(root, text="Import your personal thesaurus ?", padx=7, pady=7)
        self.thesaurus_frame.pack(fill="both", expand="yes", padx=12, pady=7)

        self.thesaurus_path_label = Label(self.thesaurus_frame, text="No thesaurus selected...")
        self.thesaurus_path_label.pack(side="left")

        self.load_thesaurus_button = Button(self.thesaurus_frame, text="Choose a thesaurus file",
                                            command=self.find_thesaurus_file, width=20)
        self.load_thesaurus_button.pack(side="right")'''

        self.go_button = Button(root, text="Go!", command=self.lanch_parsing)
        self.go_button.pack(side="right", fill="both", expand="yes", padx=10, pady=2)

        self.reset_button = Button(root, text="Reset", fg="red", command=self.reset_window)
        self.reset_button.pack(side="right", fill="both", expand="yes", padx=10, pady=2)

    #def clearEntry(self, event):
        #self.input_sentence_string.set("")

    def parse(self, event):
        self.lanch_parsing()

    def find_sql_file(self):
        #filename = tkinter.filedialog.askopenfilename(title="Select a SQL file",filetypes=[('sql files', '.sql'), ('all files', '.*')])
        #print(filename)
        self.database_path_label["text"] = "/home/anilhirehalli/nlp2sql_1/nlp2sql/database_store/school.sql"
        

    #def find_thesaurus_file(self):
        #return 0
        #filename = tkinter.filedialog.askopenfilename(title="Select a thesaurus file",filetypes=[('thesaurus files', '.dat'), ('all files', '.*')])
        #self.thesaurus_path_label["text"] = "NULL"

    def find_csv_file(self):
        #filename = tkinter.filedialog.askopenfilename(title="Select a language configuration file",filetypes=[('csv files', '.csv'), ('all files', '.*')])
        self.language_path_label["text"] = "/home/anilhirehalli/nlp2sql_1/nlp2sql/lang_store/english.csv"

    def reset_window(self):
        self.database_path_label["text"] = "No SQL dump selected..."
        #self.thesaurus_path_label["text"] = "No thesaurus selected..."
        self.input_sentence_string.set("Enter a sentence...")
        self.language_path_label["text"] = "No configuration file selected..."
        return
    def speechTotext(self):
        b= audio()
    
    def  import_text(self):   
        c=audio.send_sentence(self)
            
        print("main "+str(c))
                
        
        return
    

    def lanch_parsing(self):
        try:
            '''thesaurus_path = None

            if str(self.thesaurus_path_label["text"]) != "No thesaurus selected...":
                thesaurus_path = str(self.thesaurus_path_label["text"])'''

            if (str(self.database_path_label["text"]) != "No SQL dump selected...") and (
                        str(self.language_path_label["text"]) != "No configuration file selected...") and (
                        str(self.input_sentence_string.get()) != "Enter a sentence..."):
                NLP2sql(self.database_path_label["text"],
                       self.language_path_label["text"], #thesaurus_path=thesaurus_path,
                       json_output_path='./output.json').get_query(self.input_sentence_string.get())
                #showinfo('Result', 'Parsing done!')
        
                
            else:
                showwarning('Warning', 'You must fill in all fields, please.')
        except Exception as e:
            showwarning('Error', e)
        return


root = Tk()
App(root)
root.resizable(width=FALSE, height=FALSE)
root.mainloop()
