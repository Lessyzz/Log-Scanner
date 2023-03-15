import os
from tkinter import filedialog, messagebox
from tkinter import *

class LogScanner:
    def __init__(self):
        self.gui()
    
    def gui(self):
        self.window = Tk()
        self.window.title("Log Scanner")
        self.window.geometry("300x200")
        self.window.configure(background="#e0e2db")
        self.window.resizable(False,False)

        # Choose file button
        self.chooseFileButton = Button(text="Choose file", command=self.entry, bg="#e0e2db", fg="black")
        self.chooseFileButton.pack()
        self.chooseFileButton.place(x=120,y=20)
        self.window.mainloop()

    def entry(self):
        self.filePath = filedialog.askopenfile().name

        # First letter label
        self.firstLetterLabel = Label(self.window, bg="#e0e2db", fg="black", text="First letter:")
        self.firstLetterLabel.pack()
        self.firstLetterLabel.place(x=27,y=68)
        # Last letter label
        self.lastLetterLabel = Label(self.window, bg="#e0e2db", fg="black", text="Last letter:")
        self.lastLetterLabel.pack()
        self.lastLetterLabel.place(x=27,y=98)
        # First letter entry
        self.firstLetterEntry = Entry(self.window, bg="#e0e2db", fg="black", width=25)
        self.firstLetterEntry.pack()
        self.firstLetterEntry.place(x=120,y=70)
        # Last letter entry
        self.lastLetterEntry = Entry(self.window, bg="#e0e2db", fg="black", width=25)
        self.lastLetterEntry.pack()
        self.lastLetterEntry.place(x=120,y=100)
        # Button
        self.SelectFileForSaveButton = Button(text="Select the file to save", command=self.save, bg="#e0e2db", fg="black",width=22)
        self.SelectFileForSaveButton.pack()
        self.SelectFileForSaveButton.place(x=30,y=150)

    def save(self):
        self.saveFilePath = filedialog.askopenfile(mode="w").name # Get save file path
        # Save Button
        self.saveButton = Button(text="Save", command=self.saveButtonFunction, bg="#e0e2db", fg="black", width=8)
        self.saveButton.pack()
        self.saveButton.place(x=200,y=150)

    def saveButtonFunction(self):
        self.file = open(self.filePath).read()
        # Entrys
        self.firstLetter = self.firstLetterEntry.get()
        self.lastLetter = self.lastLetterEntry.get()
        # Getting index of letters
        self.firstIndex = self.file.index(self.firstLetter)
        self.lastIndex = self.file.index(self.lastLetter)
        # File process
        self.openSaveFile = open(self.saveFilePath, "w")
        for i in range(self.firstIndex,self.lastIndex):
            self.openSaveFile.write(self.file[i])
        
        messagebox.showinfo(title="Completed!", message="Saved!")
        self.openSaveFile.close()
        os.system(str(self.saveFilePath))
        
Run = LogScanner()
