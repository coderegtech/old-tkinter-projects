import sqlite3


class PatientData:
    def __init__(self, db):
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()
        self.cur.execute("""CREATE TABLE IF NOT EXISTS PatientRecord (
        patient_id INTEGER PRIMARY KEY,
        name text,
        address text,
        telephone_no integer,
        age integer,
        occupation text,
        status text,
        medical_his text,
        general_health text,
        headaches text,
        allergies text,
        bleeding_gums text,
        heart_bp integer,
        family_his text
        )""")

        self.conn.commit()

    def show_query(self):
        self.cur.execute("SELECT * FROM PatientRecord")
        rec = self.cur.fetchall()
        return rec

    def insert(self, name, address, telephone_no, age, occupation, status,
               medical_his, general_health, headaches, allergies, bleeding_gums, heart_bp,
               family_his):
        self.cur.execute("INSERT INTO PatientRecord VALUES (NULL, ?,?,?,?,?,?,?,?,?,?,?,?,?)",
                         (
                         name, address,telephone_no,
                         age, occupation,status,
                         medical_his,general_health,headaches,
                         allergies,bleeding_gums,heart_bp,
                         family_his
                         )
                        )
        self.conn.commit()

    def remove(self, patient_id):
        self.cur.execute("DELETE FROM PatientRecord WHERE patient_id = ?", (patient_id,))
        self.conn.commit()

    def __del__(self):
        self.conn.close()