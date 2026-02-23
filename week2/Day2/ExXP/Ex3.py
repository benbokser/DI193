# 🌟 Exercise 3: Dogs Domesticated
# Goal: Create a PetDog class that inherits from Dog and adds training and tricks.
# Instructions:

# Step 1: Import the Dog Class
#     In a new Python file, import the Dog class from the previous exercise.
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

# Step 2: Create the PetDog Class

#     Create a class called PetDog that inherits from the Dog class.
#     Add a trained attribute to the __init__ method, with a default value of False.
#     trained means that the dog is trained to do some tricks.
class PetDog(Dog):
    def __init__(self, name, age, weight):
        super().__init__(name, age, weight)
        self.trained = False
#     Implement a train() method that prints the output of bark() and sets trained to True.
    def train(self):
        print(self.bark())
        self.trained = True
#     Implement a play(*args) method that prints “<dog_names> all play together”.
#     *args on this method is a list of dog instances.
    def play(self, *args: Dog):
        dog_list = [self] + list(args)
        name_list = [dog.name for dog in dog_list]
        print(f'{', '.join(name_list)} all play together.')

#     Implement a do_a_trick() method that prints a random trick if trained is True.
#     Use this list for the ramdom tricks:
#     tricks = ["does a barrel roll", "stands on his back legs", "shakes your hand", "plays dead"]
#     Choose a random index from it each time the method is called.
    def do_a_trick(self):
        import random
        if self.trained:
            tricks = ["does a barrel roll", "stands on his back legs", "shakes your hand", "plays dead"]
            print(f"{self.name} {random.choice(tricks)}.")

# Step 3: Test PetDog Methods

#     Create instances of the PetDog class and test the train(), play(*args), and do_a_trick() methods.
petdog1 = PetDog('Sally', 5, 20)
petdog2 = PetDog('Jack', 3, 22)
petdog3 = PetDog('Joe', 8, 30)

petdog1.train()
petdog2.train()
petdog1.play(petdog2, petdog3)
petdog1.do_a_trick()
petdog2.do_a_trick()