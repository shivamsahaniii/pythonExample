#   Write a program to print all numbers from 1 to 100 that are divisible by both 3 and 5.

print(f"the number divisible my 3 and 5 are: ")
for i in range(1, 101):
    if (i % 3 == 0 and i % 5 == 0):
        print(i)