# Given a list of words:
# words = ["apple", "banana", "kiwi", "cherry", "mango"]
# Create a dictionary that maps each word to its length.
# Example:
# {"apple": 5, "banana": 6, "kiwi": 4, ...}

words = ["apple", "banana", "kiwi", "cherry", "mango"]

dicWord = {}

for word in words:
    dicWord[word] = len(word)   

print(f"{words} \nwords after converting them into dictionary \n{dicWord}")
