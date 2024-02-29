import pandas as pd
import os

running = True

cls = lambda: os.system('cls')

class PassMan:
    def __init__(self):
        self.options = {
        'a': self.add,
        'b': lambda: self.find_index(1),
        'c': lambda: self.find_index(2),
        'd': self.list_func,
        'q': self.terminate
        }
        
    def add(self): # A
        temp_dict = self.input_fields()
        self.data_dict_list.append(temp_dict)
        self.write_back_to_file(self.data_dict_list)

    def find_index(self, chooser): # B & C
        list_of_dicts = self.create_dictionary()
        found = False
        target = self.get_valid_input()
        for index, dictionary in enumerate(list_of_dicts):
            for key, value, in dictionary.items():
                if value == target:
                    found = True
                    if chooser == 1:
                        print(f"Service found.\n{list_of_dicts[index]} has been deleted")
                        del list_of_dicts[index]
                        self.write_back_to_file(self.data_dict_list)
                        break
                    if chooser == 2:
                        self.update_dictionary(index)
        if not found:
            print("Service not found")
    
    def list_func(self): # D
        i = 0
        for data_dict in self.data_dict_list:
            for key, value in data_dict.items():
                i += 1
                print(f"{key}: {value}")
                if i % 3 == 0:
                    print(f"\n")
        self.start_up()

    def terminate(self): # Q
        global running
        running = False
        cls()
        self.write_back_to_file(self.data_dict_list)
        self.start_up()    

    def input_fields(self): # Prompt for input fields for both adding and updating options. 
            while True: # Loop until break statement
                service = input("Enter the name of the service.\n> ")
                if service: # Ensure service is filled
                    user_id = input(f"Enter the user_id for {service}.\n> ")
                    if user_id: # Ensure user_id is filled
                        password = input(f"Enter the password for {service}: {user_id}.\n> ")
                        if password: # Ensure password is filled
                            break # If all variable correct, break
            temp_dict = {'service': service, 'user_id': user_id, 'password': password}
            # Create a temp dictionary with added/updated items
            return temp_dict
            # Return the new temp dictionary

    def update_dictionary(self, index):
        temp_dict = self.input_fields()
        self.data_dict_list[index] = temp_dict
        self.write_back_to_file(self.data_dict_list)
    
    def get_valid_input(self):
        while True:
            target_value = input("Please enter the service you wish to change.\n> ")
            if target_value:
                return target_value
            else:
                print("Invalid input. Please try again")

    def invalid_menu_input(self):
        print("Please enter a valid selection")
        self.start_up()

    def write_back_to_file(self, dict_list):
        df = pd.DataFrame(dict_list)
        df.to_excel(self.file_name, index=False, engine='openpyxl')

    def menu_operation(self):
        operation = input("Select which operation you want to execute.\nA) Add\nB) Delete\nC) Update\nD) List\nQ) Quit\n> ").lower()
        print("\n")
        return operation

    def start_up(self):
        while running:
            operation = self.menu_operation()
            self.options.get(operation, self.invalid_menu_input)()

    def create_dictionary(self):
        data = pd.read_excel(self.file_name, engine='openpyxl')
        df = pd.DataFrame(data, columns=["service", "user_id", "password"])
        self.data_dict_list = df.to_dict(orient='records')
        return self.data_dict_list

    def create(self):
            self.file_name = input("Enter file name: ")
            try:
                with open(self.file_name, 'r') as file:
                    print("file exists")
                    self.create_dictionary()
                    self.start_up()
            except FileNotFoundError:
                with open(self.file_name, 'w') as file:
                    print("file does not exist. Creating new one")
                    #self.new_file_created()
    
    """def new_file_created(self):
        temp_dict = [{'service': '', 'user_id': '', 'password': ''}]
        self.write_back_to_file(temp_dict)
        self.start_up()"""


def main():
    pass_instance = PassMan()
    pass_instance.create()

if __name__ == '__main__':
    main()