#   Ask the user for: Principal (P), Rate (R), Time (T). Convert all to float and compute simple interest: SI = (P ∗ R ∗ T)/100

principal = int(input("Enter the principal amount: "))
rate = float(input("Enter the rate of return: "))
time = int(input("Enter the number of year: "))

floPrincipal = float(principal)
floTime = float(time)
simpleInterest = (floPrincipal * rate * floTime) / 100

print(f"Your simple interest is {simpleInterest}")