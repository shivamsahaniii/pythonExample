#Ask the user to enter two integers and one float. Convert them all to floats and print their average.

print("Please enter two integers and one float")

num1 = int(input("Enter 1st integer number:"))
num2 = int(input("Enter 2nd integer number:"))
num3 = float(input("Enter 1st float number:"))

avg = (float(num1)+float(num2)+num3)/3
print("The average of", num1, ",", num2, "and", num3, "is", avg)