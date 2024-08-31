def addition(x, y):
    return x + y


def subtraction(x, y):
    return abs(x - y)


a = int(input("Enter the value a:"))
b = int(input("Enter the value b:"))

print(f"Addition of a two number is {addition(a, b)}")
print(f"Subtraction of a two number is {subtraction(a, b)}")
