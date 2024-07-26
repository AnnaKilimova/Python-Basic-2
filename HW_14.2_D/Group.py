from Users import Human, Student
class Group:
    def __init__(self, number):
        self.number = number
        self.group = set()

    def add_student(self, student):
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