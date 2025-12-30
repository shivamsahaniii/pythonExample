# Write a program to check whether two lists share no common elements.
# share no common elements list1 = [1, 2, 3, 4] list2 = [5, 6, 7, 8]
# share common elements list1 = [1, 2, 3] list2 = [3, 4]
# [Hint - use sets]

list1 = [1, 2, 3, 4]
list2 = [5, 6, 7, 8]

list3 = [1, 2, 3]
list4 = [3, 4]

# Case 1
common1 = set(list1).intersection(list2)
if common1:
    print("List1 and List2 share common elements:", common1)
else:
    print("List1 and List2 share NO common elements")

# Case 2
common2 = set(list3).intersection(list4)
if common2:
    print("List3 and List4 share common elements:", common2)
else:
    print("List3 and List4 share NO common elements")