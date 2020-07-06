from tkinter import *
from tkinter import ttk
import backend

#Kreiranje osnovnog prozora
root = Tk()
root.title("Rent a Car")
root.geometry("270x75+520+80")
#root.configure(background='#837e7e')
root.iconbitmap("rentaacar.ico")

def ispisi_sve(x):
    if x == 'Automobili':
        lista_automobil.delete(0, END)
        for row in backend.ispisi(x):
            lista_automobil.insert(END, row)
    elif x == 'Radnici':
        lista_radnik.delete(0, END)
        for row in backend.ispisi(x):
            lista_radnik.insert(END, row)
    elif x == 'Dobavljaci':
        lista_dobavljac.delete(0, END)
        for row in backend.ispisi(x):
            lista_dobavljac.insert(END, row)
    #lista.delete(0,END)
    #for row in backend.ispisi(x):
        #lista.insert(END,row)

def ispisi_sve_ugovor(x):
    for i in listBox.get_children():
        listBox.delete(i)
    temp_lista = []
    for row in backend.ispisi(x):
        temp_lista.append(row)
    for i, (BrUgovora,Cena,Datum,Kamata,BrRata,Dobavljac,Automobil,Radnik) in enumerate(temp_lista, start=1):
        listBox.insert("", "end", values=( BrUgovora,Cena,Datum,Kamata,BrRata,Dobavljac,Automobil,Radnik))

def dodaj(x):
    if x == 'Automobili':
        backend.dodaj(x,marka_text.get(), tip_vozila_text.get(), tip_potrosnje_text.get())
        lista_automobil.delete(0, END)
    elif x == 'Radnici':
        backend.dodaj(x,ime_text.get(), prezime_text.get(), br_ugovora_text.get())
        lista_radnik.delete(0, END)
    elif x == 'Dobavljaci':
        backend.dodaj(x,ime_kompanije_text.get(), kontakt_text.get(), mesto_text.get())
        lista_dobavljac.delete(0, END)

def dodaj_ugovor(x):
    backend.dodaj_ugovor(x,entry1_text.get(), entry3_text.get(), entry4_text.get(), entry5_text.get(), entry6_text.get(), entry7_text.get(), entry8_text.get())

def izbrisi(x):
    if x == 'Automobili':
        backend.izbrisi(x,id_automobila_text.get())
    elif x == 'Radnici':
        backend.izbrisi(x,id_radnika_text.get())
    elif x == 'Dobavljaci':
        backend.izbrisi(x,id_dobavljaca_text.get())
    elif x == 'Ugovori':
        backend.izbrisi(x,entry2_text.get())

def izmeni(x):
    if x == 'Automobili':
        backend.izmeni(x,marka_text.get(), id_automobila_text.get(), tip_vozila_text.get(), tip_potrosnje_text.get())
    elif x == 'Radnici':
        backend.izmeni(x,ime_text.get(), id_radnika_text.get(), prezime_text.get(), br_ugovora_text.get())
    elif x == 'Dobavljaci':
        backend.izmeni(x,ime_kompanije_text.get(), id_dobavljaca_text.get(), kontakt_text.get(), mesto_text.get())

def izmeni_ugovor(x):
    backend.izmeni_ugovor(x,entry1_text.get(), entry2_text.get(), entry3_text.get(), entry4_text.get(), entry5_text.get(), entry6_text.get(), entry7_text.get(), entry8_text.get())

def nadji(x):
    if x == 'Ugovori':
        for i in listBox.get_children():
            listBox.delete(i)
        temp_lista = []
        for row in backend.nadji(x, str(int(entry2_text.get()))):
            temp_lista.append(row)
            for i, (BrUgovora, Cena, Datum, Kamata, BrRata, Dobavljac, Automobil, Radnik) in enumerate(temp_lista, start=1):
                listBox.insert("", "end", values=(BrUgovora, Cena, Datum, Kamata, BrRata, Dobavljac, Automobil, Radnik))
    else:
        if x == 'Automobili':
            lista_automobil.delete(0,END)
            for row in backend.nadji(x,id_automobila_text.get()):
                lista_automobil.insert(END,row)
        elif x == 'Radnici':
            lista_radnik.delete(0,END)
            for row in backend.nadji(x,id_radnika_text.get()):
                lista_radnik.insert(END,row)
        elif x == 'Dobavljaci':
            lista_dobavljac.delete(0,END)
            for row in backend.nadji(x,id_dobavljaca_text.get()):
                lista_dobavljac.insert(END,row)

