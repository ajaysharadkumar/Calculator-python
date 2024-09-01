def addition(x: int, y: int) -> int:
    return x + y


def subtraction(x: int, y: int) -> int:
    return abs(x - y)


def multiplication(x: int, y: int) -> int:
    return x * y


a = int(input("Enter the value a: "))
b = int(input("Enter the value b: "))

print(f"Addition of a two number is {addition(a, b)}")
print(f"Subtraction of a two number is {subtraction(a, b)}")
print(f"Multiplication of a two number is {multiplication(a, b)}")
