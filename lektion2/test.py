#funktion
def print_menu(menu_choice_number, message_string):
    choice_is_valid = menu_choice_number in [1, 2, 3, 4]
    if not choice_is_valid:
        print("Invalid choice.")
        return
    print(f"You selected option {menu_choice_number}. {message_string}.")

menu_choice = input("Enter a choice (1-3. 4 to quit): ")

menu_is_running = True

while menu_is_running:
    if menu_choice == '1':
        print_menu(1, "Home")
        break
    elif menu_choice == '2':
        print_menu(2, "Settings")
        break
    elif menu_choice == '3':
        print_menu(3, "Change channel")
        break
    elif menu_choice == '4':
        print_menu(4, "Turn off")
        menu_is_running = False
    else:
        print("Invalid choice.")
