import sqlite3

# Step 1: Connect to database (creates file if not exists)
conn = sqlite3.connect("student_record.db")

# Step 2: Create a cursor
cursor = conn.cursor()

# Step 3: Create students table if it doesn't exist
cursor.execute('''CREATE TABLE IF NOT EXISTS student_record (
                    Enrollment INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    Subject TEXT NOT NULL,
                    Mark INTEGER NOT NULL
                )''')

# Clear old data to avoid duplicates on re-run (optional)
cursor.execute("DELETE FROM student_record")

# Step 4: Insert multiple student records
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

# Step 5: Fetch all student records
cursor.execute("SELECT * FROM student_record")
rows = cursor.fetchall()

print("All Student Records:")
for row in rows:
    print(row)

# Step 6: Fetch data with specific criteria (Marks > 90)
cursor.execute("SELECT name, Subject, Mark FROM student_record WHERE Mark > 90")
high_marks = cursor.fetchall()

print("\nStudents with Marks greater than 90:")
for student in high_marks:
    print(student)

# Step 7: Update student information
print("\nUpdating marks for Aarav Mehta...")
cursor.execute('''UPDATE student_record 
                  SET Mark = 98 
                  WHERE name = 'Aarav Mehta' AND Subject = 'PWP' ''')
conn.commit()

# Verify the update
cursor.execute('''SELECT name, Mark FROM student_record 
                  WHERE name = 'Aarav Mehta' ''')
updated_mark = cursor.fetchone()
print(f"Updated Mark for {updated_mark[0]}: {updated_mark[1]}")

# Step 8: Delete a student
print("\nDeleting student: Arjun Nair...")
cursor.execute('''DELETE FROM student_record WHERE name = 'Arjun Nair' ''')
conn.commit()

# Verify deletion
cursor.execute("SELECT * FROM student_record WHERE name = 'Arjun Nair'")
deleted = cursor.fetchone()
if deleted is None:
    print("Arjun Nair has been successfully deleted.")

# Step 9: Calculate the average mark
cursor.execute("SELECT AVG(Mark) FROM student_record")
avg_mark = cursor.fetchone()[0]
print(f"\nThe average mark of students is: {avg_mark:.2f}")

# Step 10: Close connection
conn.close()
