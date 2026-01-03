# | Concept: Abstraction
# Q6. Create an abstract class Employee with an abstract method calculate_salary().
# Create subclasses Intern, FullTimeEmployee, and Contract Employee that implement the method differently.

from abc import ABC, abstractmethod

class Employee(ABC):

    @abstractmethod
    def calculate_salary(self):
        pass

class Intern(Employee):
    def __init__(self, days_worked, daily_rate):
        self.days_worked = days_worked
        self.daily_rate = daily_rate

    def calculate_salary(self):
        return self.days_worked * self.daily_rate


class FullTimeEmployee(Employee):
    def __init__(self, days_worked, daily_rate, hra, tra):
        self.days_worked = days_worked
        self.daily_rate = daily_rate
        self.hra = hra
        self.tra = tra

    def calculate_salary(self):
        return (self.days_worked * self.daily_rate) + self.hra + self.tra


class ContractEmployee(Employee):
    def __init__(self, days_worked, daily_rate, hra, tra, contract_years):
        self.days_worked = days_worked
        self.daily_rate = daily_rate
        self.hra = hra
        self.tra = tra
        self.contract_years = contract_years

    def calculate_salary(self):
        return (self.days_worked * self.daily_rate) + self.hra + self.tra

print("Choose employment type:")
print("1. Intern")
print("2. Full Time Employee")
print("3. Contract Employee")

choice = int(input("Enter your choice: "))

match choice:
    case 1:
        emp = Intern(20, 600)
    case 2:
        emp = FullTimeEmployee(26, 1500, 5000, 5000)
    case 3:
        emp = ContractEmployee(24, 1200, 3000, 3000, 2)
    case _:
        print("Invalid option")
        exit()

salary = emp.calculate_salary()
print(f"Total Salary: {salary}")