# Write a program that takes salary as input. Using conditional statements, calculate the final tax rate based on these rules.
#   • If salary < 30,000 → 5%
#   • If salary is 30,000–70,000 → 15%
#   • If salary > 70,000 → 25%

salary = int(input("Enter your salary: "))
    
if(salary < 30_000):
    finalTax = (salary * 5) / 100
    print(f"your final tax is: {finalTax}")

elif(salary >= 30_000 and salary <= 70_000):
    finalTax = (salary * 15) / 100
    print(f"your final tax is: {finalTax}")

else:
    finalTax = (salary * 25) / 100
    print(f"your final tax is: {finalTax}")


