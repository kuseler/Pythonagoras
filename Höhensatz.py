import math
from tkinter import *

fields = ['Kathete "p"', 'Kathete "q"', 'Hypotenuse "a"', 'Hypotenuse "b"', 'Höhe "h"', 'Gesamthypotenuse "c"']

def ca(entries):
    global Gesamthypotenuse
    Gesamthypotenuse = float(entries['Kathete "p"'].get()) + float(entries['Kathete "q"'].get())
    entries['Gesamthypotenuse "c"'].delete(0, END)
    entries['Gesamthypotenuse "c"'].insert(0, Gesamthypotenuse)

def hoehe(entries):
    height = math.sqrt(float(entries['Kathete "p"'].get()) * float(entries['Kathete "q"'].get()))
    print(height)
    entries['Höhe "h"'].delete(0, END)
    entries['Höhe "h"'].insert(0, height)




def katha(entries):
    katha = math.sqrt(float(entries['Kathete "p"'].get()) * Gesamthypotenuse)
    entries['Hypotenuse "a"'].delete(0, END)
    entries['Hypotenuse "a"'].insert(0, katha)
    print(katha)


def kathb(entries):
    kathb = math.sqrt(float(entries['Kathete "q"'].get()) * Gesamthypotenuse)
    entries['Hypotenuse "b"'].delete(0, END)
    entries['Hypotenuse "b"'].insert(0, kathb)
    print(kathb)

def alles(entries):
    ca(entries)
    hoehe(entries)
    katha(entries)
    kathb(entries)





def makeform(root, fields):
    entries = {}
    for field in fields:
        row = Frame(root)
        lab = Label(row, width=22, text=field + ": ", anchor='w')
        ent = Entry(row)
        ent.insert(0, "0")
        row.pack(side=TOP, fill=X, padx=5, pady=5)
        lab.pack(side=LEFT)
        ent.pack(side=RIGHT, expand=YES, fill=X)
        entries[field] = ent
    return entries

if __name__ == '__main__':
    root = Tk()
    logo = PhotoImage(file="kathetensatz-1.gif")
    w1 = Label(root, image=logo).pack(side="right")
    
    ents = makeform(root, fields)
    root.bind('<Return>', (lambda event, e=ents: fetch(e)))
    b2 = Button(root, text='Höhe',
                command=(lambda e=ents: hoehe(e)))
    b2.pack(side=LEFT, padx=5, pady=5)
    b1 = Button(root, text='kathete A',
                command=(lambda e=ents: katha(e)))
    b1.pack(side=LEFT, padx=5, pady=5)
    b3 = Button(root, text='kathete B',
                command=(lambda e=ents: kathb(e)))
    b3.pack(side=LEFT, padx=5, pady=5)
    b4 = Button(root, text='C errechnen',
                command=(lambda e=ents: ca(e)))
    b4.pack(side=LEFT, padx=5, pady=5)
    b5 = Button(root, text='Alles', command=(lambda e=ents: alles(e)))
    b5.pack(side=LEFT, padx=5, pady=5)

    root.mainloop()



