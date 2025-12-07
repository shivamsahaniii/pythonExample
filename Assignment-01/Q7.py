#   Ask the user for a temperature in Celsius (string input). Convert it to float , then calculate and print temperature in Fahrenheit.

temp = input("Enter the temperature in Celsius: ")
flotemp = float(temp)
fahrentemp = (flotemp * (9/5)) + 32

print(f"the {temp} in Celsius is {fahrentemp} in Fehrenheit.")