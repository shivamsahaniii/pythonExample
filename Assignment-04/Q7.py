# Concept: Constructor Overloading (with Default Parameters)
# Q7. Create a class Person that allows the constructor to work with:
# • name only
# • name + age
# • name + age + address
# As direct constructor overloading (multiple constructors) are not allowed but
# we have to use default parameters to simulate constructor overloading.

class Person:
    def __init__(self, name, age=None, address=None):
        self.name = name
        self.age = age
        self.address = address

        if age is None and address is None:
            print(f"Initializing {self.name} with name only.")
        elif address is None:
            print(f"Initializing {self.name} with name and age {self.age}.")
        else:
            print(f"Initializing {self.name} with name, age {self.age}, and address {self.address}.")

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}, Address: {self.address}\n"

shivam = Person('Shivam')
print(shivam)

shivansh = Person('Shivansh', age=20)
print(shivansh)

archit = Person('Archit', age=22, address='Tanashi')
print(archit)