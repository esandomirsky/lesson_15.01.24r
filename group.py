class OverStudentError(Exception):
    pass

class Group:
    max_student = 10

    def __init__(self, number):
        self.number = number
        self.group = set()

    def add_student(self, student):
        if len(self.group) >= self.max_student:
            raise OverStudentError("Cannot add more than 10 students to the group")
        self.group.add(student)

    def delete_student(self, last_name):
        student_to_delete = self.find_student(last_name)
        if student_to_delete:
            self.group.remove(student_to_delete)
            print(f"{student_to_delete.first_name} {student_to_delete.last_name} has been deleted.")
        else:
            print("Student not found in the group.")

    def find_student(self, last_name):
        for student in self.group:
            if student.last_name == last_name:
                return student
        return None

    def __str__(self):
        all_students = '\n'.join([str(student) for student in self.group])
        return f"Number:{self.number}\n{all_students}"