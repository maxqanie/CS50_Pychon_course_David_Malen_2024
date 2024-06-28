def main():
    x = int(input("x:"))
    if is_even(x):
        print("Even")
    else:
        print("Odd")

def is_even(n):
    return (n % 2 == 0)


def is_even1(n):
    return True if (n % 2 == 0) else False

def is_even2(n):
    if (n % 2 == 0):
        return True
    else:
        return False

main()
# if x%2 == 0:
#     print("Even")
# else:
#     print("Odd")


