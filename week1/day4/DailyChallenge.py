# Coffee Shop Menu Manager

# Initial data
menu = {
    "espresso": 7.0,
    "latte": 12.0,
    "cappuccino": 10.0
}

def show_menu(menu_dict):
    """Print all drinks and prices."""
    if menu_dict == {}:
        print("The menu is empty.")
    else:
        for key, value in menu_dict.items():
            print(f'{key} - {value}₪')



def add_item(menu_dict):
    """Add a new drink to the menu."""
    new_drink = input('Enter new drink name:')
    if new_drink in menu_dict:
        print('Item already exists!')
    else:
        price = float(input('Enter price:'))
        menu_dict[new_drink] = price
        print(f'{new_drink} added!')





def update_price(menu_dict):
    """Change the price of an existing drink."""
    drink = input('Which drink would you like to update?')
    if drink not in menu_dict:
        print('Item not found.')
    else:
        new_price = float(input('Enter new price:'))
        menu_dict[drink] = new_price
        print('Price updated!')




def delete_item(menu_dict):
    """Remove a drink from the menu."""
    drink = input('Which drink would you like to remove?')
    if drink not in menu_dict:
        print('Item not found.')
    else:
        del menu_dict[drink]
        print('Item deleted.')


def show_options():
    """Print the available actions."""
    print('''What would you like to do?
1. Show menu
2. Add item
3. Update price
4. Delete item
5. Exit''')


def run_coffee_shop():
    """Main loop of the program."""
    # TODO
    while True:
        show_options()
        choice = input('Enter your choice(1-5):')
        if choice == '1':
            show_menu(menu)
        elif choice == '2':
            add_item(menu)
        elif choice == '3':
            update_price(menu)
        elif choice == '4':
            delete_item(menu)
        elif choice == '5':
            print('Goodbye!')
            break
        else:
            print('Invalid choice, try again.')
    


# Start the program
run_coffee_shop()