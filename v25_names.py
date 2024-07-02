def main():
    students = []
    with open("students.csv") as file:
        for line in file:
            name, house = line.rstrip().split(",")      # gives out an array
            # student = {}
            # student["name"] = name
            # student["house"] = house
            student = {"name": name, "house": house}
            students.append(student)

    def get_name(student):
        return student["name"]


    for student in sorted(students, key=get_name(), reverse=True):
        print(f"{student["name"]} is in {student["house"]}")

if __name__ == '__main__':
    main()

    # students = []
    # with open("students.csv") as file:
    #     for line in file:
    #         name, house = line.rstrip().split(",")      # gives out an array
    #         students.append(f"{name} is in {house}")    # a text is assigned to list; sorting based on name
    #
    # for student in sorted(students):
    #     print(student)


    # with open("students.csv") as file:
    #     for line in file:
    #         name, house = line.rstrip().split(",")      # gives out an array
    #         print(f"{name} is in {house}")
    #
    # with open("students.csv") as file:
    #     for line in file:
    #         row = line.rstrip().split(",")      # gives out an array
    #         print(f"{row[0]} is in {row[1]}")






    # with open("names.txt") as file:
    #     for line in sorted(file, reverse=True):
    #         print(f"Hello,", line.strip())





    # names = []
    #
    # with open("names.txt") as file:
    #     for line in file:
    #         names.append(line.strip())
    #
    # for name in sorted(names):
    #     print(f"Hello, {name}")






    # name = input("What's your name?")
    # with open("names.txt", "a") as file:
    #     file.write(f"{name}\n")


    # with open("names.txt", "r") as file:
    #     lines = file.readlines()
    #
    # for line in sorted(lines):
    #     print("Hello," + f"{line}" + "!", sep="", end="")

    # for line in lines:
    #     print(f"Hello, {line}")

    # names = []
    #
    # for _ in range(3):
    #     names.append(input("What is your name?"))
    #
    # for name in sorted(names):
    #     print(f"Hello, {name}")