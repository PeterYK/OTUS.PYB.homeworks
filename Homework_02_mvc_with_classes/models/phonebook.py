from models.filereader import FileReader
from models.filewriter import FileWriter
from models.contact import Contact

class PhoneBook:
    """
    Class for working with the phone book.
    """
    freader = FileReader("data/phonebook.csv")
    fwriter = FileWriter("data/phonebook.csv")

    def __init__(self):
        raw_list = self.freader.read_file()
        contacts = []
        for item in raw_list:
            contact = Contact(item[0], item[1], item[2])
            contacts.append(contact)
        self.contacts = contacts

    def find_contact(self, part: str) -> list[Contact]:
        """
        Find contacts in the contacts list by part of the name or phone number.
        
        Args: 
            part (str): The part of the name or phone number to search for.
        
        Returns:
            list    
        """

        found_contacts = []
        found_contacts.append(Contact("name", "phone", "comment"))  # Header row
        for contact in self.contacts[1:]:
            if part.lower() in contact.name.lower() or part.lower() in contact.phone.lower():
                found_contacts.append(contact)

        if len(found_contacts) == 1: # Ignoring a header row.
            return []
        return found_contacts

    def select_contact(self, index: int) -> Contact:
        """
        Select a contact from the contacts list by index.
        
        Args: 
            index (int): The index of the contact to select.
        """
        
    # def add_contact(self, contact: PhoneContact):
    #     """
    #     Add a new contact to the phone book.
        
    #     Args: 
    #         contact (PhoneContact): The contact to add.
        
    #     Returns:
    #         None    
    #     """        
    #     self.contacts.append(contact.to_list())
    #     add_contact(contact.to_list())

    # def update_contact(self, index: int, contact: PhoneContact):
    #     """
    #     Update an existing contact in the phone book.
        
    #     Args: 
    #         index (int): The index of the contact to update.
    #         contact (PhoneContact): The updated contact data.
    #     """
    #     self.contacts[index] = contact.to_list()
    #     update_contacts(self.contacts)