import csv
import os
class Student:
    def __init__(self,student_id,name,grades):
        self.student_id = student_id
        self.name = name
        self.grades = grades
    def __str__(self):
        return f'ID: {self.student_id} | Name: {self.name} | Grades: {self.grades}'
class StudentManager:
    def __init__(self,filename="students.csv"):
        self.filename = filename
        self.students = self.load_students()
    def load_students(self):
        students = []
        if os.path.exists(self.filename):
            with open(self.filename, mode='r', newline='') as file:
                reader = csv.reader(file)
                next(reader) 
                for row in reader:
                    student = Student(row[0], row[1], row[2])
                    students.append(student)
        return students 
    def save_students(self):
        with open(self.filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["ID", "Name", "Grade"])  
            for student in self.students:
                writer.writerow([student.student_id, student.name, student.grades])
    def add_student(self, student_id, name, grades):
        if any(student.student_id == student_id for student in self.students):
            print(f"Error: Student ID {student_id} already exists!")
            return False
        new_student = Student(student_id, name, grades)
        self.students.append(new_student)
        self.save_students()
        print(f"Student {name} added successfully!")
        return True
    def update_student(self, student_id, name=None, grades=None):
        for student in self.students:
            if student.student_id == student_id:
                if name:
                    student.name = name
                if grades:
                    student.grades = grades
                self.save_students()
                print(f"Student ID {student_id} updated successfully!")
                return True
        print(f"Error: Student ID {student_id} not found!")
        return False
    def delete_student(self, student_id):
        for student in self.students:
            if student.student_id == student_id:
                self.students.remove(student)
                self.save_students()
                print(f"Student ID {student_id} deleted successfully!")
                return True
        print(f"Error: Student ID {student_id} not found!")
        return False
    def list_students(self):
        if not self.students:
            print("No students found.")
            return
        print("Student Records:")
        for student in self.students:
            print(student)
def menu():
    manager = StudentManager()    
    while True:
        print("\nStudent Management System")
        print("1. Add Student")
        print("2. Update Student")
        print("3. Delete Student")
        print("4. List Students")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            student_id = input("Enter student ID: ")
            name = input("Enter student name: ")
            grade = input("Enter student grade: ")
            manager.add_student(student_id, name, grade)       
        elif choice == '2':
            student_id = input("Enter student ID to update: ")
            name = input("Enter new name (leave blank to keep current): ")
            grade = input("Enter new grade (leave blank to keep current): ")
            manager.update_student(student_id, name, grade)       
        elif choice == '3':
            student_id = input("Enter student ID to delete: ")
            manager.delete_student(student_id)       
        elif choice == '4':
            manager.list_students()       
        elif choice == '5':
            print("Exiting the program.")
            break      
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    menu()