def automobili():
    automobil = Toplevel()
    automobil.title("Automobili")
    automobil.geometry("370x310+95+80")
    # automobil.configure(background='#837e7e')
    automobil.iconbitmap("rentaacar.ico")
    global marka_text
    marka_text = StringVar()
    global id_automobila_text
    id_automobila_text = StringVar()
    global tip_vozila_text
    tip_vozila_text = StringVar()
    global tip_potrosnje_text
    tip_potrosnje_text = StringVar()

    marka_entry = Entry(automobil, text=marka_text, width=11, borderwidth=5, justify=RIGHT, relief=SUNKEN, insertbackground="#a49b9b")
    marka_entry.grid(row=0, column=1, columnspan=1, padx=11, pady=10, sticky=W)

    id_entry = Entry(automobil, text=id_automobila_text, width=11, borderwidth=5, justify=RIGHT, relief=SUNKEN, insertbackground="#a49b9b")
    id_entry.grid(row=0, column=3, columnspan=1, padx=11, pady=10, sticky=W)

    tip_vozila_entry = Entry(automobil, text=tip_vozila_text, width=11, borderwidth=5, justify=RIGHT, relief=SUNKEN, insertbackground="#a49b9b")
    tip_vozila_entry.grid(row=1, column=1, columnspan=1, padx=11, pady=10, sticky=W)

    tip_potrosnje_entry = Entry(automobil, text=tip_potrosnje_text, width=11, borderwidth=5, justify=RIGHT, relief=SUNKEN, insertbackground="#a49b9b")
    tip_potrosnje_entry.grid(row=1, column=3, columnspan=1, padx=11, pady=10, sticky=W)

    marka_label = Label(automobil, text='Marka')
    marka_label.grid(row=0, column=0, padx=10)

    id_label = Label(automobil, text='ID')
    id_label.grid(row=0, column=2, padx=10)

    tip_vozila_label = Label(automobil, text='Tip Vozila')
    tip_vozila_label.grid(row=1, column=0, padx=10)

    tipPotrosnje_label = Label(automobil, text='Tip Potrosnje')
    tipPotrosnje_label.grid(row=1, column=2, padx=10)

    dodaj_button = Button(automobil, text="Dodaj", command=lambda: dodaj("Automobili"))
    dodaj_button.grid(row=2,column=0)

    izmeni_button = Button(automobil, text="Izmeni", command=lambda: izmeni("Automobili"))
    izmeni_button.grid(row=2,column=1)

    izbrisi_button = Button(automobil, text="Izbrisi", command=lambda: izbrisi("Automobili"))
    izbrisi_button.grid(row=2,column=2)

    nadji_button = Button(automobil, text="Nadji", command=lambda: nadji("Automobili"))
    nadji_button.grid(row=2,column=3)

    ispisi_button = Button(automobil, text="Ispisi sve",padx=13, command=lambda: ispisi_sve("Automobili"))
    ispisi_button.grid(row=3, column=1,columnspan=2)

    global lista_automobil
    lista_automobil = Listbox(automobil)
    lista_automobil.grid(row=4,columnspan=4)
    lista_automobil.configure(height=10,width=50)

