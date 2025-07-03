
from calcApp import add, subtract, multiply, divide
from config import APP_NAME

def main():
    print(f"Welcome to {APP_NAME}!")
    a, b = 10, 5
    print(f"{a} + {b} = {add(a, b)}")
    print(f"{a} - {b} = {subtract(a, b)}")
    print(f"{a} * {b} = {multiply(a, b)}")
    print(f"{a} / {b} = {divide(a, b)}")

if __name__ == "__main__":
    main()
