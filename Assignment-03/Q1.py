# Ask the user for a string and check whether it is a palindrome or not.
#   A palindrome is a string which is same when we read it forward & backward. Eg -
#       “madam”, “racecar” etc.
# [Hint - A palindrome string is equal to the reversed version of the string. We can
# use a loop to reverse the string manually. ]

word = input("Enter the word: ")
backword = ""
for latter in word:
    backword = latter + backword

if(word == backword):
    print(f"{word} and {backword} are Palindrome")
else:   
    print(f"{word} and {backword} are Not a Palindrome")