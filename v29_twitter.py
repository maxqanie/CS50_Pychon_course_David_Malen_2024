import re

url = input("URL: ").strip()


# Twitter does not accept all characters in username
if matches := re.search(r"^(?:https?://(?:www\.)?)?twitter\.com/([a-z0-9_])$",url, re.IGNORECASE):
    print(f"Username:", matches.group(1))
else:
    print("Not a valid entry")


# Adding flexibility to domain
if matches := re.search(r"^(?:https?://(?:www\.)?)?twitter\.(.+)/(.+)$",url, re.IGNORECASE):
    if matches.group(1) == "com":
        print(f"Username:", matches.group(1))
else:
    print("Not a valid entry")


# Use of non-capturing feature of parentheses
# (?:....)
if matches := re.search(r"^(?:https?://(?:www\.)?)?twitter\.com/(.+)$",url, re.IGNORECASE):
    print(f"Username:", matches.group(1))
else:
    print("Not a valid entry")


# Use of wulrase operator
if matches := re.search(r"^(https?://(www\.)?)?twitter\.com/(.+)$",url, re.IGNORECASE):
    print(f"Username:", matches.group(3))
else:
    print("Not a valid entry")

# Ensure twitter.com is first entered
# Note that every pair of parentheses you use will be captured to save the info
# It does not matter if we use ? or not
matches = re.search(r"^(https?://(www\.)?)?twitter\.com/(.+)$",url, re.IGNORECASE)
if matches:
    print(f"Username:", matches.group(3))
else:
    print("Not a valid entry!")


# instead of replace we use re (regex)
username = re.sub(r"^(https?://(www\.)?)?twitter\.com/", "", url)
print(f"username: {username}")


# To not touch the input from the user
username = url.removeprefix("https://twitter.com/")
print(f"Username: {username}")


# this is to extract the username from the url
username = url.replace("https://twitter.com/","")
print(f"Username: {username}")