def radnici():
    radnik = Toplevel()
    radnik.title("Radnici")
    radnik.geometry("370x310+860+80")
    # radnik.configure(background='#837e7e')
    radnik.iconbitmap("rentaacar.ico")
    global ime_text
    ime_text = StringVar()
    global id_radnika_text
    id_radnika_text = StringVar()
    global prezime_text
    prezime_text = StringVar()
    global br_ugovora_text
    br_ugovora_text = StringVar()

    ime_entry = Entry(radnik, text=ime_text, width=11, borderwidth=5, justify=RIGHT, relief=SUNKEN, insertbackground="#a49b9b")
    ime_entry.grid(row=0, column=1, columnspan=1, padx=11, pady=10, sticky=W)

    id_entry = Entry(radnik, text=id_radnika_text, width=11, borderwidth=5, justify=RIGHT, relief=SUNKEN, insertbackground="#a49b9b")
    id_entry.grid(row=0, column=3, columnspan=1, padx=11, pady=10, sticky=W)

    prezime_entry = Entry(radnik, text=prezime_text, width=11, borderwidth=5, justify=RIGHT, relief=SUNKEN, insertbackground="#a49b9b")
    prezime_entry.grid(row=1, column=1, columnspan=1, padx=11, pady=10, sticky=W)

    br_ugovora_entry = Entry(radnik, text=br_ugovora_text, width=11, borderwidth=5, justify=RIGHT, relief=SUNKEN, insertbackground="#a49b9b")
    br_ugovora_entry.grid(row=1, column=3, columnspan=1, padx=11, pady=10, sticky=W)

    ime_label = Label(radnik, text='Ime')
    ime_label.grid(row=0, column=0, padx=10)

    id_label = Label(radnik, text='ID')
    id_label.grid(row=0, column=2, padx=10)

    prezime_label = Label(radnik, text='Prezime')
    prezime_label.grid(row=1, column=0, padx=10)

    br_ugovora_label = Label(radnik, text='Broj Ugovora')
    br_ugovora_label.grid(row=1, column=2, padx=10)

    dodaj_button = Button(radnik, text="Dodaj", command=lambda: dodaj("Radnici"))
    dodaj_button.grid(row=2,column=0)

    izmeni_button = Button(radnik, text="Izmeni", command=lambda: izmeni("Radnici"))
    izmeni_button.grid(row=2,column=1)

    izbrisi_button = Button(radnik, text="Izbrisi", command=lambda: izbrisi("Radnici"))
    izbrisi_button.grid(row=2,column=2)

    nadji_button = Button(radnik, text="Nadji", command=lambda: nadji("Radnici"))
    nadji_button.grid(row=2,column=3)

    ispisi_button = Button(radnik, text="Ispisi sve",padx=13, command=lambda: ispisi_sve("Radnici"))
    ispisi_button.grid(row=3, column=1,columnspan=2)

    global lista_radnik
    lista_radnik = Listbox(radnik)
    lista_radnik.grid(row=4,columnspan=4)
    lista_radnik.configure(height=10,width=50)

