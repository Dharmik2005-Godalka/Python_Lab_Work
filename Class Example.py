class Car:
    # Constructor
    def __init__(self, brand, model):
        self.brand = brand  # Attribute
        self.model = model  # Attribute

    # Method 
    def car_details(self):
        return f"Car: {self.brand}, Model: {self.model}"

# object
my_car = Car("Toyota", "Corolla")
print(my_car.car_details())
