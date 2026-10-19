
from student import Student
from exceptions import MaxStudentsError


class Group:
    MAX_STUDENTS = 10

    def __init__(self, name):
        self.name = name
        self.students = []

    def add_student(self, student):
        if not isinstance(student, Student):
            raise TypeError("Можно добавлять только объекты класса Student.")

        if len(self.students) >= self.MAX_STUDENTS:
            raise MaxStudentsError(
                "В группе не может быть больше 10 студентов!"
            )

        self.students.append(student)

    def find_student(self, search_value):
        for student in self.students:
            if search_value in str(student):
                return student
        return None

    def delete_student(self, last_name):
        for student in self.students:
            if student.last_name == last_name:
                self.students.remove(student)
                return

        print(f"Студент с фамилией {last_name} не найден.")

    def __str__(self):
        if not self.students:
            return f"Группа {self.name} пуста."

        students_list = "\n".join(
            str(student) for student in self.students
        )
        return f"Группа {self.name}:\n{students_list}"
