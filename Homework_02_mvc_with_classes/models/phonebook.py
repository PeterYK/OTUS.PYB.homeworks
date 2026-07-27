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

    def remove(self, contact: Contact):
        if contact in self.contacts:
            self.contacts.remove(contact)

        contacts_list = [] 
        for contact in self.contacts:
            contacts_list.append([contact.name, contact.phone, contact.comment])
        self.fwriter.write_file(contacts_list)

    def add_contact(self, contact: Contact):
        self.contacts.append(contact)
        contacts_list = [] 
        for contact in self.contacts:
            contacts_list.append([contact.name, contact.phone, contact.comment])
        self.fwriter.write_file(contacts_list)


    def edit_contact(self, updatedContact: Contact):
        if updatedContact in self.contacts:
            contacts_list = [] 
            for contact in self.contacts:
                contacts_list.append([contact.name, contact.phone, contact.comment])
            self.fwriter.write_file(contacts_list)
            print(f"Удалось обвновить контакт {updatedContact}")
        else:
            print(f"Не удалось обвновить контакт {updatedContact}")

    def remove_all_contacts(self): 
        contact = Contact("name", "phone", "comment")
        self.contacts = []
        self.contacts.append(contact)
        clear_contacts = [["name", "phone", "comment"]]
        self.fwriter.write_file(clear_contacts)