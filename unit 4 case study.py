# Student Record Lookup System
# Using Hash Table with Separate Chaining

class Student:
    def __init__(self, roll_no, name, marks):
        self.roll_no = roll_no
        self.name = name
        self.marks = marks


class StudentHashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(size)]

    # Hash function
    def hash_function(self, roll_no):
        return roll_no % self.size

    # Add student
    def add_student(self, roll_no, name, marks):
        index = self.hash_function(roll_no)

        for student in self.table[index]:
            if student.roll_no == roll_no:
                student.name = name
                student.marks = marks
                print("Student record updated!")
                return

        student = Student(roll_no, name, marks)
        self.table[index].append(student)
        print("Student added successfully!")

    # Search student
    def search_student(self, roll_no):
        index = self.hash_function(roll_no)

        for student in self.table[index]:
            if student.roll_no == roll_no:
                print("\nStudent Found")
                print("Roll Number:", student.roll_no)
                print("Name:", student.name)
                print("Marks:", student.marks)
                return

        print("Student not found!")

    # Delete student
    def delete_student(self, roll_no):
        index = self.hash_function(roll_no)

        for student in self.table[index]:
            if student.roll_no == roll_no:
                self.table[index].remove(student)
                print("Student deleted successfully!")
                return

        print("Student not found!")

    # Display all students
    def display_students(self):
        print("\nStudent Records")
        found = False

        for bucket in self.table:
            for student in bucket:
                print(
                    "Roll No:", student.roll_no,
                    "| Name:", student.name,
                    "| Marks:", student.marks
                )
                found = True

        if not found:
            print("No student records available.")


# Main program
students = StudentHashTable()

while True:
    print("\n===== STUDENT RECORD SYSTEM =====")
    print("1. Add Student")
    print("2. Search Student")
    print("3. Delete Student")
    print("4. Display All Students")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        try:
            roll_no = int(input("Enter roll number: "))
            name = input("Enter student name: ").strip()
            marks = float(input("Enter marks: "))

            if roll_no < 0 or not name or not 0 <= marks <= 100:
                print("Enter valid roll number, name, and marks (0-100).")
            else:
                students.add_student(roll_no, name, marks)
        except ValueError:
            print("Please enter valid numeric values.")

    elif choice == "2":
        try:
            roll_no = int(input("Enter roll number to search: "))
            students.search_student(roll_no)
        except ValueError:
            print("Roll number must be an integer.")

    elif choice == "3":
        try:
            roll_no = int(input("Enter roll number to delete: "))
            students.delete_student(roll_no)
        except ValueError:
            print("Roll number must be an integer.")

    elif choice == "4":
        students.display_students()

    elif choice == "5":
        print("Student Record System Closed.")
        break

    else:
        print("Invalid choice! Please try again.")