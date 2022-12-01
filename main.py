from tkinter import *
from tkinter import filedialog

import os
import kodolo
from tkinter import messagebox

def start():
    KI.delete("1.0","end-1c")
    jsz = jelsz.get()
    sz = BE.get("1.0","end-1c")

    if jsz != "" and sz != "":
        if var.get() == 1:
            ksz = kodolo.koder(sz, jsz)
        else:
            ksz = kodolo.dekoder(sz, jsz)
        KI.insert(END, ksz)
    elif sz == "":
        messagebox.showinfo("Hiba", "Nem adott meg kódolandó szöveget!")
    elif jsz == "":
        messagebox.showinfo("Hiba", "Nem adott meg jelszót!")




def nyit():
    BE.delete("1.0","end-1c")
    fnev = filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("file_type","*.txt"),("all files","*.*")))
    of = open(fnev, 'r', encoding='utf-8')
    BE.insert(END,of.read())
    of.close()

def ment():
    if (KI.get("1.0", "end-1c")) != "":
        fnev = filedialog.asksaveasfilename(initialdir="/", title="Select file",
                                            filetypes=(("file_type", "*.txt"), ("all files", "*.*")))
        cf = open(fnev, 'a', encoding='utf-8')
        cf.write(KI.get("1.0", "end-1c"))
        cf.close()
    else:
        messagebox.showinfo("Hiba", "Sajnos nincs mit menteni")




ablak = Tk()
var = IntVar()
ablak.title('Titkosító')

ablak.geometry("800x600")
ko= Radiobutton(ablak, text="Kódol", variable=var, font="Helvetica 12 " ,state="active" ,value=1).grid(row=0,column=0,sticky=S)
dko= Radiobutton(ablak, text="Dekódol", font="Helvetica 12 ",variable=var, value=2).grid(row=0,column=1,sticky=S)

Label(ablak, font="Helvetica 12 ",text="Jelszó:").grid(row=1, column=0,sticky=W)
jelsz = Entry(ablak, font="Helvetica 12")
jelsz.grid(row=1, column=0,sticky=S)

Label(ablak, font="Helvetica 12 ",text="Bemenet:").grid(row=2,column=0,sticky=S)
BE = Text(ablak,width=49)
BE.grid(row=3, column=0,sticky=S)
Label(ablak, font="Helvetica 12 ",text="Kimenet:",).grid(row=2,column=1,sticky=S)
KI = Text(ablak,width=49)
KI.grid(row=3, column=1,sticky=S)
Button(ablak, text="Megnyitás", font="Helvetica 12 ",command=nyit).grid(row=4, column=0,sticky=W)
Button(ablak, text="Mentés" , font="Helvetica 12 ",command=ment).grid(row=4, column=1,sticky=E)
Button(ablak, text="   Start  ", justify="center" ,font="Helvetica 12 ",command=start).grid(row=5, column=1,sticky=E)
ablak.mainloop()

#ko.pack(anchor=W)
#dko.pack(anchor=W)
