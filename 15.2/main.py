
from student import Student
from group import Group
from exceptions import MaxStudentsError


st1 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
st2 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')

gr = Group('PD1')

gr.add_student(st1)
gr.add_student(st2)

print(gr)

# Проверка поиска студента
assert gr.find_student('Jobs') == st1
assert gr.find_student('Jobs2') is None

# Удаление студента
gr.delete_student('Taylor')

print("\nПосле удаления студента:")
print(gr)

# Проверка ограничения в 10 студентов
try:
    for i in range(3, 13):
        student = Student(
            'Unknown', 20, f'Student{i}', f'Test{i}', f'AN{i}'
        )
        gr.add_student(student)

except MaxStudentsError as error:
    print(f"\nОшибка: {error}")

print("\nИтоговый состав группы:")
print(gr)
