from tkinter import *
import os

os.system("cls")
print("""
    Type full PATH: 
    Example: 'C:/file.txt'
    """)

filePath = input() # Get file path
# File process
file_open = open(filePath)
file_read = file_open.read()
# Get inputs
first = input("Type first letter: ")
last = input("Type last letter: ")
# Get indexs
firstindex = file_read.index(first)
lastindex = file_read.index(last)
# Save file
saveFile = input("Type the path to the file to save: ")
saveFileOpen = open(saveFile, "w")

for i in range(firstindex,lastindex):
    saveFileOpen.write(file_read[i])
print("Saved!")
