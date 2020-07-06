import sqlite3

def konekcija():
    kon=sqlite3.connect("baza.db")
    kon.close()

def dodaj(x,y,z,c):
    kon=sqlite3.connect("baza.db")
    kursor=kon.cursor()
    kursor.execute("INSERT INTO {0} VALUES (NULL,?,?,?)".format(x) ,(y,z,c))
    kon.commit()
    kon.close()
    ispisi(x)

def dodaj_ugovor(x,y,z,c,g,h,j,k):
    kon=sqlite3.connect("baza.db")
    kursor=kon.cursor()
    kursor.execute("INSERT INTO {0} VALUES (NULL,?,?,?,?,?,?,?)".format(x) ,(y,z,c,g,h,j,k))
    kon.commit()
    kon.close()
    ispisi(x)

def ispisi(x):
    kon=sqlite3.connect("baza.db")
    kursor=kon.cursor()
    kursor.execute("SELECT * FROM %s" %x)
    rows=kursor.fetchall()
    kon.close()
    return rows

def nadji(x,y):
    if x == 'Automobili':
        id = 'idAutomobila'
    elif x == 'Radnici':
        id = 'idRadnika'
    elif x == 'Dobavljaci':
        id = 'idDobavljaca'
    elif x == 'Ugovori':
        id = 'brUgovora'
    kon=sqlite3.connect("baza.db")
    kursor=kon.cursor()
    kursor.execute("SELECT * FROM {0} WHERE {1} = {2} ".format(x,id,y))
    rows=kursor.fetchall()
    kon.close()
    return rows

def izbrisi(x, y):
    if x == 'Automobili':
        id = 'idAutomobila'
    elif x == 'Radnici':
        id = 'idRadnika'
    elif x == 'Dobavljaci':
        id = 'idDobavljaca'
    elif x == 'Ugovori':
        id = 'brUgovora'
    kon=sqlite3.connect("baza.db")
    kursor=kon.cursor()
    kursor.execute("DELETE FROM {0} WHERE {1} = {2} ".format(x,id,y))
    kon.commit()
    kon.close()

def izmeni(x,y,z,c,v):
    if x == 'Automobili':
        id = 'idAutomobila'
        drugi = 'tipVozila'
        treci = 'tipPotrosnje'
        prvi = 'marka'
    elif x == 'Radnici':
        id = 'idRadnika'
        prvi = 'ime'
        drugi = 'prezime'
        treci = 'potpisaniUgovori'
    elif x == 'Dobavljaci':
        id = 'idDobavljaca'
        prvi = 'imeKompanije'
        drugi = 'kontakt'
        treci = 'mesto'
    kon=sqlite3.connect("baza.db")
    kursor=kon.cursor()
    kursor.execute("UPDATE {0} SET {1} = ?, {2}= ?, {3}= ? WHERE {4}={5}".format(x,prvi,drugi,treci,id,z),(y,c,v))
    kon.commit()
    kon.close()

def izmeni_ugovor(x,y,z,c,g,h,j,k,m):
    kon=sqlite3.connect("baza.db")
    kursor=kon.cursor()
    kursor.execute("UPDATE {0} SET cena = ?, datum= ?, kamata= ?, brRata= ?, dobavljac= ?, automobil= ?, radnik= ? WHERE brUgovora= ?".format(x),(y,c,g,h,j,k,m,z))
    kon.commit()
    kon.close()

konekcija()