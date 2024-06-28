## Using a function to create to an arrithmatics operation
## 17/06/2024

def main():
    x = int(input("x: "))
    print("x square is ", square(x))

def square(n):
    return pow(n, 2)

# instead of main():
if __name__ == "__main__":
    main()