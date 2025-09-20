import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",          
        password="943pradip@A",   
        database="student_db"
    )

def add_student(name, age, grade):
    conn = get_connection()
    cursor = conn.cursor()
    query = "INSERT INTO students123 (name, age, grade) VALUES (%s, %s, %s)"
    cursor.execute(query, (name, age, grade))
    conn.commit()
    conn.close()
    print("Student added successfully!")

def view_students():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students123")
    rows = cursor.fetchall()
    conn.close()
    print("\n--- Student Records ---")
    for row in rows:
        print(row)

def search_student(student_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students123 WHERE id = %s", (student_id,))
    row = cursor.fetchone()
    conn.close()
    if row:
        print("Student Found:", row)
    else:
        print("Student not found.")

def update_student(student_id, name, age, grade):
    conn = get_connection()
    cursor = conn.cursor()
    query = "UPDATE students123 SET name=%s, age=%s, grade=%s WHERE id=%s"
    cursor.execute(query, (name, age, grade, student_id))
    conn.commit()
    conn.close()
    print("Student updated successfully!")

from colorama import Fore, Style, init
init(autoreset=True)   # auto reset color after print

def delete_student(student_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM students123 WHERE id=%s", (student_id,))
    conn.commit()
    
    if cursor.rowcount > 0:
        print(Fore.GREEN + "✅ Student deleted successfully!" + Style.RESET_ALL)
    else:
        print(Fore.RED + "⚠️ Student not found." + Style.RESET_ALL)
    
    conn.close()
5

    
  
def menu():
    while True:
        print("\n====== Student Management System ======")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Search Student by ID")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            name = input("Enter name: ")
            age = int(input("Enter age: "))
            grade = input("Enter grade: ")
            add_student(name, age, grade)

        elif choice == "2":
            view_students()

        elif choice == "3":
            student_id = int(input("Enter Student ID: "))
            search_student(student_id)

        elif choice == "4":
            student_id = int(input("Enter Student ID to update: "))
            name = input("Enter new name: ")
            age = int(input("Enter new age: "))
            grade = input("Enter new grade: ")
            update_student(student_id, name, age, grade)

        elif choice == "5":
            student_id = int(input("Enter Student ID to delete: "))
            delete_student(student_id)

        elif choice == "6":
            print("Exiting...")
            break

        else:
            print("Invalid choice. Try again.")

menu()




