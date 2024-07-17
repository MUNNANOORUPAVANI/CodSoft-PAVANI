def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Division by zero is not allowed"
    else:
        return x / y

def power(x, y):
    return x ** y

def modulus(x, y):
    return x % y

def square(x):
    return x ** 2

def cube(x):
    return x ** 3

print("Select operation:")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
print("5.Power")
print("6.Modulus")
print("7.Square")
print("8.Cube")

while True:
    choice = input("Enter choice(1/2/3/4/5/6/7/8): ")

    if choice in ('1', '2', '3', '4', '5', '6'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))

        elif choice == '5':
            print(num1, "^", num2, "=", power(num1, num2))

        elif choice == '6':
            print(num1, "%", num2, "=", modulus(num1, num2))

    elif choice in ('7', '8'):
        num1 = float(input("Enter a number: "))

        if choice == '7':
            print("Square of", num1, "=", square(num1))

        elif choice == '8':
            print("Cube of", num1, "=", cube(num1))

    else:
        print("Invalid Input")
        break
