# This feature is called operator overloading where we are using a method that allows and defines
# new operators. In the method below, the grogram allows for creation of two objects of the class
# and addition of its respective instance variablws. Note that we defined "+" to do addition we could
# defined it differently.
class Vault:
    # you can initialize the class with default values for the parameters
    def __init__(self, galleons = 0, sickles = 0, knuts = 0):
        self.galleons = galleons
        self.sickles = sickles
        self.knuts = knuts


    def __str__(self):
        return f"{self.galleons} Galleons, {self.sickles} Sickles, {self.knuts} Knuts"


    # you can address the class from within the class
    def __add__(self, other):
        galleons = self.galleons + other.galleons
        sickles = self.sickles + other.sickles
        knuts = self.knuts + other.knuts
        return Vault(galleons, sickles, knuts)


# Though defined for two objects, Python does dissecting so that there are always two objects
potter = Vault(100, 50, 25)
weasley = Vault(25, 50, 100)
ginger = Vault(75, 100, 75)

total = potter + weasley + ginger
print(total)