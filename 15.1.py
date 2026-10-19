
class MaxStudentsError(Exception):
    """Пользовательское исключение: превышено количество студентов."""
    pass


class Student:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name


class Group:
    def __init__(self, name):
        self.name = name
        self.students = []

    def add_student(self, student):
        if len(self.students) >= 10:
            raise MaxStudentsError(
                "В группе не может быть больше 10 студентов!"
            )

        self.students.append(student)
        print(f"Студент {student.name} добавлен в группу.")

    def show_students(self):
        print(f"\nГруппа {self.name}:")
        for student in self.students:
            print(student)


# Создаём группу
group = Group("ИТ-101")

# Добавляем 11 студентов
try:
    for i in range(1, 12):
        student = Student(f"Студент {i}")
        group.add_student(student)
except MaxStudentsError as error:
    print(f"Ошибка: {error}")

# Выводим список студентов
group.show_students()

