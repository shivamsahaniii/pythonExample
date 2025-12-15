#   Write a function to return the sum of digits of a number, n .

def calculateSum(num):
    sum = 0
    while num > 0:
        digit = num % 10
        sum += digit
        num = num // 10

    return sum
    
num = int(input("Enter the number: "))
print(f"the sum of digit of {num} is {calculateSum(num)}")