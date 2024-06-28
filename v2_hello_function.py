## Using a function to create "Hello, "
## 17/06/2024
def main():
    name = input("What is your name?")
    hello(name)
    hello()
    print(hello(name))

# def hello(to="world"):  # "world!" is the default value so for no input we have
#     print("Hello, ", to, "!", sep="", end="\n")
#     # Argument of hello has to be string
#     # Default value is "world!"
#     # if hello() is run with now argument
#     # it prints with a default value

# It is better to define functions with returning a value as opposed to just printing something
def hello(to="world"):  # "world!" is the default value so for no input we have
    return f"Hello, {to}"

if __name__ == '__main__':
    main()
