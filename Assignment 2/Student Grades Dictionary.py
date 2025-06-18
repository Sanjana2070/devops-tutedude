<<<<<<< HEAD
# Student Grades Dictionary
students = {}

while True:
    print("\n1. Add student")
    print("2. Update student grade")
    print("3. Print all grades")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter student name: ")
        grade = input("Enter grade: ")
        students[name] = grade
        print(f"{name} added.")
    elif choice == "2":
        name = input("Enter student name to update: ")
        if name in students:
            grade = input("Enter new grade: ")
            students[name] = grade
            print(f"{name}'s grade updated.")
        else:
            print("Student not found.")
    elif choice == "3":
        print("\nStudent Grades:")
        for name, grade in students.items():
            print(f"{name}: {grade}")
    elif choice == "4":
        break
    else:
        print("Invalid choice.")
=======
# Student Grades Dictionary
students = {}

while True:
    print("\n1. Add student")
    print("2. Update student grade")
    print("3. Print all grades")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter student name: ")
        grade = input("Enter grade: ")
        students[name] = grade
        print(f"{name} added.")
    elif choice == "2":
        name = input("Enter student name to update: ")
        if name in students:
            grade = input("Enter new grade: ")
            students[name] = grade
            print(f"{name}'s grade updated.")
        else:
            print("Student not found.")
    elif choice == "3":
        print("\nStudent Grades:")
        for name, grade in students.items():
            print(f"{name}: {grade}")
    elif choice == "4":
        break
    else:
        print("Invalid choice.")
>>>>>>> af418ba (Assignment 5)
