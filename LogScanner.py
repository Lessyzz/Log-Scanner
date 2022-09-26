import os
from tkinter import filedialog
from tkinter import *
from tkinter import messagebox
lang = os.getenv('LANG')


def scan():
    global firstentry
    global endentry
    global filepath
    global savefilepath
    file = open(filepath).read()
    firstentry = firstentry.get()
    endentry = endentry.get()
    ###### 
    firstindex = file.index(firstentry)
    endindex = file.index(endentry)
    savefileopen = open(savefilepath, "w")
    for i in range(firstindex,endindex):
        savefileopen.write(file[i])
    if "tr_TR" in lang:
        messagebox.showinfo(title="Tamamlandı!", message="Kaydedildi!")
    else:
        messagebox.showinfo(title="Completed!", message="Saved!")

def save():
    global savefilepath
    if "tr_TR" in lang:
        savefilepath = filedialog.askopenfile(mode="w").name
        savebutton = Button(text="Kaydet", command=scan, bg="black", fg="red", width=8)
        savebutton.pack()
        savebutton.place(x=200,y=150)
    else:
        savefilepath = filedialog.askopenfile(mode="w").name
        savebutton = Button(text="Save", command=scan, bg="black", fg="red", width=8)
        savebutton.pack()
        savebutton.place(x=200,y=150)

def texts():
    global filepath
    global firstentry
    global endentry
    if "tr_TR" in lang:
        filepath = filedialog.askopenfile().name
        labelfirst = Label(window, bg="black", fg="red", text="Başlangıç metni:")
        labelfirst.pack()
        labelfirst.place(x=27,y=68)
        ######
        labelend = Label(window, bg="black", fg="red", text="Bitiş metni:")
        labelend.pack()
        labelend.place(x=27,y=98)
        ######
        first = Entry(window, bg="red", fg="black", width=25)
        first.pack()
        first.place(x=120,y=70)
        ######
        end = Entry(window, bg="red", fg="black", width=25)
        end.pack()
        end.place(x=120,y=100)
        ######
        button = Button(text="Kaydedilecek dosyayı seçiniz", command=save, bg="black", fg="red",width=22)
        button.pack()
        button.place(x=30,y=150)
        ######
        firstentry = first
        endentry = end

    else:
        filepath = filedialog.askopenfile().name
        labelfirst = Label(window, bg="black", fg="red", text="Type first text:")
        labelfirst.pack()
        labelfirst.place(x=37,y=68)
        ######
        labelend = Label(window, bg="black", fg="red", text="Type last text:")
        labelend.pack()
        labelend.place(x=37,y=98)
        ######
        first = Entry(window, bg="red", fg="black", width=25)
        first.pack()
        first.place(x=120,y=70)
        ######
        end = Entry(window, bg="red", fg="black", width=25)
        end.pack()
        end.place(x=120,y=100)
        ######
        button = Button(text="Select the file to save", command=save, bg="black", fg="red",width=19)
        button.pack()
        button.place(x=50,y=150)
        ######
        firstentry = first
        endentry = end
  
    
filepath = ""
savefilepath = ""
firstentry = ""
endentry = ""

if "tr_TR" in lang:
    window = Tk()
    window.title("LogScanner by Lessy")
    window.geometry("300x200")
    window.configure(background="black")
    window.resizable(False,False)
    ######
    Label2 = Label(window, bg="black", fg="red", text="by Lessy", font="Times 8")
    Label2.pack()
    Label2.place(x=250, y=5)
    ######
    button = Button(text="Dosyayı seç", command=texts, bg="black", fg="red")
    button.pack()
    button.place(x=120,y=20)
    window.mainloop()


else:
    window = Tk()
    window.title("LogScanner by Lessy")
    window.geometry("300x200")
    window.configure(background="black")
    window.resizable(False,False)
    ######
    Label2 = Label(window, bg="black", fg="red", text="by Lessy", font="Times 8")
    Label2.pack()
    Label2.place(x=250, y=5)
    ######
    button = Button(text="Choose file", command=texts, bg="black", fg="red")
    button.pack()
    button.place(x=120,y=20)
    window.mainloop()





