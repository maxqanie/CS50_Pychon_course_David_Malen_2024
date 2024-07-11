class Student:
    ...


def main():
    student = get_student3()
    if student["name"] == "Padma":
        student["house"] = "Ravenclaw"
    print(f"{student["name"]} is from {student["house"]}")


# def main():
#     student = get_student1()
#     if student[0] == "Padma":
#         student[1] = "Ravenclaw"
#     print(f"{student["name"]} is from {student["house"]}")


# (name, house) is tuple it is an immutable array; the output the function is still a value but a tuple
def get_student1():
    name = input("Name: ")
    house = input("House: ")
    return (name, house)


# Now the function outputs an array with immutable elements
def get_student2():
    name = input("Name: ")
    house = input("House: ")
    return [name, house]


# Now the function outputs an array with immutable elements
def get_student3():
    student = {}
    student["name"] = input("Name: ")
    student["house"] = input("House: ")
    return student


if __name__ == '__main__':
    main()
