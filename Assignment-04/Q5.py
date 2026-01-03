# Concept: Inheritance
# Q5. Create a base class Vehicle with attributes like brand and model.
# Create two subclasses Car and Bike that add extra attributes - seats (in Car) &
# engine_cc (in Bike).

class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def show_info(self):
        print(f"\nBrand: {self.brand}")
        print(f"Model: {self.model}")

class Car(Vehicle):
    def __init__(self, brand, model, seats):
        super().__init__(brand, model)
        self.seats = seats

    def show_info(self):
        super().show_info()
        print(f"Seats: {self.seats}")

class Bike(Vehicle):
    def __init__(self, brand, model, engine_cc):
        super().__init__(brand, model)
        self.engine_cc = engine_cc

    def show_info(self):
        super().show_info()
        print(f"Engine CC: {self.engine_cc}")

print("Choose vehicle:")
print("1. Bike")
print("2. Car")
choice = int(input("\nEnter your choice: "))

brand = input("\nEnter vehicle brand: ")
model = input("Enter vehicle model: ")

if choice == 1:
    cc = int(input("\nEnter engine CC: "))
    bike = Bike(brand, model, cc)
    bike.show_info()

elif choice == 2:
    seats = int(input("\nEnter number of seats: "))
    car = Car(brand, model, seats)
    car.show_info()

else:
    print("Invalid choice")