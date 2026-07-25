from hw_utils import enter_string_value, enter_int_value
from hw_model import fetch_contacts_from_file, clear_file, add_contact, update_contacts

def get_all_contacts() -> list:
    """
    Get all contacts from the file.
    
    Args: 
        None
    
    Returns:
        list: list of all contacts as a list of lists. Each contact is a list of strings.     
    """
    contacts = fetch_contacts_from_file()
    return contacts


def select_contact() -> list:
    """
    Select contact from the all contacts list.
    
    Args: 
        None. All contacts are read from the file.
    
    Returns:
        None    
    """

    all_contacts = get_all_contacts()
    if len(all_contacts) < 2:
        print('Нет контактов')
        return []

    is_correct_index = False
    while not is_correct_index:
        selected_contact_index =  enter_int_value("Введите порядковый номер контакта: ")
        if selected_contact_index >= len(all_contacts) or selected_contact_index <= 0:
            print(f'Вы ввели {selected_contact_index}, в контактах всего {len(all_contacts) - 1}. Попробуйте снова:')
        else:
            is_correct_index = True
    return all_contacts[selected_contact_index]

def select_found_contact(contacts: list) -> list:
    """
    Select contact from the found contacts list.
    
    Args: 
        contacts(list): found contacts data as a list of list.
    
    Returns:
        list (Contact)    
    """

    if len(contacts) == 1: # Ignoring a header row.
        print('\n*** Нет найденных контактов ***\n')
        return []

    is_incorrect_index = True
    while is_incorrect_index:
        selected_contact_index =  enter_int_value("Введите порядковый номер контакта: ")
        if selected_contact_index >= len(contacts) or selected_contact_index <= 0:
            print(f'Вы ввели {selected_contact_index}, в найденных контактах всего {len(contacts) - 1}. Попробуйте снова:')
        else:
            is_incorrect_index = False

    return contacts[selected_contact_index]

def find_contacts() -> list:
    """
    Find contacts in the contacts list by part of the name or phone number.
    
    Args: 
        None
    
    Returns:
        list    
    """

    found_contacts = []
    found_contacts.append(["name", "phone", "comment"])
    part = enter_string_value("Введите часть имени или номера телефона для поиска: ")
    contacts = get_all_contacts()
    for item in contacts[1:]:
        if part.lower() in item[0].lower() or part.lower() in item[1].lower():
            found_contacts.append(item)

    if len(found_contacts) < 2: 
        return []
    return found_contacts

def resume_find(part: str) -> bool:
    """
    Support function for resuming contact search.
    
    Args: 
        part(str): part of the name or phone number to search for.
    
    Returns:
        None    
    """

    resume_to_find = enter_string_value(f'Контакт с именем или номером содержащий "{part}" НЕ НАЙДЕН. Продолжить поиск?\ny/n?: ')
    if resume_to_find != 'y' and resume_to_find != 'n':
        print(f'Вы ввели "{resume_to_find}". Нужно ввести "y" или "n".')
        resume_find(part)
        return
    elif resume_to_find == 'n':
        return False
    return True

def create_contact():
    """
    Creating a new contact data as a list of strings.
    
    Args: 
        None
    
    Returns:
        None    
    """
    name = enter_string_value("Введите данные: \nимя - ")
    phone_number = enter_string_value("Номер телефона - ")
    comment = enter_string_value("Комментарий - ")
    contact = [name, phone_number, comment]
    print(f"\nContact: {contact[0]}\t{contact[1]}\t{contact[2]} - added\n")
    add_contact(contact)
    
def delete_all_contacts():
    """
    Remove all contacts from the file.
    
    Args: 
        None
    
    Returns:
        None    
    """
    clear_file()

def edit_contact(contact: list):
    """
    Edit a selected contact form from found or main cintact list.
    
    Args: 
        contact(list): found contacts data as a list of strings.
    
    Returns:
        None    
    """

    all_contacts = get_all_contacts()
    found_contact = []
    for item in all_contacts:
        if contact[2] == item[2]:
            found_contact = item
            break
    else:
        print(f"Этот контакт не найден в телефонной книге")
        # show_menu()
        return
    name = enter_string_value("Введите данные: \nимя - ")
    phone_number = enter_string_value("Номер телефона - ")
    comment = enter_string_value("Комментарий - ")
    contact = [name, phone_number, comment]
    found_contact[0] = name
    found_contact[1] = phone_number
    found_contact[2] = comment
    update_contacts(all_contacts)
    print(f'\nКонтакт обновлен:\n{found_contact[0]}\t\t{found_contact[1]}\t\t{found_contact[2]}\n')

def remove_contact(contact: list):
    """
    remove a selected contact form  contact list and save changes to the file.
    
    Args: 
        contact(list): selected contact data as a list of strings.
    
    Returns:
        None    
    """

    is_incorrect_value = True
    while is_incorrect_value:
        accept_to_delete = enter_string_value('Вы действительно хотите удалить контакт? \nВведите "y"/"n": ')
        if accept_to_delete == 'y' or accept_to_delete == 'n':
            is_incorrect_value = False
        else:
            print("Нужно ввести 'y' или 'n'. Попробуйте еще раз")

    if accept_to_delete == 'n':
        return

    all_contacts = get_all_contacts()
    found_contact = []
    for item in all_contacts:
        if contact[2] == item[2]:
            found_contact = item
            break
    else:
        print(f"Этот контакт не найден в телефонной книге")
        return
    
    all_contacts.remove(found_contact)
    update_contacts(all_contacts)
    print(f'Контакт УДАЛЕН:\n{found_contact[0]}\t\t{found_contact[1]}\t\t{found_contact[2]}\n')
