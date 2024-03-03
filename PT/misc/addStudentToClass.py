import random
import sqlite3


conn = sqlite3.connect('students.db')
cursor = conn.cursor()

cursor.execute(f'''
            CREATE TABLE IF NOT EXISTS student_classes(
                enrollment_id INTEGER PRIMARY KEY AUTOINCREMENT,
                student_id TEXT,
                name TEXT,
                class_id TEXT,
                FOREIGN KEY (student_id) REFERENCES student(id),
                FOREIGN KEY (class_id) REFERENCES classes(id)
            )
''')

cursor.execute("SELECT * FROM classes")
results = cursor.fetchall()
m1s = results[0:4]

m2s1 = results[:1]
m2s2 = results[-3:]

m2s = m2s1 + m2s2

def RegisterToCLass(stuId):
    cursor.execute(f"SELECT * FROM student WHERE id = {stuId}")
    info = cursor.fetchone()
    major = info[3]
    if major == "1":
        for s in m1s:
            cursor.execute("INSERT INTO student_classes (student_id,name,class_id) VALUES(?,?,?)",(stuId,info[2],s[0]))
    else:
        for s in m2s:
            cursor.execute("INSERT INTO student_classes (student_id,name,class_id) VALUES(?,?,?)",(stuId,info[2],s[0]))


cursor.execute("SELECT * FROM student")
students = cursor.fetchall()

for i in students:
    RegisterToCLass(i[0])

conn.commit()
conn.close()