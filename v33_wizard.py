class Wizard:
    def __init__(self, name):
        if not name:
            raise ValueError("Missing name")
        self.name = name

    ...

class Student(Wizard):
    def __init__(self, name, house):
        super().__init__(name)
        self.name = name
        self.house = house

    def __str__(self):
        return f"{self.name} from {self.house}"
    ...


class Professor(Wizard):
    def __init__(self, name, subject):
        super().__init__(name)
        self.name = name
        self.subject = subject

    def __str__(self):
        return f"{self.name} teaches {self.subject}"
    ...

wizard = Wizard("Albus")
student = Student("Harry", "Gryffindor")
professor = Professor("Severus", "Defense Against the Dark Arts")

print(student)
print(professor)



##################################################################################
# These two classes have one thing in common: get the name and check
# This commonality can be used to create another class called Wizard where the
# error checking will occur. This feature of class is called inheritance
# class Student:
#     def __init__(self, name, house):
#         if not name:
#             raise ValueError("Missing name")
#         self.name = name
#         self.house = house
#     ...
#
#
# class professor:
#     def __init__(self, name, subject):
#         if not name:
#             raise ValueError("Missing name")
#         self.name = name
#         self.subject = subject
#     ...


