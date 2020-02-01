import speech_recognition as sr
import tkinter.filedialog
from tkinter import *
from tkinter.messagebox import *
from parsingException import ParsingException

class audio:
    def __init__(self):
        root = Tk()
        root.resizable(width=FALSE, height=FALSE)
        
        root.title('Speech to text')
        root.bind('<Return>', self.parse)
        
        
        
        self.sentence_frame = LabelFrame(root, text="Speech to text", padx=7, pady=7)#5,5
        
        self.sentence_frame.pack(fill="both", expand="yes", padx=12, pady=7)#10,5

        self.input_sentence_string = StringVar()
        self.database_pa_label = Label(self.sentence_frame, text="Say somthing...")
        self.database_pa_label.pack(side="left")
        self.text_frame = LabelFrame(root, text="listening...", padx=7, pady=7)
        
        self.text_frame.pack(fill="both", expand="yes", padx=12, pady=7)

        self.text_path_label = Label(self.text_frame, text="Text area")
        self.text_path_label.pack(side="left")
        # Record Audio
        '''r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Say something!")
            audio = r.listen(source)
         
        # Speech recognition using Google Speech Recognition
        try:
            # for testing purposes, we're just using the default API key
            # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
            # instead of `r.recognize_google(audio)`
            print("You said: " + r.recognize_google(audio))

        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))'''
        
       
       
    

        

        

        self.reset_button = Button(root, text="Close", fg="red", command=root.destroy)
        self.reset_button.pack(side="right", fill="both", expand="yes", padx=10, pady=2)
        #self.reset_button = Button(root, text="select", fg="black", command=self.send_sentence)
        #self.reset_button.pack(side="right", fill="both", expand="yes", padx=10, pady=2)
        self.go_button = Button(root, text="Talk", fg="Black",command=self.lanch_parsing)
        self.go_button.pack(side="right", fill="both", expand="yes", padx=10, pady=2)

    def clearEntry(self, event):
        self.input_sentence_string.set("")

    def parse(self, event):
        self.lanch_parsing()
    def send_sentence(self):
        #print(str(self.text_path_label["text"]))
        if (str(self.text_path_label["text"]) != "No SQL dump selected..."):
            print("here " + str(self.text_path_label["text"]))
            #self.input_sentence_string.set("Anil")
            return str(self.text_path_label["text"])
    def lanch_parsing(self):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            #print("Say something!")
            audio = r.listen(source)
         
        # Speech recognition using Google Speech Recognition
        try:
            # for testing purposes, we're just using the default API key
            # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
            # instead of `r.recognize_google(audio)`
            self.text_path_label["text"]= r.recognize_google(audio)
            print("You said "+ r.recognize_google(audio))

        except sr.UnknownValueError:
            showwarning('Error',"Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
            showwarning('Error',"Could not request results from Google Speech Recognition service; {0}".format(e))
        
        



