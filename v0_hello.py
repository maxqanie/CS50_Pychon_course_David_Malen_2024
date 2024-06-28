## string manipulation
## 17/06/2024



# Ask users for their name
name = input("What is your name?")
# Say hello to user
## v1
print("Hello, " + name +"!")
## v2
print("Hello,", name, "!")


# Tampering with print(*objects, sep=' ', end='\n', file=None, flush=False) as a function
# Between each comma, the separator is one blank space
# print() will end with going to the next line as shown by \n

## v3
print("Hello, ", end="")
print(name, sep="", end="")
print("!")

## v4
print("Hello, ", name, "!", sep="")

## v5
print("Hello, ", name, sep="", end="!\n")

## v6
print(f"Hello, {name}!")


## printing quatation marks
print("Hello, \"friend\"!")
print('Hello, "friend"!')

# Removing empty blanks
name = name.strip()
print(f"Hello, {name}!")

# Capitalizing the first letter
name = name.capitalize()
print(f"Hello, {name}!")
# Capitalizing all names
name = name.title()
print(f"Hello, {name}!")

name = input("What is your name?").strip().title()
print(f"Hello, {name}!")

first, middle1, middle2, middle3, middle4, last = name.split(" ")
print(f"{middle1}, {middle2}, {middle3}")



