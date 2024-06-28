## integer manipulation
## 17/06/2024




# Integer input
x = int(input("x:"))
y = int(input("y:"))
print(x + y)
# Float input
x = float(input("x:"))
y = float(input("y:"))
print(int(x + y))
Rounding: round(number, ndigits=None)
# Note the number of digits to be rounded is optional. None is always used for optionality

x = float(input("x:"))
y = float(input("y:"))
# z = round(x + y)
z = round(x / y, 2)
print(f"{z}")
print(f"{x/y:.4f}")
