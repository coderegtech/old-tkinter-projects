import sqlite3

class Data:
    def __init__(self, db):
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()
        self.cur.execute("""CREATE TABLE IF NOT EXISTS student_database
        (
        no INTEGER PRIMARY KEY,
        LRN integer,
        l_name text,
        f_name text,
        address text,
        guardian text,
        guardian_no integer,
        birthday text,
        birth_place text,
        sex text
        )
        """)

        self.conn.commit()

    def insert(self, lrn, l_name, f_name, address, guardian, guardian_no,
               birth_day, birth_place, sex):
        self.cur.execute("INSERT INTO student_database VALUES(NULL, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                         (
                             lrn, l_name, f_name, address, guardian, guardian_no,
                             birth_day, birth_place, sex
                         ))
        self.conn.commit()

    def show_query(self):
        self.cur.execute("SELECT * FROM student_database")
        row = self.cur.fetchall()
        return row

    def remove(self, no):
        self.cur.execute("DELETE FROM student_database WHERE no =?", (no,))
        self.conn.commit()
