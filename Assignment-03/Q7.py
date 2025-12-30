# Write a program that takes a string from the user and prints the number of spaces in the string.

sentence = input("Enter the sentence: ")
count = 0

for word in sentence:
    if (word == " "):
        count += 1

print(f"the sentence ... {sentence} ... has {count} spaces..")