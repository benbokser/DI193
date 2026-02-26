# The file should contain a class called MenuManager, with the following functions:
import json
class MenuManager:
#     __init__() - The function should read the menu from the restaurant_menu.json file and store it in a variable called menu.
    def __init__(self):
        with open("restaurant_menu.json", "r") as f:
            menu = json.load(f)
            self.menu = menu
#     add_item(name, price) – this method should add an item to the menu, although do not save the changes to the file yet.
    def add_item(self, name, price):
        self.menu['items'].append({'name': name, 'price': price})
#     remove_item(name) – if the item is in the menu, this function should remove it from the menu (and again do not save the changes to the file yet) and return True. If the item was not in the menu, return False. (Hint: use Python’s del operator).
    def remove_item(self, name):
        for item in self.menu['items']:
            if item['name'] == name:
                del item
                return True
        return False
                
#     save_to_file() - When the manager is finished updating the menu this function should be called and it should save all the updates and write them into the the restaurant_menu.json file (ie. the file which holds the menu).
    def save_to_file(self):
        with open("restaurant_menu.json", "w") as f:
            json.dump(self.menu, f, indent=2)