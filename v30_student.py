# properties is an attribute that allows to control the class defensively
class Student:
    def __init__(self, name, house):
        self.name = name
        self.house = house

    def __str__(self):
        return f"{self.name} from {self.house}"

    # the purpose of getter and setters is that we have created functions that get and set attributes within a class
    # These functions streamline the parameter setting in a class so those attributes cannot be controlled from
    # outside the class. In this way, we can error check them within these functions
    # Remember the objective of using getter and setter is that I could verify the attribute values if a user tries
    # to change parameters from outside a class
    # Using getter and setter enable control over
    # that object so that you can just trust that it's going to be correct as
    # designed Using a getter and Setter really just enables python to
    # automatically detect when you're trying to manually set a value
    # The equal sign and the dot as I've highlighted here is enough of a clue to python to realize
    # wait a minute you're trying to set a value let me see if this class has a
    # Setter defined and if so I'm going to call that and I'm not just going to

    # Setter and getter have _ in their parameter

    # Getter
    # Getter only gets one argument: self
    @property
    def house(self):
        return self._house

    # Setter
    @house.setter
    def house(self, house):
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid House")
        self._house = house
    # Note that house is the variable that comes from the user as an input while self.house is instant variable
    # set aside in memory to store attributes aka name and house in this program

    @property
    def name(self):
        return self._name

    # Setter
    @name.setter
    def name(self, name):
        if not name:
            raise ValueError("Missing name")
        self._name = name

# You can still access instance variables. We read the attributes and change them if we want. There is nothing
# stopping us from changing name or house from outside the class

def main():
    student = get_student()
    student.house = "Slytherin"
    print(student)


def get_student():
    name = input("Name: ")
    house = input("House: ")
    return Student(name, house)


############################################################
# Creating a method in a class and accessing to it outside of class
# class Student:
#     def __init__(self, name, house, patronus):
#         if not name:
#             raise ValueError("Missing name")
#         if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
#             raise ValueError("Invalid House")
#         self.name = name
#         self.house = house
#         self.patronus = patronus
#
#     def __str__(self):
#         return f"{self.name} from {self.house}"
#
#
#     def charm(self):
#         match self.patronus:
#             case "Stag":
#                 return "🐴"
#             case "Otter":
#                 return "🦦"
#             case "Jack Russel terrier":
#                 return "🐶"
#             case _:
#                 return "🪄"
# def main():
#     student = get_student()
#     print("Expecto Patronum!")
#     print(student.charm())
#
#
# def get_student():
#     name = input("Name: ")
#     house = input("House: ")
#     patronus = input("Patronus: ")
#     return Student(name, house, patronus)

#############################################################
# ## class is a data type and a blueprint for an object
# ## It is like defining a type like integer or float in C but it allows us to
# ## control the parameter a lot easier than dictionaries and lists
# ## Object is instanciation of a class
# ## class Student(): is enough to define a class
# ## classes are mutable and immutable
# ## name and house are the attributes of the class
# ## An object is the instance of the class where can have two attributes
#
# # Instance of a Class: An object is an instance of a class. A class is like
# # a blueprint or template, and an object is a specific realization of that blueprint.
# class Student:
#     # name, house in def __init__ are instance variables
#     # self allows us to store the variables (parameters) in the current object of the class
#     # self gives you access to the current object that was just created
#     # class is a function that creates an objects with certain attributes and variables
#
#     # def __init__ is a function within the class
#     def __init__(self, name, house, patronus):
#         # Checking for errors
#         if not name:
#             raise ValueError("Missing name")
#         if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
#             raise ValueError("Invalid House")
#         self.name = name
#         self.house = house
#         self.patronus = patronus
#
#     def __str__(self):
#         return f"{self.name} from {self.house}"
#
#
# # # Python allows dynamic attribute assignment. This means that you
# # can add attributes to an instance of a class after the instance
# # has been created, even if the class definition itself does not
# # explicitly define those attributes.
# # class Student():
# #     ...
# def main():
#     student = get_student()
#     # if we print the instance, it will output the memory address unless __str__(self) is defined
#     print(student)
#     # print(f"{student.name} is from {student.house}")
#
#
# # More powerful form of creating attributes
# def get_student():
#     name = input("Name: ")
#     house = input("House: ")
#     patronus = input("Patronus: ")
#     # constructor call: it is going to instantiate and construct a student object
#     # It is using Student class as a mold or template so that every student is structured the same but
#     # because I can pass arguments to the Student function, I can customize the content of the object
#     # the Class is a function
#     student = Student(name, house, patronus)
#     # print(student)  # publishes the memory location of the object
#     # print(id(student))  # id of a class
#     # print(type(student))  # <class '__main__.Student'>
#     return student

#############################################################
# # the basic format of a class
# def get_student():
#     student = Student()
#     student.name = input("Name: ")
#     student.house = input("House: ")
#     return student
#############################################################
# main function for get_student3
# def main():
#     student = get_student3()
#     if student["name"] == "Padma":
#         student["house"] = "Ravenclaw"
#     print(f"{student["name"]} is from {student["house"]}")

# main function for get_student1
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
