class Student:
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course

student = Student("Sneha", 20, "Computer Science")

print(vars(student))
