#Activity 1: 
# Base class
class Superhero:
    def __init__(self, name, power, age):
        self.name = name
        self.power = power
        self.age = age

    def introduce(self):
        return f"I am {self.name}, I have the power of {self.power}."

    def use_power(self):
        return f"{self.name} uses {self.power}!"

# Subclass with inheritance and polymorphism
class FlyingSuperhero(Superhero):
    def __init__(self, name, power, age, flying_speed):
        super().__init__(name, power, age)
        self.flying_speed = flying_speed  # New attribute

    # Override the use_power method (polymorphism)
    def use_power(self):
        return f"{self.name} flies at {self.flying_speed} km/h while using {self.power}!"

# Create instances
hero1 = Superhero("Invisible Shadow", "Invisibility", 28)
hero2 = FlyingSuperhero("Sky Blaze", "Fire Manipulation", 32, 250)

# Test methods
print(hero1.introduce())
print(hero1.use_power())

print(hero2.introduce())
print(hero2.use_power())


#Activity 2
# Base class (optional, but good for structure)
class Vehicle:
    def move(self):
        pass  # To be overridden by subclasses

# Car class
class Car(Vehicle):
    def move(self):
        print("Driving 🚗")

# Plane class
class Plane(Vehicle):
    def move(self):
        print("Flying ✈️")

# Boat class
class Boat(Vehicle):
    def move(self):
        print("Sailing ⛵")

# Function to demonstrate polymorphism
def let_it_move(vehicle):
    vehicle.move()

# Create instances
car = Car()
plane = Plane()
boat = Boat()

# Call move() on each instance using the same function
let_it_move(car)    # Output: Driving 🚗
let_it_move(plane)  # Output: Flying ✈️
let_it_move(boat)   # Output: Sailing ⛵


