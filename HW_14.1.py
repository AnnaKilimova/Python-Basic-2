class Human:
    def __init__(self, gender, age, first_name, last_name):
        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f'{self.gender}, {self.age}, {self.first_name} {self.last_name}'

class Student(Human):
    def __init__(self, gender, age, first_name, last_name, record_book):
        super().__init__(gender, age, first_name, last_name)
        self.record_book = record_book

    def __str__(self):
        return f'{self.gender} {self.age} {self.first_name} {self.last_name} {self.record_book}'

class AddingStudentException(Exception):
    def __init__(self, message="Can not add more than 10 students"):
        self.message = message
        super().__init__(self.message)

class Group:
    def __init__(self, number):
        self.number = number
        self.group = set()

    def add_student(self, student):
        if len(self.group) >= 10:
            raise AddingStudentException()
        self.group.add(student)

    def delete_student(self, last_name):
        if self.find_student(last_name) != None:
            for i in self.group:
                if last_name in str(i):
                    self.group.discard(i)
                    return self.group

    def find_student(self, last_name):
        for student in self.group:
            if last_name in str(student):
                return student

    def __str__(self):
        all_students = ''
        self.number = 0
        for count in self.group:
            self.number += 1
            all_students += f' {count}.'
        return f'Number:{self.number}\\n {all_students} '

st1 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
st2 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')
st3 = Student('Male', 30, 'Steve', 'Smith', 'AN143')
st4 = Student('Female', 25, 'Liza', 'Wilson', 'AN144')
st5 = Student('Male', 30, 'Steve', 'Johnson', 'AN146')
st6 = Student('Male', 30, 'Steve', 'Wright', 'AN147')
st7 = Student('Female', 25, 'Liza', 'White', 'AN148')
st8 = Student('Male', 30, 'Steve', 'Green', 'AN149')
st9 = Student('Female', 25, 'Liza', 'Scott', 'AN150')
st10 = Student('Male', 30, 'Steve', 'Long', 'AN151')
st11 = Student('Male', 30, 'Steve', 'Aaron', 'AN151')
st12 = Student('Male', 30, 'Steve', 'Baron', 'AN151')

gr = Group('PD1')

try:
    gr.add_student(st1)
    gr.add_student(st2)
    gr.add_student(st2)
    gr.add_student(st3)
    gr.add_student(st4)
    gr.add_student(st5)
    gr.add_student(st6)
    gr.add_student(st7)
    gr.add_student(st8)
    gr.add_student(st9)
    gr.add_student(st10)
    gr.add_student(st11)
except AddingStudentException as e:
    print(e)

print(gr)
assert str(gr.find_student('Jobs')) == str(st1), 'Test1'
assert gr.find_student('Jobs2') is None, 'Test2'
assert isinstance(gr.find_student('Jobs'), Student) is True, 'Метод поиска должен возвращать экземпляр'

gr.delete_student('Taylor')
print(gr)  # Only one student

gr.delete_student('Taylor')  # No error!