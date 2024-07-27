students = [
    {"Name" : "Padma", "house" : "Ravenclaw", "Patronous" : "Otter"},
    {"Name" : "Cho", "house" : "Hufflepuff", "Patronous" : "Otter"},
    {"Name" : "Hermione", "house" : "Gryffindor", "Patronous" : "Otter"},
    {"Name" : "Harry", "house" : "Gryffindor", "Patronous" : "Otter"},
    {"Name" : "Ron", "house" : "Gryffindor", "Patronous" : "Jack Russell Terrier"},
    {"Name" : "Draco", "house" : "Slytherin", "Patronous" : None},
]


houses = set()
for student in students:
    houses.add(student["house"])

for house in sorted(houses):
    print(house)

# houses = []
# for student in students:
#     if student["house"] not in houses:
#         houses.append(student["house"])
#
#
# for house in sorted(houses):
#     print(house)