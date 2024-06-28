## Loops

i = 3
while i != 0:
    print("meow")
    i -= 1


for i in [1, 2, 3]:
    print("meow")

for i in range(3):
    print("meow")

for _ in range(3):
    print("meow")

print("meow\n" * 3, end="")

while True:
    n = int(input("n:"))
    if n > 0:
        break
print("meow\n" * n, end="")