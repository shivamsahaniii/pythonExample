# . Let’s create a “Number Guessing Game”. Given a secret number 
#       (already decided by you), write a program that asks the user to guess it and prints:
# • "Too high" if the guess is above the number
# • "Too low" if the guess is below
# • "Correct!" if the guess matches

# def guessNumer():
#     num = 17

#     while True:
#         number = int(input("Enter the number: "))

#         if(number > num):
#             print(f"Too high")
#         elif(number < num):
#             print(f"Too low")
#         else:
#             print(f"Correct!")
#             return

# guessNumer()


def guess_number():
    secret = 17
    while (guess := int(input("Enter your guess: "))) != secret:
        print("Too high" if guess > secret else "Too low")
    print("Correct!")

guess_number()