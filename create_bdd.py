import sqlite3
import random
import string
import datetime

def creer_bdd():
    conn = sqlite3.connect('bdd.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE data
                 (date text, heure text, nserie text)''')
    conn.commit()
    conn.close()

def id_generator(size=6):
    return ''.join([random.choice(string.ascii_letters + string.digits) for n in range(size)])

def ajouter_un_champ():
    nserie = id_generator(10)
    current_date = datetime.datetime.now().date()
    current_time = datetime.datetime.now().time()
    conn = sqlite3.connect('bdd.db')
    c = conn.cursor()
    c.execute("INSERT INTO data VALUES ('{}','{}','{}')".format(current_date, current_time, nserie))
    conn.commit()
    conn.close()

def show_bdd_values():
    conn = sqlite3.connect('bdd.db')
    c = conn.cursor()
    for donnee in c.execute('SELECT * FROM data ORDER BY date'):
        print(donnee)

#creer_bdd()
#ajouter_un_champ()
#ajouter_un_champ()
show_bdd_values()