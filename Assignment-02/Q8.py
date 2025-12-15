#   Let’s create a Simple Calculator that performs arithmetic operations. Create
#   a function calculator(a, b, operation) that performs addition, subtraction,
#   multiplication, or division based on the operation parameter.
#   [ operation parameter can have values ‘+’ , ‘-’ , '*’ & ‘/’ .

def calculator(a, b , operation):
    match(operation):
        case '+':
            print(f"the addition of {a} and {b} is {a + b} \n") 
        case '-':
            print(f"the subtraction of {a} and {b} is {a -b } \n")
        case '*':
            print(f"the multiplication of {a} and {b} is {a * b} \n")
        case '/':
            print(f"the division of {a} and {b} is {a / b} \n")
        case _:
            print("wrong input")

while True:
    num1 = int(input("Enter first number: "))
    print("Enter the operation.. ‘+’ , ‘-’ , '*’ & ‘/’  ")
    operation = input("Enter the input one of above.:  ")
    num2 = int(input("Enter second number: "))

    calculator(num1, num2, operation)

    start = input("Do you want to calculate again (Yes ot No): ")
    if(start == 'No'):
        print(f"come again to play")
        break