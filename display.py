'''from tkinter import *

master = Tk()
query = "select * from student;"
print(query)
master.title('Query')
master.geometry('350x100')
w = Label(master, text="Query"+"\n\n"+query,font="-weight bold")
#w = Label(master, text=query,width=40,height=10)

w.pack()'''
#!/usr/bin/python3
import tkinter.filedialog
from tkinter import *
from tkinter.messagebox import *
import MySQLdb



class App:
    global values 
    def __init__(self,query):
        root = Tk()
        root.resizable(width=FALSE, height=FALSE)
        
        root.title('Query')
        root.bind('<Return>', self.parse)
        global values
        
        values = query
        
        
        self.sentence_frame = LabelFrame(root, text="Query Generated", padx=7, pady=7)#5,5
        
        self.sentence_frame.pack(fill="both", expand="yes", padx=12, pady=7)#10,5

        self.input_sentence_string = StringVar()
        self.database_path_label = Label(self.sentence_frame, text=query)
        self.database_path_label.pack(side="left")
        
       
       
    

        

        

        self.reset_button = Button(root, text="Dont ! Execute", fg="red", command=root.destroy)
        self.reset_button.pack(side="right", fill="both", expand="yes", padx=10, pady=2)
        self.go_button = Button(root, text="Execute", fg="green",command=self.lanch_parsing)
        self.go_button.pack(side="right", fill="both", expand="yes", padx=10, pady=2)

    def clearEntry(self, event):
        self.input_sentence_string.set("")

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

    def lanch_parsing(self):
        try:
            onemore = str(values)
            something=onemore.replace("\n"," ")
            db = MySQLdb.connect(host='localhost', 
                     user='anilhirehalli',            
                     passwd='password',  
                     db='college') 
            cur = db.cursor()
            cur.execute(something)
            for row in cur.fetchall():
                print(row)
            db.close()
            
        except Exception as e:
            print("Coming")
            showwarning('Error', e)
        return


#App("SELECT COUNT(*) FROM student;")


