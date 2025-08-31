import sqlite3
conn = sqlite3.connect("student_record.db")
cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS student_record (
                    Enrollment INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    Subject TEXT NOT NULL,
                    Mark INTEGER NOT NULL
                )''')

student_record = [
    (92301733016,'Aarav Mehta','PWP',95),
    (92301733017,'Riya Sharma','PWP',85),
    (92301733027,'Kabir Patel','PWP',90),
    (92301733046,'Ishita Desai','PWP',93),
    (92301733058,'Arjun Nair','PWP',75)
]

cursor.executemany('''INSERT INTO student_record (Enrollment, name, Subject, Mark) 
                      VALUES (?, ?, ?, ?)''', student_record)

conn.commit()

cursor.execute("SELECT * FROM student_record")
rows = cursor.fetchall()

print("All Student Records:")
for row in rows:
    print(row)

conn.close()
