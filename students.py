# student_management.py

students = []  # list to store student records

def add_student():
    roll = input("Enter Roll Number: ")
    name = input("Enter Name: ")
    age = input("Enter Age: ")
    course = input("Enter Course: ")
    
    student = {
        "roll": roll,
        "name": name,
        "age": age,
        "course": course
    }
    students.append(student)
    print("✅ Student added successfully!\n")

def view_students():
    if not students:
        print("⚠ No students found!\n")
        return
    print("\n--- Student List ---")
    for s in students:
        print(f"Roll: {s['roll']}, Name: {s['name']}, Age: {s['age']}, Course: {s['course']}")
    print()

def search_student():
    roll = input("Enter Roll Number to Search: ")
    for s in students:
        if s["roll"] == roll:
            print(f"✅ Found: Roll: {s['roll']}, Name: {s['name']}, Age: {s['age']}, Course: {s['course']}\n")
            return
    print("❌ Student not found!\n")

def update_student():
    roll = input("Enter Roll Number to Update: ")
    for s in students:
        if s["roll"] == roll:
            print("Enter new details (leave blank to keep old value):")
            name = input(f"Name ({s['name']}): ") or s['name']
            age = input(f"Age ({s['age']}): ") or s['age']
            course = input(f"Course ({s['course']}): ") or s['course']
            s.update({"name": name, "age": age, "course": course})
            print("✅ Student updated successfully!\n")
            return
    print("❌ Student not found!\n")

def delete_student():
    roll = input("Enter Roll Number to Delete: ")
    for s in students:
        if s["roll"] == roll:
            students.remove(s)
            print("✅ Student deleted successfully!\n")
            return
    print("❌ Student not found!\n")

def menu():
    while True:
        print("====== Student Management System ======")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")
        
        choice = input("Enter choice (1-6): ")
        
        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            update_student()
        elif choice == "5":
            delete_student()
        elif choice == "6":
            print("👋 Exiting... Goodbye!")
            break
        else:
            print("⚠ Invalid choice! Try again.\n")

if __name__ == "__main__":
    menu()
