import sqlite3
import random
from string import digits

firstName = ["فاطمة", "مريم", "زينب", "لمى", "رغد", "ياسمين", "لينا", "هالة", "سارة", "نورا"]
secondName = ["محمد", "أحمد", "علي", "يوسف", "أسامة", "عمر", "خالد", "مصطفى", "أيمن", "سعيد"]
lastName = ["العتيبي", "المطيري", "الشمري", "الحربي",  "الدوسري"]

conn = sqlite3.connect('students.db')
cursor = conn.cursor()

cursor.execute(f'''
            CREATE TABLE IF NOT EXISTS student(
                id TEXT PRIMARY KEY,
                pass TEXT NOT NULL,
                name TEXT NOT NULL,
                m TEXT NOT NULL
            )
''')

sid = []
while len(sid) < 100:
    num = (f"420{''.join(random.choice(digits) for i in range(4))}")
    if num not in sid:
        sid.append(num)


for i in sid:
    stuid = i
    password = "1234"
    name = (f"{random.choice(firstName)} {random.choice(secondName)} {random.choice(lastName)}")
    cursor.execute(f'''
    INSERT INTO student(id,pass,name,m) VALUES (?,?,?,?)
    ''',(stuid,password,name,random.randint(1,2)))

conn.commit()