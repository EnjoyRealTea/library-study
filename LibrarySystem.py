# ============================================== Case Study 05 =========================================================
# ========================================= Library Management System ==================================================
# *********************************************** E. Thompson **********************************************************

def add_user(user_name):
    # Function to add a new library user
    if user_name in users_list.keys():
        print(f"{user_name} is already a library member.")
    elif not user_name.isalpha():
        print("Error: Invalid username (must be a single word).")
    else:
        users_list[user_name] = {'Books on loan': [], 'Outstanding Fines': 0, 'Rewards': 0, 'Limit': 3}
        print(f"{user_name} successfully added to the library system.")


def check_out(user_name, book_title):
    # Function to record a book moving from stock to a user
    if library_inventory[book_title]['Copies in stock'] == 0:
        print(f"Error: {book_title} is out of stock.")
    elif len(users_list[user_name]['Books on loan']) >= users_list[user_name]['Limit']:
        print(f"Error: {user_name} has reached their borrowing limit.")
    elif users_list[user_name]['Outstanding Fines'] != 0:
        print(f"Error: {user_name} has outstanding fines to be paid before borrowing.")
    else:
        library_inventory[book_title]['Copies in stock'] -= 1
        library_inventory[book_title]['Current borrowers'].append(user_name)
        users_list[user_name]['Books on loan'].append(book_title)
        print(f"'{book_title}' successfully checked out.")


def check_in(book_title, user_name):
    # Function to record a book moving from a user back to library stock
    if book_title in users_list[user_name]['Books on loan']:
        library_inventory[book_title]['Copies in stock'] += 1
        library_inventory[book_title]['Current borrowers'].remove(user_name)
        users_list[user_name]['Books on loan'].remove(book_title)
        print(f"{book_title} successfully returned.")
        fine_or_reward(user_name)
    else:
        print(f"Error: {user_name} did not check '{book_title}' out.")


def pay_fine(user_name):
    # Function to record that a fine has been paid
    if users_list[user_name]['Outstanding Fines'] > 0:
        users_list[user_name]['Outstanding Fines'] -= 1
        print(f"Fine successfully paid: {user_name} has {users_list[user_name]['Outstanding Fines']} "
              f"outstanding fines to pay.")
    else:
        print(f"Error: {user_name} does not have any fines to pay.")


def fine_or_reward(user_name):
    # Function to give a user a fine for a late return, or a reward if it is on time.
    # If the user collects 10 rewards, their borrowing limit is increased. A fine resets their limit and rewards.
    # However, they cannot increase their borrowing limit beyond 6 books.
    while True:
        on_time = input("Was the book returned on time? (Y/N)").upper()
        if on_time == 'N':
            users_list[user_name]['Outstanding Fines'] += 1
            users_list[user_name]['Limit'] = 3
            users_list[user_name]['Rewards'] = 0
            break
        elif on_time == 'Y':
            users_list[user_name]['Rewards'] += 1
            if users_list[user_name]['Rewards'] > 9 and users_list[user_name]['Limit'] < 6:
                users_list[user_name]['Limit'] += 1
                print(f"Congratulations to {user_name}! They have earned 10 rewards and can now borrow"
                      f" {users_list[user_name]['Limit']} books!")
                users_list[user_name]['Rewards'] = 0
            break
        else:
            print("Error: Invalid input. Please enter Y or N.")


def get_member():
    # Function to get a valid member's name from the user
    while True:
        name = input("Please enter the member's name: ").capitalize()
        if name in users_list.keys():
            return name
        else:
            print(f"Error: Library member {name} not found.")


def get_book():
    # Function to get a valid book title from the user
    while True:
        user_book = input("Please enter the book title (To see a list, enter 0):").capitalize()
        if user_book == '0':
            for item in library_inventory.keys():
                print(item)
        elif user_book in library_inventory.keys():
            return user_book
        else:
            print(f"Error: '{user_book}' was not found in the system.")


def show_records(library_dictionary):
    # Displays all records for the user
    for items, values in library_dictionary.items():
        print(items)
        for status, value in values.items():
            print(f"\t{status}: {value}")


# -----------------------------------------------------------
# Information about the library users and their current statuses:
users_list = {'Brian': {'Books on loan': [], 'Outstanding Fines': 0, 'Rewards': 9, 'Limit': 3},
              'Wendy': {'Books on loan': [], 'Outstanding Fines': 0, 'Rewards': 9, 'Limit': 6},
              'Jenny': {'Books on loan': [], 'Outstanding Fines': 2, 'Rewards': 0, 'Limit': 3}}

# Inventory of books held by the library and the location of copies:
library_inventory = {
    'Deadly fiction': {'Copies in stock': 4, 'Current borrowers': []},
    'History of the world': {'Copies in stock': 2, 'Current borrowers': []},
    'Banana cookbook': {'Copies in stock': 1, 'Current borrowers': []},
    'How to breed chipmunks': {'Copies in stock': 3, 'Current borrowers': []},
    'Superstar': {'Copies in stock': 6, 'Current borrowers': []}
}

print("Welcome to the Library Management System")

# Provide the user with the list of options for the library system:
while True:
    print("""
Please select from the following options:
1. Add a new library member to the system
2. Check out a book
3. Return a book
4. Pay a fine
5. View current book stock
6. View library members
7. Exit
""")
    user_choice = input("Please enter your choice (1-7):")

    # -----------------------------------------------------------
    if user_choice == '7':
        # Exit system
        break
    # -----------------------------------------------------------
    elif user_choice == '1':
        # Add a new member to the system
        user = input("Please enter the new member's name: ").capitalize()
        add_user(user)
    # -----------------------------------------------------------
    elif user_choice == '2':
        # Check out a book
        check_out(get_member(), get_book())
    # -----------------------------------------------------------
    elif user_choice == '3':
        # Return a book
        check_in(get_book(), get_member())
    # -----------------------------------------------------------
    elif user_choice == '4':
        # Pay a fine
        pay_fine(get_member())
    # -----------------------------------------------------------
    elif user_choice == '5':
        print("\nCurrent Library Inventory Status:")
        show_records(library_inventory)
    # -----------------------------------------------------------
    elif user_choice == '6':
        print("\nCurrent Library Member List:")
        show_records(users_list)
    # -----------------------------------------------------------
    else:
        print("Error: Please enter a number between 1 and 7.")