def dobavljaci():
    dobavljac = Toplevel()
    dobavljac.title("Dobavljaci")
    dobavljac.geometry("370x310+477+200")
    # dobavljac.configure(background='#837e7e')
    dobavljac.iconbitmap("rentaacar.ico")
    global ime_kompanije_text
    ime_kompanije_text = StringVar()
    global id_dobavljaca_text
    id_dobavljaca_text = StringVar()
    global kontakt_text
    kontakt_text = StringVar()
    global mesto_text
    mesto_text = StringVar()

    ime_kompanije_entry = Entry(dobavljac, text=ime_kompanije_text, width=11, borderwidth=5, justify=RIGHT, relief=SUNKEN, insertbackground="#a49b9b")
    ime_kompanije_entry.grid(row=0, column=1, columnspan=1, padx=11, pady=10, sticky=W)

    id_entry = Entry(dobavljac, text=id_dobavljaca_text, width=11, borderwidth=5, justify=RIGHT, relief=SUNKEN, insertbackground="#a49b9b")
    id_entry.grid(row=0, column=3, columnspan=1, padx=11, pady=10, sticky=W)

    kontakt_entry = Entry(dobavljac, text=kontakt_text, width=11, borderwidth=5, justify=RIGHT, relief=SUNKEN, insertbackground="#a49b9b")
    kontakt_entry.grid(row=1, column=1, columnspan=1, padx=11, pady=10, sticky=W)

    mesto_entry = Entry(dobavljac, text=mesto_text, width=11, borderwidth=5, justify=RIGHT, relief=SUNKEN, insertbackground="#a49b9b")
    mesto_entry.grid(row=1, column=3, columnspan=1, padx=11, pady=10, sticky=W)

    ime_kompanije_label = Label(dobavljac, text='Ime Kompanije')
    ime_kompanije_label.grid(row=0, column=0, padx=10)

    id_label = Label(dobavljac, text='ID')
    id_label.grid(row=0, column=2, padx=10)

    kontakt_label = Label(dobavljac, text='Kontakt')
    kontakt_label.grid(row=1, column=0, padx=10)

    mesto_label = Label(dobavljac, text='Mesto')
    mesto_label.grid(row=1, column=2, padx=10)

    dodaj_button = Button(dobavljac, text="Dodaj", command=lambda: dodaj("Dobavljaci"))
    dodaj_button.grid(row=2,column=0)

    izmeni_button = Button(dobavljac, text="Izmeni", command=lambda: izmeni("Dobavljaci"))
    izmeni_button.grid(row=2,column=1)

    izbrisi_button = Button(dobavljac, text="Izbrisi", command=lambda: izbrisi("Dobavljaci"))
    izbrisi_button.grid(row=2,column=2)

    nadji_button = Button(dobavljac, text="Nadji", command=lambda: nadji("Dobavljaci"))
    nadji_button.grid(row=2,column=3)

    ispisi_button = Button(dobavljac, text="Ispisi sve",padx=13, command=lambda: ispisi_sve("Dobavljaci"))
    ispisi_button.grid(row=3, column=1,columnspan=2)

    global lista_dobavljac
    lista_dobavljac = Listbox(dobavljac)
    lista_dobavljac.grid(row=4,columnspan=4)
    lista_dobavljac.configure(height=10,width=50)

