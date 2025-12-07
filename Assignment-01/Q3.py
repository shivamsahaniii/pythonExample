#   Ask the user to enter two integers and one float. Convert them all to floats and print their average.

num1 = int(input("Enter first integer number: "))
num2 = int(input("Enter second integer number: "))
num3 = float(input("Enter a float number: "))

avg = (float(num1) +  float(num2) + num3) / 3

print(f"The average of {num1}, {num2} and {num3} is {avg}")