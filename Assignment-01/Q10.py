#   Take a decimal number as input (like 45.78 ) and output its:
#       • integer part - 45
#       • fractional part - .78

num = input("Enter a decimal number: ")
parts = num.split(".")

integer_part = parts[0]
fractional_part = "." + parts[1]

print("Integer part:", integer_part)
print("Fractional part:", fractional_part)