from models.phonebook import PhoneBook
from models.contact import Contact
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
        """
        Function for show main menu.
        
        Args: 
            None
        
        Returns:
            None    
        """
        self.view.show_main_menu()
        index = self.view.user_select_main_menu()
        self.select_main_menu(index)

    def select_main_menu(self, index: int):
        """
        Find a contact by name.
        
        Args: 
            index (int): Index of menu.
        
        Returns:
            None    
        """

        if index == 1:
            contacts = self.phonebook.contacts
            self.view.show_contacts(contacts)
            self.show_main_menu()
        elif index == 2:
            self.create_contact()
            self.show_main_menu()
            pass
        elif index == 3:
            self.find_contact()
        elif index == 4:
            self.select_contact()            
        elif index == 5:
            self.phonebook.remove_all_contacts()
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
                contact_index = self.view.select_contact(contacts)
                if contact_index == 0:
                    self.show_main_menu()
                else:
                    contact = contacts[contact_index]
                    self.view.show_contact_menu(contact)
                    self.select_contact_menu(contact)
        elif index == 2:
            self.show_main_menu()

    def select_contact_menu(self, contact: Contact):
        index = self.view.user_select_contact_menu()
        if index == 1:
            self.edit_contact(contact)
            self.show_main_menu()
        elif index == 2:
            self.remove_contact(contact)
            self.show_main_menu()
        elif index == 3:
            self.show_main_menu()

    def remove_contact(self, contact: Contact):
        self.phonebook.remove(contact)
        self.view.show_removed_contact(contact, self.phonebook.contacts)

    def create_contact(self):
        contact_data = self.view.enter_contact_data()
        new_contact = Contact(contact_data[0], contact_data[1], contact_data[2])
        self.phonebook.add_contact(new_contact)

    def edit_contact(self, contact: Contact):
        contact_data = self.view.enter_contact_data()
        contact.name = contact_data[0]
        contact.phone = contact_data[1]
        contact.comment = contact_data[2]
        self.phonebook.edit_contact(contact)

    def select_contact(self):
        contacts = self.phonebook.contacts
        contact_index = self.view.select_contact(contacts)
        contact = contacts[contact_index]
        self.view.show_contact_menu(contact)
        self.select_contact_menu(contact)  