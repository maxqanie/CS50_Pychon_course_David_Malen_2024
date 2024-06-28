try:
    x = int(input("x:"))
except ValueError:
    print("x must be an integer!")
else:
    print(f"x is {x}")


while True:
    try:
        y = int(input("y:"))
    except ValueError:
        print("y must be an integer!")
    else:
        break
print(f"y is {y}")


while True:
    try:
        y = int(input("y:"))
        break
    except ValueError:
        print("y must be an integer!")
print(f"y is {y}")