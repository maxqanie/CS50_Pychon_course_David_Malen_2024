import random


# houses is a general constant which is a list
# Unlike instance variable, which is defined with self. and can change (be given attributes), houses is fixed in
# memory and cannot be changed from outside the class
class Hat:
    houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]

    # classmethod allows us to access the method without defining an instance
    @classmethod
    def sort(cls, name):
        house = random.choice(cls.houses)
        print(name, "is in", house)



Hat.sort("Harry")

# class Hat:
#     def __init__(self):
#         self.houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]
#     def sort(self, name):
#         house = random.choice(self.houses)
#         print(name, "is in", house)
#
#
#
# hat = Hat()
# hat.sort("Harry")
