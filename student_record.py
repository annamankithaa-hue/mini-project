# Student Record System using Dictionary

students = {}

def add_student(roll_no, name, branch):
    students[roll_no] = {"Name": name, "Branch": branch}
    print(f"Student {name} added successfully!")

def display_students():
    if not students:
        print("No records found.")
    else:
        for roll_no, details in students.items():
            print(f"Roll No: {roll_no}, Name: {details['Name']}, Branch: {details['Branch']}")

def search_student(roll_no):
    if roll_no in students:
        print(f"Found: Roll No: {roll_no}, Name: {students[roll_no]['Name']}, Branch: {students[roll_no]['Branch']}")
    else:
        print("Student not found.")

# Example run
add_student(101, "Ankita", "ECE")
add_student(102, "Ravi", "CSE")
display_students()
search_student(101)
