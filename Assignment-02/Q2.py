# Write a function that takes two integers a and b and prints all even numbers between them (inclusive).

def betweenEven(startNum, endNum):

    print(f"the even number in between {startNum} and {endNum} are: ")
    for i in range(startNum, endNum, 1):
        if(i%2 == 0):
            print(f"{i}")

startNum = int(input("Enter stating number: "))
endNum = int(input("Enter ending number: "))

betweenEven(startNum, endNum)