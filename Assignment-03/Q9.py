# Given a list, print all elements that appear more than once in the list.
# [Hint - use sets]

list1 = [1, 2, 4, 6, 3, 7, 5, 4, 2, 9, 1, 6, 3, 9, 0]

seen = set()
duplicates = set()

for i in list1:
    if i in seen:
        duplicates.add(i)
    else:
        seen.add(i)

print(duplicates)