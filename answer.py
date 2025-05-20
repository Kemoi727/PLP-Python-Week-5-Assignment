#Assignment 1: Design Your Own Class! 
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


