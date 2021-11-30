import sqlite3
con = sqlite3.connect('Students.db')
cur = con.cursor()
cur.execute('DELETE from numberofquestion where id=121')
con.commit()
con.close()
