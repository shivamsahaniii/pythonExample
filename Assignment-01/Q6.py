#   Write a program to swap values of two numbers entered by the user

num1 = int(input("Enter the 1st number: "))
num2 = int(input("Enter the 2nd number: "))

print(f"The numbers before swapping is {num1} and {num2}")

num3 = num2
num2 = num1 
num1 = num3

print(f"The numbers after swapping is {num1} and {num2}")
