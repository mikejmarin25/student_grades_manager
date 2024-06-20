class StudentGradesManager:
    def __init__(self):
        self.student_records = {}

    def add_student(self, name):
        if name in self.student_records:
            print(f"Student {name} already exists.")
        else:
            self.student_records[name] = []
            print(f"Student {name} added.")

    def add_grade(self, name, grade):
        if name not in self.student_records:
            print(f"Student {name} does not exist.")
        else:
            self.student_records[name].append(grade)
            print(f"Added grade {grade} for student {name}.")

    def calculate_average(self, name):
        if name not in self.student_records:
            print(f"Student {name} does not exist.")
        elif len(self.student_records[name]) == 0:
            print(f"No grades recorded for student {name}.")
        else:
            average = sum(self.student_records[name]) / len(self.student_records[name])
            print(f"Average grade for student {name} is {average:.2f}.")

    def display_all_students(self):
        if not self.student_records:
            print("No students in the record.")
        else:
            print("Student Records:")
            for name, grades in self.student_records.items():
                print(f"{name}: {grades}")


def main():
    manager = StudentGradesManager()

    while True:
        print("\nOptions:")
        print("1. Add Student")
        print("2. Add Grade")
        print("3. Calculate Average")
        print("4. Display All Students")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            name = input("Enter student's name: ")
            manager.add_student(name)
        elif choice == '2':
            name = input("Enter student's name: ")
            grade = float(input("Enter grade: "))
            manager.add_grade(name, grade)
        elif choice == '3':
            name = input("Enter student's name: ")
            manager.calculate_average(name)
        elif choice == '4':
            manager.display_all_students()
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
