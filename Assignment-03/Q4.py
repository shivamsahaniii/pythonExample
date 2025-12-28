# Given a tuple of integers, create:
#   • A tuple of all even numbers
#   • A tuple of all odd numbers

tup = (1, 43, 23, 65, 87, 33, 44, 56, 89, 21, 75, 35, 66, 58, 88, 90)
eventup = ()
oddtup = ()
for i in tup:
    if(i % 2 == 0):
        eventup += (i,)
    else:
        oddtup += (i,)

    # eventup = tuple(i for i in tup if i % 2 == 0)
    # oddtup = tuple(i for i in tup if i % 2 != 0)

print(f"Even tuple: {eventup}")
print(f"Odd tuple: {oddtup}")   