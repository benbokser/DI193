# # Daily challenge: Old MacDonald’s Farm
# # Instructions: Old MacDonald’s Farm

# # You are given example code and output. Your task is to create a Farm class that produces the same output.


# # Step 1: Create the Farm Class
# #     Create a class called Farm.
# #     This class will represent a farm and its animals.


# # Step 2: Implement the __init__ Method
# #     The Farm class should have an __init__ method.
# #     It should take one parameter: farm_name.
# #     Inside __init__, create two attributes: name to store the farm’s name and animals to store the animals (initialize as an empty dictionary).
class Farm:
    def __init__(self, farm_name):
        self.name = farm_name
        self.animals = {}

# Step 3: Implement the add_animal Method
#     Create a method called add_animal.
#     It should take two parameters: animal_type and count (with a default value of 1). Count is the quantity of the animal that will be added to the animal dictionary.
#     The dictionary will look like this:
# {'cow': 1, 'pig':3, 'horse': 2}
#     If the animal_type already exists in the animals dictionary, increment its count by count.
#     If it doesn’t exist, add it to the dictionary as the key and with the given count as value.

    def add_animal(self, animal_type, count=1):
        if animal_type in self.animals:
            self.animals[animal_type] += count
        else:
            self.animals[animal_type] = count
# Step 8: upgrade the add_animal Method

#     use **kwargs for passing multiple animals. The keys will be the animal name and the value will be the quantity.
#     Then you can call the method this way: macdonald.add_animal('cow'= 5, 'sheep' = 2, 'goat' = 12)
# In this case I will add an additional add_animals method.
    def add_animals(self, **kwargs):
        for type, count in kwargs.items():
            if type in self.animals:
                self.animals[type] += count
            else:
                self.animals[type] = count
# Step 4: Implement the get_info Method

#     Create a method called get_info.
#     It should return a string that displays the farm’s name, the animals and their counts, and the “E-I-E-I-0!” phrase.
#     Format the output to match the provided example.
#     Use string formatting to align the animal names and counts into columns.
    def get_info(self):
        lines = []
        lines.append(f"{self.name}'s farm")
        lines.append("")
        if self.animals:
            max_len = max(len(name) for name in self.animals.keys())
            for name, count in self.animals.items():
                lines.append(f"{name:<{max_len}} : {count}")
            lines.append("")
        lines.append('    E-I-E-I-0!')
        return "\n".join(lines)

# Step 6: Implement the get_animal_types Method
#     Add a method called get_animal_types to the Farm class.
#     This method should return a sorted list of all animal types (keys from the animals dictionary).
#     Use the sorted() function to sort the list.
    def get_animal_types(self):
        return sorted(self.animals.keys())
# Step 7: Implement the get_short_info Method

#     Add a method called get_short_info to the Farm class.
#     This method should return a string like “McDonald’s farm has cows, goats and sheeps.”.
#     Call the get_animal_types method to get the list of animals.
#     Construct the string, adding an “s” to the animal name if its count is greater than 1.
#     Use string formatting to create the output.
    def get_short_info(self):
        types = self.get_animal_types()
        new_types = []
        for i in types:
            if i == 'sheep':
                new_types.append(i)
            elif self.animals[i] == 1:
                new_types.append('one ' + i)
            else:
                new_types.append(i + 's')
        if len(new_types) == 1:
            types_str = new_types[0]
        elif len(new_types) == 2:
            types_str = f'{new_types[0]} and {new_types[1]}'
        else:
            types_str = ''
            for i in range(len(new_types)-1):
                types_str = types_str + f'{new_types[i]}, '
            types_str = types_str + f'and {new_types[-1]}'
        return f"{self.name}'s farm has {types_str}."
# Step 5: Test Your Code

macdonald = Farm("McDonald")
macdonald.add_animal('cow', 5)
macdonald.add_animal('sheep')
macdonald.add_animal('sheep')
macdonald.add_animal('goat', 12)
macdonald.add_animal('chicken')
macdonald.add_animals(cow= 5, sheep = 2, goat = 12)
print(macdonald.get_info())
print(macdonald.get_animal_types())
print(macdonald.get_short_info())
# #output:
# # McDonald's farm

# # cow : 5
# # sheep : 2
# # goat : 12

# #     E-I-E-I-0!


# Bonus: Expand The Farm
#implemented above.
