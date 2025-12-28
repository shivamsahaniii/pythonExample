# Input two lists of integers from the user. Merge them into one list and sort the result.

# Eg - list1 = [1, 2, 7] , list2 = [3, 4, 5]
# result = [1, 2, 3, 4, 5, 7]

list1 = list(map(int, input("Enter the first list: ").split()))
list2 = list(map(int, input("Enter the second list: ").split()))
newlist = []

for i in list1:
    newlist.append(i)

for i in list2:
    newlist.append(i)

newlist.sort()
print(newlist)


# list1 = list(map(int, input("Enter the first list: ").split()))
# list2 = list(map(int, input("Enter the second list: ").split()))

# result = sorted(list1 + list2)
# print(result)