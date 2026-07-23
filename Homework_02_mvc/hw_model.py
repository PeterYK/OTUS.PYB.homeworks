import csv

FILE_NAME = "phone_book.csv"

def fetch_contacts_from_file() -> list:    
    with open(FILE_NAME, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        contacts = list(reader)
    return contacts

def clear_file():
    with open(FILE_NAME, "w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["name", "phone", "comment"])

def add_contact(contact: list):
    """
    Add a new contact to the contacts list and save it to the file.
    
    Args: 
        contact(list): contact data as a list of strings.
    
    Returns:
        None    
    """
    with open(FILE_NAME, "a", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(contact)


def update_contacts(contacts: list):
    with open(FILE_NAME, "w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(contacts)