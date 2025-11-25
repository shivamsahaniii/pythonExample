num1 = int(input("Enter the 1st number: "))
num2 = int(input("Enter the 2nd number: "))

print("The numbers before swapping: ", num1, num2)

num3 = num2
num2 = num1 
num1 = num3

print("The numbers after swapping: ", num1, num2)
