import re

# Shrinking the code: if you want python to find sth and also ensures it exists in a
# single line, walrus sign := is used
name = input("What is your name?").strip()
if matches := re.search(r"^(.+), ?(.+)$", name):
    name = matches.group(2) + " " + matches.group(1)
print(f"hello, {name}")

# making space after comma optional
# you cannot put it in parantheses since it will be collected
name = input("What is your name?").strip()
matches = re.search(r"^(.+), ?(.+)$", name)
if matches:
    name = matches.group(2) + " " + matches.group(1)
print(f"hello, {name}")

# Using particular spacing
name = input("What is your name?").strip()
matches = re.search(r"^(.+), (.+)$", name)
if matches:
    name = matches.group(2) + " " + matches.group(1)
print(f"hello, {name}")

# Using particular spacing
name = input("What is your name?").strip()
matches = re.search(r"^(.+), (.+)$", name)
if matches:
    last = matches.group(1)
    first = matches.group(2)
    name = f"{first} {last}"
print(f"hello, {name}")

# # re.search allows the get matches if using ()
# # every expression in () will be
# # .+ enforces matching of at least one character (any)
# name = input("What is your name?").strip()
# matches = re.search(r"^(.+), (.+)$", name)
# if matches:
#     last, first = matches.groups(2)
#     name = f"{first} {last}"
# print(f"hello, {name}")


# name = input("What is your name?").strip()
# if "," in name:
#     last, first = name.split(", ")
#     name = f"{first} {last}"
# print(f"hello, {name}")
