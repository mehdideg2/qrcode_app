import sqlite3
conn = sqlite3.connect('bdd.db')
c = conn.cursor()
c.execute('''CREATE TABLE data
             (date text, heure text, nserie text)''')
c.execute("INSERT INTO data VALUES ('2018-03-29','22:50','123')")
conn.commit()
conn.close()