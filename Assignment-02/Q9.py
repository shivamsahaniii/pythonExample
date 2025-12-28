#   Write a function is_prime(n) that returns True if n is a prime number and False otherwise, using a loop.
# [Hint -
# 1. We only check prime for 2 or numbers greater than 2. 2 is the smallest
# prime number.
# 2. A non-Prime number, n , will always get divided by atleast one number in
# range [2, n-1].
# Eg - For number 9 we’ll check in range (2, 8) & it’ll get divided by 3. So 9 is
# non-prime & we’ll return false for it.
# For number 7 we’ll check in range (2, 6) & it won’t get divided by any. So 7
# is prime & we’ll return true for it. ]

def is_prime(n):
    if n <= 1:
        return False
    for num in range(2, n-1):
        if(n % num == 0):
            return False
    return True
        
num = int(input("Enter the number: "))
print(f"{is_prime(num)}")