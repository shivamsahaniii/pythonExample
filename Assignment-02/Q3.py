# Write a function that prints the digits of a number, n .
# For eg: n = 312 , there are 3 digits in it 3, 1 and 2 & we need to print them.

# [Hint - The right most digit of a number N is N%10. 
# And to remove the right most digit from a number, we can do N = N / 10.]

# Output will look like 2  1  3

def digitsInNum(num):
    while num > 0:
        digit = num % 10
        print(f"{digit}")
        num = num // 10

# Output will look like 3  1  2
def inAssending(num):
    rev = 0
    while num > 0:
        rev = rev * 10 + ( num % 10)
        num = num // 10

    while rev > 0:
        print(rev % 10)
        rev = rev // 10 

num = int(input("Enter the number: "))

digitsInNum(num)
print("\n")
inAssending(num)