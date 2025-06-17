def substraction(a, b):
    return a - b

def addition(a, b):
    return a + b

def division(a, b):
    return a / b

def multiplication(a, b):
    return a * b

def exponentiation(a, b):
    return a ** b

def square_root(a, b):
    return a ** (1/b)







a =int(input("Enter a number:\n"))
b = int(input("Second number\n"))


c = int(input('Input a number from according to an operation you wish to perform\nSubstraction - 1\nAddition - 2\nDivision - 3\nMultiplication - 4\nExponentiation - 5\nSquare root - 6\n'))
match c:
    case 1:
        print(substraction(a, b))

    case 2:
        print(addition(a,b))
    
    case 3:
        print(division(a, b))
    
    case 4:
        print(multiplication(a, b))
    case 5:
        print(exponentiation(a, b))
    case 6:
        print(square_root(a, b))
    
    case _:
        print("invalid input")
    
