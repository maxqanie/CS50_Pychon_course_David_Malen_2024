## List and dictionary creation

students = ["Harry", "Hermione", "Ronald"]
for student in students:
    print(student)

print(len(students))
for i in range(len(students)):
    print(i + 1, students[i])
#
students = {
    "Harry" : "Gryffindor",
    "Hermione" : "Gryffindor",
    "Ron" : "G ryffindor",
    "Draco" : "Gryffindor",
}
print(students["Harry"])
for student in students:
    print(student, students[student])


students = [
    {"Name" : "Hermione", "House" : "Gryffindor", "Patronous" : "Otter"},
    {"Name" : "Harry", "House" : "Gryffindor", "Patronous" : "Otter"},
    {"Name" : "Ron", "House" : "Gryffindor", "Patronous" : "Jack Russell Terrier"},
    {"Name" : "Draco", "House" : "Slytherin", "Patronous" : None},
]

for student in students:
    print(student[""])
    print(student["Name"], student["House"], sep=", ")