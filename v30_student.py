## class is a data type and a blue print for an object
## It is like defining a type like integer or float in C but it allows us to
## control the parameter a lot easier than dictionaries and lists
## Object is instanciation of a class
## class Student(): is enough to define a class
## classes are mutable and immutable
## name and house are the attributes of the class
## An object is the instance of the class where can have two attributes

# Instance of a Class: An object is an instance of a class. A class is like
# a blueprint or template, and an object is a specific realization of that blueprint.
class Student:
    # name, house in def __init__ are instance variables
    # self allows us to store the variables (parameters) in the current object of the class
    # self gives you access to the current object that was just created
    # class is a function that creates an objects with certain attributes and variables

    # def __init__ is a function within the class
    def __init__(self, name, house):
        self.name = name
        self.house = house

# # Python allows dynamic attribute assignment. This means that you
# can add attributes to an instance of a class after the instance
# has been created, even if the class definition itself does not
# explicitly define those attributes.
# class Student():
#     ...
def main():
    student = get_student()
    print(f"{student.name} is from {student.house}")


# More powerful form of creating attributes
def get_student():
    name = input("Name: ")
    house = input("House: ")
    # constructor call: it is going to instantiate and construct a student object
    # It is using Student class as a mold or template so that every student is structured the same but
    # because I can pass arguments to the Student function, I can customize the content of the object
    # the Class is a function
    student = Student(name, house)
    print(student)  # publishes the memory location of the object
    print(id(student))  # id of a class
    print(type(student))  # <class '__main__.Student'>
    return student




#############################################################
# # the basic format of a class
# def get_student():
#     student = Student()
#     student.name = input("Name: ")
#     student.house = input("House: ")
#     return student
#############################################################
## main function for get_student3
# def main():
#     student = get_student3()
#     if student["name"] == "Padma":
#         student["house"] = "Ravenclaw"
#     print(f"{student["name"]} is from {student["house"]}")

## main function for get_student1
# def main():
#     student = get_student1()
#     if student[0] == "Padma":
#         student[1] = "Ravenclaw"
#     print(f"{student["name"]} is from {student["house"]}")


# # (name, house) is tuple it is an immutable array; the output the function is still a value but a tuple
# def get_student1():
#     name = input("Name: ")
#     house = input("House: ")
#     return (name, house)
#
#
# # Now the function outputs an array with immutable elements
# def get_student2():
#     name = input("Name: ")
#     house = input("House: ")
#     return [name, house]
#
#
# # Now the function outputs an array with immutable elements
# def get_student3():
#     student = {}
#     student["name"] = input("Name: ")
#     student["house"] = input("House: ")
#     return student


if __name__ == '__main__':
    main()
