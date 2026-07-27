from models.phonebook import PhoneBook
from views.view import ConsoleView

class ViewController:
    """
    Class for controlling the view and model.
    """
    def __init__(self, phonebook: PhoneBook, view: ConsoleView):
        self.phonebook = phonebook
        self.view = view

    def run(self):
        self.show_main_menu()

    def show_main_menu(self):
        self.view.show_main_menu()
        index = self.view.user_select_main_menu()
        self.select_main_menu(index)

    def select_main_menu(self, index: int):
        if index == 1:
            contacts = self.phonebook.contacts
            self.view.show_contacts(contacts)
            self.show_main_menu()
        elif index == 2:
            # create_contact()
            # show_menu()
            pass
        elif index == 3:
            self.find_contact()
        elif index == 4:
            # contact = select_contact()  
            # show_contact_menu(contact)      
            pass
        elif index == 5:
            # delete_all_contacts()
            self.show_main_menu()
            pass

    def find_contact(self):
        """
        Find a contact by name.
        
        Args: 
            name (str): The name of the contact to find.
        
        Returns:
            list: A list of contacts that match the search criteria.    
        """
        part = self.view.enter_part_of_contact()
        found_contacts = self.phonebook.find_contact(part)
        self.run_found_contacts_menu(found_contacts)

    def run_found_contacts_menu(self, contacts: list):
        """
        Show the found contacts menu.
        
        Args: 
            contacts(list): before found contacts as a list of lists.
        
        Returns:
            None    
        """

        self.view.show_found_contacts_menu(contacts)
        index = self.view.user_select_found_contacts_menu()

        if index == 1:
            if len(contacts) == 1:  # No contacts found (first contact is a header row).
                self.show_main_menu()
            else:
                contact_index = self.view.select_found_contact(contacts)
                if contact_index == 0:
                    self.show_main_menu()
                else:
                    self.view.show_contact_menu(contacts[contact_index])
        elif index == 2:
            self.show_main_menu()