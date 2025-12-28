#   Given a list of integers compute the average of all numbers in the list

marks = [89, 78, 90, 61, 99, 91, 80]
total = 0

for i in marks:
    total += i

count = len(marks)
avg = total / count
print(marks)
print(f"the Average of the given list is {avg}")