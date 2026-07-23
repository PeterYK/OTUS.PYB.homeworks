import csv

FILE_NAME = "phone_book.csv"

def fetch_contacts_from_file() -> list:
    """
    Gettibg all contacts data from the file.
    
    Args: 
        None
    
    Returns:
        list (list of contacts)    
    """    
    with open(FILE_NAME, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        contacts = list(reader)
    return contacts

def clear_file():
    """
    Rewriting data_file with empty data.
    
    Args: 
        None
    
    Returns:
        None    
    """
    with open(FILE_NAME, "w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["name", "phone", "comment"])

def add_contact(contact: list):
    """
    Save new contact data to the file.
    
    Args: 
        contacts(list): contact data as a list of strings.
    
    Returns:
        None    
    """
    with open(FILE_NAME, "a", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(contact)


def update_contacts(contacts: list):
    """
    Rewrite  contacts data data to the file.
    
    Args: 
        contact(list): contact data as a list of strings.
    
    Returns:
        None    
    """
    with open(FILE_NAME, "w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(contacts)