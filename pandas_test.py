# Import necessary libraries
import os
import pandas as pd

# Initialize a global variable to control the program execution
running = True

# Define a lambda function 'cls' to clear the console screen
cls = lambda: os.system('cls')


class PassMan:
    def __init__(self):
        # Define a dictionary of options, mapping user inputs to corresponding methods
        self.options = {
            'a': self.add,
            'b': lambda: self.find_index(1),
            'c': lambda: self.find_index(2),
            'd': self.list_func,
            'q': self.terminate
        }
        # Flag to track whether the data file is new
        self.new_file = False

    def add(self): # A
        # Prompt the user to input fields for a new service
        temp_dict = self.input_fields()

        # Append the newly created dictionary to the list of service data
        self.data_dict_list.append(temp_dict)

        # Update the file with the new service information
        self.write_back_to_file()


    def find_index(self, chooser): # B & C
    # Retrieve the list of dictionaries containing service information
        list_of_dicts = self.create_dictionary()

        # Flag to indicate if the target service is found
        found = False

        # Prompt the user for the service name to search for
        target = self.get_valid_input()

        # Iterate through the list of dictionaries
        for index, dictionary in enumerate(list_of_dicts):
            # Check if the target service name exists in the current dictionary
            for key, value in dictionary.items():
                if value == target:
                    found = True

                    # If deleting (chooser == 1), inform user, remove the dictionary, and update the file
                    if chooser == 1:
                        print(f"Service found.\n{list_of_dicts[index]} has been deleted")
                        del list_of_dicts[index]
                        self.write_back_to_file()
                        break

                    # If updating (chooser == 2), call the update_dictionary method
                    if chooser == 2:
                        self.update_dictionary(index)

        # If the target service is not found, inform the user
        if not found:
            print("Service not found")

    
    def list_func(self): # D
        # Check if the file has existing data
        if not self.new_file:
            i = 0
            # Iterate through dictionaries in the list and print key-value pairs
            for data_dict in self.data_dict_list:
                for key, value in data_dict.items():
                    i += 1
                    print(f"{key}: {value}")
                    # Print an extra newline after every 3 key-value pairs
                    if i % 3 == 0:
                        print(f"\n")
            # Restart the main menu loop
            self.start_up()
        else:
            # Inform the user that the file is new and contains no data
            print("***New file created with no data. Cannot list data***\n")
            # Restart the main menu loop
            self.start_up()


    def terminate(self): # Q
        # Terminate the program by setting the global running flag to False
        global running
        running = False

        # Clear the console screen
        cls()

        # Update the file with the current service information
        self.write_back_to_file()

        # Restart the main menu loop
        self.start_up()


    def input_fields(self): 
        # Continuously prompt the user for service, user_id, and password until valid inputs are provided
        while True: 
            service = input("Enter the name of the service.\n> ")
            if service: 
                user_id = input(f"Enter the user_id for {service}.\n> ")
                if user_id: 
                    password = input(f"Enter the password for {service}: {user_id}.\n> ")
                    if password: 
                        # Break the loop if all input fields are filled
                        break 
        # Create a dictionary with the collected service, user_id, and password
        temp_dict = {'service': service, 'user_id': user_id, 'password': password}
        return temp_dict



    def update_dictionary(self, index):
        # Prompt the user to input new fields for updating the selected service
        temp_dict = self.input_fields()

        # Update the existing dictionary at the specified index with the new information
        self.data_dict_list[index] = temp_dict

        # Update the file with the modified service information
        self.write_back_to_file()

    def get_valid_input(self):
        # Continuously prompt the user for the service they wish to change until a valid input is provided
        while True:
            target_value = input("Please enter the service you wish to change.\n> ")
            if target_value:
                return target_value
            else:
                print("Invalid input. Please try again")

    def invalid_menu_input(self):
        # Inform the user about an invalid menu selection and restart the main menu loop
        print("Please enter a valid selection")
        self.start_up()


    def write_back_to_file(self):
        # Convert the list of dictionaries to a DataFrame and write it to an Excel file
        df = pd.DataFrame(self.data_dict_list)
        df.to_excel(self.file_name, index=False, engine='openpyxl')

    def menu_operation(self):
        # Prompt the user to select an operation and convert the input to lowercase
        operation = input("Select which operation you want to execute.\nA) Add\nB) Delete\nC) Update\nD) List\nQ) Quit\n> ").lower()
        print("\n")
        return operation

    def start_up(self):
        # Continuously loop through the main menu options as long as the 'running' flag is True
        while running:
            operation = self.menu_operation()

            # Execute the selected operation based on the options dictionary
            self.options.get(operation, self.invalid_menu_input)()

    def create_dictionary(self):
    # Read data from an existing Excel file and convert it to a list of dictionaries
        data = pd.read_excel(self.file_name, engine='openpyxl')
        df = pd.DataFrame(data, columns=["service", "user_id", "password"])
        self.data_dict_list = df.to_dict(orient='records')
        return self.data_dict_list

    def create(self):
        # Prompt the user for a file name and check if it exists
        self.file_name = input("Enter file name: ")
        try:
            with open(self.file_name, 'r') as file:
                print("File exists")
                self.new_file = False
                self.create_dictionary()
                self.start_up()
        except FileNotFoundError:
            # If the file does not exist, create a new one
            with open(self.file_name, 'w') as file:
                print("File does not exist. Creating a new one")
                self.new_file = True
                self.new_file_created()

    def new_file_created(self):
        # Initialize the list with a default empty dictionary, write it to the file, and restart the main menu loop
        self.data_dict_list = [{'service': '', 'user_id': '', 'password': ''}]
        self.write_back_to_file()
        self.start_up()

def main():
    # Instantiate PassMan class and create a new file
    pass_instance = PassMan()
    pass_instance.create()

if __name__ == '__main__':
    # Call the main function if the script is executed directly
    main()
