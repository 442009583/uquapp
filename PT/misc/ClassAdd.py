import sqlite3
import random

conn = sqlite3.connect('students.db')
cursor = conn.cursor()

cursor.execute(f'''
            CREATE TABLE IF NOT EXISTS classes(
                id TEXT PRIMARY KEY,
                name TEXT NOT NULL,
                start TEXT NOT NULL,
                end TEXT NOT NULL
            )
''')

subjects = {
    'الإنجليزي': {'start': 13, 'end': 16, 'id': 'ENG101'},

    'التاريخ': {'start': 10, 'end': 12, 'id': 'HIST101'},
    'الأدب العربي': {'start': 16, 'end': 18, 'id': 'ARAB101'},
    'علم نفس': {'start': 18, 'end': 20, 'id': 'PSY101'},

    'الفيزياء': {'start': 16, 'end': 18, 'id': 'PHY101'},
    'الرياضيات': {'start': 10, 'end': 12, 'id': 'MATH101'},
    'علوم الحاسب': {'start': 8, 'end': 10, 'id': 'CS101'},
}

def insertclass(id,name,stime,etime):
    cursor.execute(f'''
    INSERT INTO Classes(id,name,start,end) VALUES(?,?,?,?)
''',(id,name,stime,etime))


for subject,info in subjects.items():

    insertclass(info["id"],subject,info["start"],info["end"])

conn.commit()