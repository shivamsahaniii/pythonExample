#   The user enters a string containing a number (e.g., "45" ). Convert it to:
#       • an integer
#       • a float
#       • a string again
#       Print all three values with their types.

stringNum = input("Enter the value: ")

strintInt = int(stringNum)
strintFloat = float(stringNum)
strintStr = str(strintInt)

print(f"input in integer is {strintInt} and type is {type(strintInt)}")
print(f"input in float is {strintFloat} and type is {type(strintFloat)}")
print(f"input in string is {strintStr} and type is {type(strintStr)}")