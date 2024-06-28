def main():
    hello("world")
    goodbye("world")

def hello(name):
    print(f"Hello, {name}!")


def goodbye(name):
    print(f"Goodbye, {name}")
# This ensures that main is run only from within v20_sayings.py file
if __name__ == "__main__":
    main()