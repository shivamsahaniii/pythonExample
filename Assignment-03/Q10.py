# Ask the user for a string and print:
# • All unique characters
# • The count of unique characters
word = input("Enter the string: ").lower()

seen = set()
duplicates = set()

for ch in word:
    if(ch != " "):
        if ch in seen:
            duplicates.add(ch)
        else:
            seen.add(ch)

unique = seen - duplicates

print(f"All unique characters: {unique}")
print(f"Count of unique characters: {len(unique)}")