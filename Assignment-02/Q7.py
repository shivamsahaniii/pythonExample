#   Design a program to continuously input a number n from user & print if it is positive or negative until the user enters “Quit”.

while True:
    data = input("Enter your input: ")

    if(data == "Quit"):
        print(f"come again to play")
        break

    num = int(data)

    if(num > 0):
        print(f"{num} is positive number")
    elif(num < 0):
        print(f"{num} is negative number")
    else:
        print("it's a zero")