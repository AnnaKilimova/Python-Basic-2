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

    def __hash__(self):
        return hash(str(self))

    def __str__(self):
        return f'{self.gender} {self.age} {self.first_name} {self.last_name} {self.record_book}'

    def __eq__(self, other):
        if isinstance(other, Student):
            return self.last_name == other.last_name