def ugovori():
    ugovor = Toplevel()
    ugovor.title("Ugovori")
    ugovor.title("Dobavljaci")
    ugovor.geometry("475x480+430+150")
    # ugovor.configure(background='#837e7e')
    ugovor.iconbitmap("rentaacar.ico")
    global entry1_text
    entry1_text = StringVar()
    global entry2_text
    entry2_text = StringVar()
    global entry3_text
    entry3_text = StringVar()
    global entry4_text
    entry4_text = StringVar()
    global entry5_text
    entry5_text = StringVar()
    global entry6_text
    entry6_text = StringVar()
    global entry7_text
    entry7_text = StringVar()
    global entry8_text
    entry8_text = StringVar()

    cena_entry = Entry(ugovor, text=entry1_text, width=11, borderwidth=5, justify=RIGHT, relief=SUNKEN, insertbackground="#a49b9b")
    cena_entry.grid(row=0, column=1, columnspan=1, padx=11, pady=10, sticky=W)

    br_ugovora_entry = Entry(ugovor, text=entry2_text, width=11, borderwidth=5, justify=RIGHT, relief=SUNKEN, insertbackground="#a49b9b")
    br_ugovora_entry.grid(row=0, column=3, columnspan=1, padx=11, pady=10, sticky=W)

    datum_entry = Entry(ugovor, text=entry3_text, width=11, borderwidth=5, justify=RIGHT, relief=SUNKEN, insertbackground="#a49b9b")
    datum_entry.grid(row=1, column=1, columnspan=1, padx=11, pady=10, sticky=W)

    kamata_entry = Entry(ugovor, text=entry4_text, width=11, borderwidth=5, justify=RIGHT, relief=SUNKEN, insertbackground="#a49b9b")
    kamata_entry.grid(row=1, column=3, columnspan=1, padx=11, pady=10, sticky=W)

    broj_rata_entry = Entry(ugovor, text=entry5_text, width=11, borderwidth=5, justify=RIGHT, relief=SUNKEN, insertbackground="#a49b9b")
    broj_rata_entry.grid(row=2, column=1, columnspan=1, padx=11, pady=10, sticky=W)

    dobavljac_entry = Entry(ugovor, text=entry6_text, width=11, borderwidth=5, justify=RIGHT, relief=SUNKEN, insertbackground="#a49b9b")
    dobavljac_entry.grid(row=2, column=3, columnspan=1, padx=11, pady=10, sticky=W)

    automobil_entry = Entry(ugovor, text=entry7_text, width=11, borderwidth=5, justify=RIGHT, relief=SUNKEN, insertbackground="#a49b9b")
    automobil_entry.grid(row=3, column=1, columnspan=1, padx=11, pady=10, sticky=W)

    radnik_entry = Entry(ugovor, text=entry8_text, width=11, borderwidth=5, justify=RIGHT, relief=SUNKEN, insertbackground="#a49b9b")
    radnik_entry.grid(row=3, column=3, columnspan=1, padx=11, pady=10, sticky=W)

    cena_label = Label(ugovor, text='Cena')
    cena_label.grid(row=0, column=0, padx=10)

    br_ugovora_label = Label(ugovor, text='Br Ugovora')
    br_ugovora_label.grid(row=0, column=2, padx=10)

    datum_label = Label(ugovor, text='Datum')
    datum_label.grid(row=1, column=0, padx=10)

    kamata_label = Label(ugovor, text='Kamata')
    kamata_label.grid(row=1, column=2, padx=10)

    broj_rata_label = Label(ugovor, text='Br Rata')
    broj_rata_label.grid(row=2, column=0, padx=10)

    dobavljac_label = Label(ugovor, text='Dobavljac')
    dobavljac_label.grid(row=2, column=2, padx=10)

    automobil_label = Label(ugovor, text='Automobil')
    automobil_label.grid(row=3, column=0, padx=10)

    radnik_label = Label(ugovor, text='Radnik')
    radnik_label.grid(row=3, column=2, padx=10)

    dodaj_button = Button(ugovor, text="Dodaj", command=lambda: dodaj_ugovor("Ugovori"))
    dodaj_button.grid(row=4,column=0)

    izmeni_button = Button(ugovor, text="Izmeni", command=lambda: izmeni_ugovor("Ugovori"))
    izmeni_button.grid(row=4,column=1)

    izbrisi_button = Button(ugovor, text="Izbrisi", command=lambda: izbrisi("Ugovori"))
    izbrisi_button.grid(row=4,column=2)

    nadji_button = Button(ugovor, text="Nadji", command=lambda: nadji("Ugovori"))
    nadji_button.grid(row=4,column=3)

    ispisi_button = Button(ugovor, text="Ispisi sve",padx=13, command=lambda: ispisi_sve_ugovor("Ugovori"))
    ispisi_button.grid(row=5, column=1,columnspan=2)

    #global lista
    #lista = Listbox(ugovor)
    #lista.grid(row=6,columnspan=4)
    #lista.configure(height=10,width=50,setgrid=0)

    global listBox
    cols = ('Br Ugovora','Cena','Datum','Kamata','Br Rata','Dobavljac','Automobil','Radnik')
    listBox = ttk.Treeview(ugovor, columns=cols, show='headings')
    #listBox.configure(width=50)
    for col in cols:
        listBox.heading(col, text=col)
        listBox.column(col,width=60)
    listBox.grid(row=7, column=0, columnspan=4)

#Dugmici na pocetnoj strani
automobili = Button(root, text="Automobili",padx=17, command=automobili)
automobili.grid(row=0,column=2,padx=18,pady=5, sticky=E)

radnici = Button(root, text="Radnici",padx=20, command=radnici)
radnici.grid(row=0,column=3,padx=20,pady=5,sticky=E)

dobavljaci = Button(root, text="Dobavljaci",padx=20, command=dobavljaci)
dobavljaci.grid(row=1,column=2,padx=18,sticky=SE)

ugovori = Button(root, text="Ugovori",padx=20, command=ugovori)
ugovori.grid(row=1,column=3,padx=18,sticky=SW)

root.mainloop()