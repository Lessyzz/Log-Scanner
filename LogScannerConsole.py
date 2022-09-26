import os
lang = os.getenv('LANG')
from tkinter import *

if "tr_TR" in lang:
    print("""
        Tüm dosya yolunu yazınız: 
        Örneğin:/ 'C:/aa.txt'
        """)
    file_input = input()
    file = open(file_input)
    giris = file.read()
    first = input("Başlangıç metni: ")
    end = input("Bitiş metni: ")
    firstindex = giris.index(first)
    endindex = giris.index(end)

    secondfile = input("Kaydedilecek dosyanın yolunu yazınız: ")
    secondfileopen = open(secondfile, "w")

    for i in range(firstindex,endindex):
        secondfileopen.write(giris[i])
    print("Kaydedildi!")

else:
    print("""
        Type full PATH: 
        Example:/ 'C:/aa.txt'
        """)
    file_input = input()
    file = open(file_input)
    giris = file.read()
    first = input("Type first text: ")
    end = input("Type last text: ")
    firstindex = giris.index(first)
    endindex = giris.index(end)

    secondfile = input("Type the path to the file to save: ")
    secondfileopen = open(secondfile, "w")

    for i in range(firstindex,endindex):
        secondfileopen.write(giris[i])
    print("Saved!")
