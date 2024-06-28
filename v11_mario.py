def main():
    size = int(input("Size:"))
    print_square(size)

def print_square(size):
    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()

def print_square(size):
    for i in range(size):
        print_row(size)

def print_row(width):
    print("#" * width)

def print_square(size):
    for i in range(size):
        print("#" * size)

main()