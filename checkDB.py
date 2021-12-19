import sqlite3

def check():
    con=sqlite3.connect('Students.db')
    cur = con.cursor()

    cur.execute('Select id from numberOfQuestion ORDER BY ID DESC LIMIT 1')
    last_q = cur.fetchall()
    last_q=last_q[0][0]

    cur.execute('Select id from Progress ORDER BY ID DESC LIMIT 1')
    last_p =cur.fetchall()
    last_p=last_p[0][0]

    if last_p < last_q:
        cur.execute('DELETE from numberOfQuestion Where id='+str(last_q))
        con.commit()
        print("delete in question and progress")
    else:
        print("same number in question and progress")
    con.close()
