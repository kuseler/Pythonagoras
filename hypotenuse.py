
import math
from tkinter import *
fields = ('Kathete', 'Kathete1', 'Hypotenuse')

def hypoten(entries):
    kat = float(entries['Kathete'].get())
    kat1 = float(entries['Kathete1'].get())
    hypo = math.sqrt(kat*kat + kat1*kat1)
    print(hypo)


def kat(entries):
    hypo = float(entries['Hypotenuse'].get())
    kat = float(entries['Hypotenuse'].get())
    kat1 = math.sqrt(hypo*hypo - kat*kat)
    print(kat1)


def makeform(root, fields):
    entries = {}
    for field in fields:
        row = Frame(root)
        lab = Label(row, width=22, text=field+": ", anchor='w')
        ent = Entry(row)
        ent.insert(0,"0")
        row.pack(side=TOP, fill=X, padx=5, pady=5)
        lab.pack(side=LEFT)
        ent.pack(side=RIGHT, expand=YES, fill=X)
        entries[field] = ent
    return entries

if __name__ == '__main__':
    root = Tk()
    ents = makeform(root, fields)
    root.bind('<Return>', (lambda event, e=ents: fetch(e)))
    b1 = Button(root, text='hypotenuse',
                command=(lambda e=ents: hypoten(e)))
    b1.pack(side=LEFT, padx=5, pady=5)
    b2 = Button(root, text='Kathete',
                command=(lambda e=ents: kat(e)))
    b2.pack(side=LEFT, padx=5, pady=5)
    b3 = Button(root, text='Quit', command=root.quit)
    b3.pack(side=LEFT, padx=5, pady=5)
    root.mainloop()

