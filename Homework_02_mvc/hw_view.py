# from hw_model import *
from hw_utils import enter_int_value, enter_string_value
from hw_controller import get_all_contacts, select_contact, delete_all_contacts, find_contacts, resume_find, create_contact, select_found_contact, remove_contact, edit_contact

def show_menu():
    """
    Show the main menu.
    
    Args: 
        None
    
    Returns:
        None    
    """
    print('''
*************************************
*             Главное меню:            *
          ''')
    print('''
 1. все контакты
 2. создать контакт
 3. найти контакт
 4. выбрать контакт
 5. удалить все контакты(non)
          ''')
    is_valide_command = False
    while not is_valide_command:
        number = enter_int_value("\nВыберите опцию меню (введите число): ")
        if number in [1, 2, 3, 4, 5]:
            is_valide_command = True
        else:
            print(f"'{number}' - нет такого пункта меню. Выдерите корректный пункт меню (введите число).")

    if number == 1:
        show_contacts()
        pass
    elif number == 2:
        create_contact()
        show_menu()
    elif number == 3:
        try_to_find_contact()
    elif number == 4:
        contact = select_contact()  
        show_contact_menu(contact)      
    elif number == 5:
        delete_all_contacts()
        show_menu()

def show_contacts():
    """
    Show all contacts in the contacts list.
    
    Args: 
        None
    
    Returns:
        None    
    """

    contacts = get_all_contacts()
    print(f"\nContacts:\n")
    index = 0
    for item in contacts:
        if index == 0:
            print(f"{item[0]}\t\t{item[1]}\t\t{item[2]}\n")
        else:
            print(f"{index}. {item[0]}\t\t{item[1]}\t\t{item[2]}")
        index += 1
    show_menu()


def show_contact_menu(contact: list):
    """
    Show the contact menu.
    
    Args: 
        contact(list): contact data as a list of strings.
    
    Returns:
        None    
    """

    print('''
*************************************
*           Контакт:           *
          ''')
    print(f'{contact[0]}\t\t{contact[1]}\t\t{contact[2]}')
    print('''
 1. изменить контакт
 2. удалить контакт
 3. главное меню
          ''')
    number = enter_int_value("\nВыберите опцию меню (введите число): ")
    if number == 1:
        edit_contact(contact)
        show_menu()
    elif number == 2:
        remove_contact(contact)
        show_menu()
    elif number == 3:
        show_menu()
    else:
        print(f"'{number}' - нет такого пункта меню. Выберите корректный пункт меню (введите число).")
        show_contact_menu(contact)

def show_found_contacts(contacts: list):
    """
    Show found contacts in the contacts list.
    
    Args: 
        contacts(list): found contacts data as a list of list.
    
    Returns:
        None    
    """

    print(f"\nFound contacts:\n")
    index = 0
    for item in contacts:
        if index == 0:
            print(f"{item[0]}\t\t{item[1]}\t\t{item[2]}\n")
        else:
            print(f"{index}. {item[0]}\t\t{item[1]}\t\t{item[2]}")
        index += 1

def show_found_contacts_menu(contacts: list):
    """
    Show the found contacts menu.
    
    Args: 
        contacts(list): before found contacts as a list of lists.
    
    Returns:
        None    
    """
    print('''
*************************************
*       Найденные контакты:        *
          ''')
    print('''
 1. выбрать контакт
 2. главное меню
          ''')
    is_incorrect_number = True
    while is_incorrect_number:
        number = enter_int_value("\nВыберите опцию меню (введите число): ")
        if number in [1, 2]:
            is_incorrect_number = False

    if number == 1:
        contact = select_found_contact(contacts)
        if len(contact) == 0:
            show_menu()
        else:
            show_contact_menu(contact)
    elif number == 2:
        show_menu()

def try_to_find_contact():
    contacts = find_contacts()
    if len(contacts) == 0:
        if resume_find():
            try_to_find_contact()
            return
        else:
            show_menu()
            return
    show_found_contacts(contacts)    
    show_found_contacts_menu(contacts)
    


def resume_find() -> bool:
    """
    Support function for resuming contact search.
    
    Args: 
        part(str): part of the name or phone number to search for.
    
    Returns:
        None    
    """

    is_not_correct_enter = True
    while is_not_correct_enter:
        resume_to_find = enter_string_value(f'Контакт НЕ НАЙДЕН. Продолжить поиск?\ny/n?: ')
        if resume_to_find != 'y' and resume_to_find != 'n':
            print(f'Вы ввели "{resume_to_find}". Нужно ввести "y" или "n".')
        else:
            is_not_correct_enter = False

    if resume_to_find == 'y':
        return True
    else:
        return False



