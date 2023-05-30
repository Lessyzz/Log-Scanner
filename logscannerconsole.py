from tkinter import *
import os

class LogScannerConsole():
    def __init__(self):
        os.system("cls")
        print(
"""Type full PATH: 
Example: 'C:/file.txt'
""")
        self.getFilePath()

    def getFilePath(self):
        self.filePath   = input() # Get file path
        # File process
        self.file_open  = open(self.filePath)
        self.file_read  = self.file_open.read()
        self.getWords()

    def getWords(self):
        # Get words
        self.firstWord  = input("Type first word: ")
        self.lastWord   = input("Type last word: ")
        # Get indexs of words
        self.firstindex = self.file_read.index(self.firstWord)
        self.lastindex  = self.file_read.index(self.lastWord)
        self.saveFile()

    def saveFile(self):
        # Get save file path
        self.saveFilePath    = input("Type the path to the file to save: ")
        self.saveFileOpen    = open(self.saveFilePath, "w")
        self.write()

    def write(self):
        for i in range(self.firstindex, self.lastindex):
            self.saveFileOpen.write(self.file_read[i])
        print("Saved!")

Run = LogScannerConsole()
