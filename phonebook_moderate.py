running = True
CONTACT_FILE = "contact_list.txt"
# Killswitch operator

def read_file_into_array():
    contact_array = []
    # create an empty array to hold contacts read from file
    try:
        with open(CONTACT_FILE, 'r') as file:
            contacts = file.read().split(';')
            # open/create a file and split it's contents based on a ';'
        for i in range(len(contacts)):
            contact_array.append(contacts[i])
            # append each contact separeated by ';' to the contact array
        return contact_array
    except FileNotFoundError:
        # Accept a file error so the program will not crash
        return contact_array

def add_contact_handler(contact_array):
    # Handler called when user wants to add a new contact
    name = input("\nEnter the person's name:\n")
    number = input("Enter their phone number:\n")
    email = input("Enter their email address:\n")
    contact_list = [name, number, email]
    # Create a list of all information about one contact
    add_contact(contact_array, contact_list)
    # Call the function that will add contact information to the contact array

def add_contact(contact_array, contact):
    contact_array.append(str(contact))
    # Append a new contact as a string 
    print(f"{contact} has been addded.")
    write_array_to_file(contact_array)
    # Call the function that writes the updated contact array back to the file
    start_up()
    # Continue the main loop

def search_contact_handler(contact_array):
    # Handler called when the user wants to search a contact
    searched_contact = input("Please enter the name, phone number, or email address of the contact you wish to search\n> ").lower()
    search_contacts(contact_array, searched_contact)
    # Call the function that will search through the contact array for the searched contact

def search_contacts(contact_array, contact):
    i = 0
    # Initialize a counter for array index's
    for array in contact_array:
        i += 1
        # For each element in the contact array, increment the index counter by one
        if contact in array:
            # If the searched contact is in the found, search through all elements of the nested array for any searched element.
            # Whether that's the name, phone number, or email
            found_contact = contact_array[i-1]
            print(f"{found_contact} found.")
            # Declare and print the found contact using the contact array and the index value minus one from above

            return found_contact
    else:
        contact_not_found()
        # If not found, call the functoin that deals with a contact not being found
    
    start_up()
    # Regaurdless of whether it was found or not, continue the main loop
        
def delete_contact_handler(contact_array):
    # Handler responsible for deleting a specific contact from the contact array
    deleted_contact = input("Please enter the contact you with to delete.\n> ").lower()
    delete_contact(contact_array, deleted_contact)
    # Call the function that will process deleting the desired contact from the contact array

def delete_contact(contact_array, contact):
    contact_to_delete = search_contacts(contact_array, contact)
    # Ensure the desired contact to delete exists before attempting deletion
    if contact_to_delete:
        contact_array.remove(contact_to_delete)
        # If contact is found, remove it from the array
    print(f"\n{contact_to_delete} has been removed from your contacts list.")
    write_array_to_file(contact_array)
    start_up()
    # Write the updated contact array back to the file and then continue the main loop

    
def list_all_contacts(contact_array):
    for contact in contact_array:
        print(f"{contact}")
    # List all contacts (name, phone number, and email in an array) in the contact array 

def terminate(contact_array):
    global running 
    running = False
    start_up()
    # Function responsible for killing the program if the user presses 'q'

def write_array_to_file(contact_array):
    write_contact_array = ';'.join(contact_array)
    with open(CONTACT_FILE, 'w') as contacts:
        contacts.write(write_contact_array)
    # Pass in the contact array, erase what is in the file, and then write the updated contact array into the file

def menu_operation():
    operations = input("Choose which operation to execute.\nA)Add contact.\nB)Search contact.\nC)Delete contact.\nD)List all contacts.\nQ)Quit\n> ").lower()
    return operations
    # Output the main menu that the user chooses the operation from

options = {
        'a': add_contact_handler,
        'b': search_contact_handler,
        'c': delete_contact_handler,
        'd': list_all_contacts,
        'q': terminate
    }
    # Dictionary responsible for dealing with user input

def invalid_menu_input(contact_array):
    print("Please enter a valid selection")
    start_up()
    # Output to user when an invalid input is attempted. Continue running the main loop

def contact_not_found():
    print("This contact does not exist.")
    start_up()
    # If contact is not found, inform user and continue running the main loop

def start_up():
    while running:
        # Unless running is false (which only happens if the user enters q), run the start up logic
        operation = menu_operation()
        # Prompt the users input
        contact_array = read_file_into_array()
        # Create the contact array from the file
        options.get(operation, invalid_menu_input)(contact_array)
        # Use dictionary to call the correct function based on the users input
    
    
if __name__ =='__main__':
    start_up()