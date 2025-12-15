#   Write a function to return the count the number of digits in a number, n 

def numCount(num):
    count = 0
    while num > 0:
        count += 1
        num = num // 10
        print(num)

    return count

num = int(input("Enter the number: "))
print(f"{num} has {numCount(num)} digits in it.")