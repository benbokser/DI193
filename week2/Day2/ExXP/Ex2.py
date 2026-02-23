# 🌟 Exercise 2: Dogs
# Goal: Create a Dog class with methods for barking, running speed, and fighting.

# Instructions:

# Step 1: Create the Dog Class
#     Create a class called Dog with name, age, and weight attributes.
#     Implement a bark() method that returns “<dog_name> is barking”.
#     Implement a run_speed() method that returns weight / age * 10.
#     Implement a fight(other_dog) method that returns a string indicating which dog won the fight, based on run_speed * weight.
class Dog:
    def __init__(self, name: str, age: int, weight: float):
        self.name = name
        self.age = age
        self.weight = weight

    def bark(self):
       return f'{self.name} is barking.'  

    def run_speed(self):
        return (self.weight / self.age)*10
    
    def fight(self, other_dog):
        if self.run_speed()*self.weight > other_dog.run_speed()*other_dog.weight:
            return(f'{self.name} wins!')
        elif self.run_speed()*self.weight < other_dog.run_speed()*other_dog.weight:
            return(f'{other_dog.name} wins!')
        elif self.run_speed()*self.weight == other_dog.run_speed()*other_dog.weight:
            return(f"It's a draw!")

# Step 2: Create Dog Instances

#     Create three instances of the Dog class with different names, ages, and weights.
dog1 = Dog('Rex', 8, 20)
dog2 = Dog('Socks', 3, 15)
dog3 = Dog('Roger', 4, 25)

# Step 3: Test Dog Methods
#     Call the bark(), run_speed(), and fight() methods on the dog instances to test their functionality.
print(dog1.bark())
print(dog2.run_speed())
print(dog1.fight(dog2))
print(dog2.fight(dog3))

