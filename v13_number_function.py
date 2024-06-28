## Exceptions with functions

def main():
    x = get_int("x:")
    print(f"x is {x}")

def get_int():
    while True:
        try:
            y = int(input("y:"))
            return y
        except ValueError:
            print("y must be an integer!")

def get_int():
    while True:
        try:
            return int(input("y:"))
        except ValueError:
            print("y must be an integer!")

def get_int():
    while True:
        try:
            return int(input("y:"))
        except ValueError:
            pass
def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            pass
main()