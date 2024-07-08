import re

print(r"You are \n \. Gorgeous!")      # r (raw) reads the data as it reads
print("You are \nGorgeous!")        # reads \n as going to the next line
email = input("What is your email?")

# question marks allows optionality 0 or 1 repetition
if re.search(r"^(\w)+@(\w+\.)*\w+\.edu$", email, re.IGNORECASE):
    print("Valid")
else:
    print("Invalid")


# case insensitive
if re.search(r"^(\w|\s|[.])+@(\w|\s|[.])+\.edu$", email, re.IGNORECASE):
    print("Valid")
else:
    print("Invalid")

# lower case enfored
if re.search(r"^(\w|\s|[.])+@(\w|\s|[.])+\.edu$", email.lower()):
    print("Valid")
else:
    print("Invalid")

# space and . included
if re.search(r"^(\w|\s|[.])+@(\w|\s|[.])+\.edu$", email):
    print("Valid")
else:
    print("Invalid")
#
# # space included
# if re.search(r"^[a-zA-Z0-9_ ]+@[a-zA-Z_ ]+\.edu$", email):
#     print("Valid")
# else:
#     print("Invalid")
#
# # alpha numeric input
# if re.search(r"\w+@\w+\.(edu|com|org|ir|net|gov|ca)$", email):
#     print("Valid")
# else:
#     print("Invalid")
#
#
# # \w: alpha numeric \s space included \d decimal
# # compliment are capital letters
# if re.search(r"\S\w+@\S\w+\.edu$", email):
#     print("Valid")
# else:
#     print("Invalid")
#     # ^ matches the end of the string and $ matches the end of the string
#     # In "^.+@.+\.edu$" the program checks if the string user inputs directly addresses the email
#
#
# # alpha numeric input
# if re.search(r"^[a-zA-Z0-9_]+@[a-zA-Z_]+\.edu$", email):
#     print("Valid")
# else:
#     print("Invalid")
#     # ^ matches the end of the string and $ matches the end of the string
#     # In "^.+@.+\.edu$" the program checks if the string user inputs directly addresses the email
#
#
# if re.search(r"^[^@]+@[^@]+\.edu$", email):
#     print("Valid")
# else:
#     print("Invalid")

# username, domain = email.split("@")

# if (username) and domain.endswith(".edu"):
#     print("Valid")
# else:
#     print("Invalid")
#
# if (username) and ("." in domain):
#     print("Valid")
# else:
#     print("Invalid")
#
#
# if '@' in email and '.' in email:
#     print("Valid")
# else:
#     print("Invalid")

