import sqlite3
conn = sqlite3.connect("student_record.db")
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS student_record (
                    Enrollment INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    Subject TEXT NOT NULL,
                    Mark INTEGER NOT NULL
                )''')
cursor.execute("DELETE FROM student_record")
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
cursor.execute("SELECT name, Subject, Mark FROM student_record WHERE Mark > 90")
high_marks = cursor.fetchall()

print("\nStudents with Marks greater than 90:")
for student in high_marks:
    print(student)

print("\nUpdating marks for Aarav Mehta...")
cursor.execute('''UPDATE student_record 
                  SET Mark = 98 
                  WHERE name = 'Aarav Mehta' AND Subject = 'PWP' ''')
conn.commit()

cursor.execute('''SELECT name, Mark FROM student_record 
                  WHERE name = 'Aarav Mehta' ''')
updated_mark = cursor.fetchone()
print(f"Updated Mark for {updated_mark[0]}: {updated_mark[1]}")

print("\nDeleting student: Arjun Nair...")
cursor.execute('''DELETE FROM student_record WHERE name = 'Arjun Nair' ''')
conn.commit()
cursor.execute("SELECT * FROM student_record WHERE name = 'Arjun Nair'")
deleted = cursor.fetchone()

if deleted is None:
    print("Arjun Nair has been successfully deleted.")

# Step 9: Close connection
conn.close()
