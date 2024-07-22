# Instance Methods:
# Associated with an instance of a class.
# Use self as the first parameter.
# Can access and modify instance data and class data.
# Called on instances of the class.
#
#
# Class Methods:
# Associated with the class itself.
# Use cls as the first parameter.
# Can access and modify class-level data, but not instance data.
# Called on the class itself or instances of the class.
# Defined with the @classmethod decorator.
# Key Differences:
#
# First Parameter: self for instance methods, cls for class methods.
# Access: Instance methods access both instance and class data, class methods only access class data.
# Usage: Instance methods for operations related to an instance, class methods for operations related to the class as
# a whole.
class Student:
    def __init__(self, name, house):
        self.name = name
        self.house = house

    def __str__(self):
        return f"{self.name} from {self.house}"

    @property
    def house(self):
        return self._house

    # Setter
    @house.setter
    def house(self, house):
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid House")
        self._house = house

    @property
    def name(self):
        return self._name

    # Setter
    @name.setter
    def name(self, name):
        if not name:
            raise ValueError("Missing name")
        self._name = name

    @classmethod
    def get_student(cls):
        name = input("Name: ")
        house = input("House: ")
        return cls(name, house)


def main():
    print(Student.get_student())


if __name__ == '__main__':
    main()