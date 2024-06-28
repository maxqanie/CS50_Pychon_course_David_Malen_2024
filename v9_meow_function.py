## Using loops with function

def main():
    meow(get_number())
def meow(i):
    for _ in range(i):
        print("mew")
def get_number():
    while True:
        n = int(input("n:"))
        if n > 0:
            return n

main()