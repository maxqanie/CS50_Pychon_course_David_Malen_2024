import csv


def main():
    students = []
    with open("students_v1.csv") as file:
        reader = csv.reader(file)
        for row in reader:
            students.append({"name": row[0], "home": row[1]})

    print(students)

    for student in sorted(students, key=lambda student: student["home"]):
        print(f"{student["name"]} is in {student["home"]}")




# ## Sorting a dictionry input
# def main():
#     students = []
#     with open("students_v0.csv") as file:
#         for line in file:
#             name, house = line.rstrip().split(",")      # gives out an array
#             student = {"name": name, "house": house}
#             students.append(student)
#     print(student)
#     print(students)
#     print(get_name)
#
#     # Passing the function: You pass get_name to sorted so that sorted can call it on each element
#     # Avoid using parentheses (get_name()) when passing a function as an argument unless you intend to call the
#     # function immediately and pass its return value
#
#     ## IMPORTANT
#     # it is a general rule in Python (and in many other programming languages) that when you want to pass a function
#     # as an argument to another function, you should pass the function itself (i.e., its reference or memory address)
#     # and not the result of calling the function. This allows the receiving function to call the passed function
#     # as needed.
#     # for student in sorted(students, key=get_name, reverse=False):
#     #     print(f"{student["name"]} is in {student["house"]}")
#
#     # Equivalent to above instead lambda is used for an anonymous function that is used once
#     # for multiple inputs we have lambda student, x, y,...:....
#     for student in sorted(students, key=lambda student: student["house"]):
#         print(f"{student["name"]} is in {student["house"]}")
#
#
#
# def get_name(student):
#     return student["name"]
#
# def get_house(student):
#     return student["house"]




if __name__ == '__main__':
    main()

    # students = []
    # with open("students_v0.csv") as file:
    #     for line in file:
    #         name, house = line.rstrip().split(",")      # gives out an array
    #         students.append(f"{name} is in {house}")    # a text is assigned to list; sorting based on name
    #
    # for student in sorted(students):
    #     print(student)


    # with open("students_v0.csv") as file:
    #     for line in file:
    #         name, house = line.rstrip().split(",")      # gives out an array
    #         print(f"{name} is in {house}")
    #
    # with open("students_v0.csv") as file:
    #     for line in file:
    #         row = line.rstrip().split(",")      # gives out an array
    #         print(f"{row[0]} is in {row[1]}")