import csv
import os


FILE_NAME = "phone_book.csv"


def run_phone_book():
    """
    Run the phone book application.
    
    Args: 
        None
    
    Returns:
        Nome    
    """
    print("\n***** Phonebook *****\n")
    if prepare_to_work(FILE_NAME):
        show_menu()
    else:
        print('''Fatal error. The phone book file could not be created or opened.''')


def prepare_to_work(filename: str):   
    """
    Prepare the phone book for work.
    
    Args: 
        Relative path to the phone book file (filename) as a string.
    
    Returns:
        None    
    """ 
    if os.path.exists(filename):
        print(f"Файл {filename} уже существует.")
        return True
    
    headers = ["name", "phone", "comment"]

    os.makedirs(os.path.dirname(filename) or ".", exist_ok=True)
    
    with open(filename, "w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(headers)
    
    print(f"Файл {filename} создан.")
    return True


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
 5. удалить все контакты
          ''')
    number = enter_int_value("\nВыберите опцию меню (введите число): ")
    if number == 1:
        show_contacts()
    elif number == 2:
        create_contact()
    elif number == 3:
        find_contacts()
    elif number == 4:
        select_contact()        
    elif number == 5:
        delete_all_contacts()
    else:
        print(f"'{number}' - нет такого пункта меню. Выдерите корректный пункт меню (введите число).")
        show_menu()

   
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
    number = enter_int_value("\nВыберите опцию меню (введите число): ")
    if number == 1:
        select_found_contact(contacts)
    elif number == 2:
        show_menu()
    else:
        print(f"'{number}' - нет такого пункта меню. Выберите корректный пункт меню (введите число).")
        show_found_contacts_menu(contacts)


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
    elif number == 2:
        remove_contact(contact)
    elif number == 3:
        show_menu()
    else:
        print(f"'{number}' - нет такого пункта меню. Выберите корректный пункт меню (введите число).")
        show_contact_menu(contact)


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
    show_found_contacts_menu(contacts)


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
    add_contact(contact)
    show_menu()


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
    show_contacts()


def delete_all_contacts():
    """
    Remove all contacts from the file.
    
    Args: 
        None
    
    Returns:
        None    
    """

    with open(FILE_NAME, "w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["name", "phone", "comment"])
    show_menu()


def find_contacts():
    """
    Find contacts in the contacts list by part of the name or phone number.
    
    Args: 
        None
    
    Returns:
        None    
    """

    found_contacts = []
    found_contacts.append(["name", "phone", "comment"])
    part = enter_string_value("Введите часть имени или номера телефона для поиска: ")
    contacts = get_all_contacts()
    for item in contacts[1:]:
        if part.lower() in item[0].lower() or part.lower() in item[1].lower():
            found_contacts.append(item)
    if len(found_contacts) < 2: 
        if resume_find(part):
            find_contacts()
        else:
            show_menu()
            return
    show_found_contacts(found_contacts)


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


def select_found_contact(contacts: list):
    """
    Select contact from the found contacts list.
    
    Args: 
        contacts(list): found contacts data as a list of list.
    
    Returns:
        None    
    """

    if len(contacts) == 1: # Ignoring a header row.
        print('\n*** Нет найденных контактов ***\n')
        show_found_contacts_menu(contacts)
        return
    
    selected_contact_index =  enter_int_value("Введите порядковый номер контакта: ")
    if selected_contact_index >= len(contacts) or selected_contact_index <= 0:
        print(f'Вы ввели {selected_contact_index}, в найденных контактах всего {len(contacts) - 1}. Попробуйте снова:')
        select_found_contact(contacts)
    else:
        show_contact_menu(contacts[selected_contact_index])


def select_contact():
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
        show_found_contacts_menu()
        return
    selected_contact_index =  enter_int_value("Введите порядковый номер контакта: ")
    if selected_contact_index >= len(all_contacts) or selected_contact_index <= 0:
        print(f'Вы ввели {selected_contact_index}, в контактах всего {len(all_contacts) - 1}. Попробуйте снова:')
        select_contact()
    else:
        show_contact_menu(all_contacts[selected_contact_index])


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
        show_menu()
        return
    name = enter_string_value("Введите данные: \nимя - ")
    phone_number = enter_string_value("Номер телефона - ")
    comment = enter_string_value("Комментарий - ")
    contact = [name, phone_number, comment]
    found_contact[0] = name
    found_contact[1] = phone_number
    found_contact[2] = comment
    with open(FILE_NAME, "w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(all_contacts)
        print(f'\nКонтакт обновлен:\n{found_contact[0]}\t\t{found_contact[1]}\t\t{found_contact[2]}\n')
    show_contacts()
    show_menu()


def get_all_contacts() -> list:
    """
    Get all contacts from the file.
    
    Args: 
        None
    
    Returns:
        list: list of all contacts as a list of lists. Each contact is a list of strings.     
    """

    with open(FILE_NAME, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        contacts = list(reader)
    return contacts


def remove_contact(contact: list):
    """
    remove a selected contact form  contact list and save changes to the file.
    
    Args: 
        contact(list): selected contact data as a list of strings.
    
    Returns:
        None    
    """

    accept_to_delete = enter_string_value('Вы действительно хотите удалить контакт? \nВведите "y"/"n": ')

    if accept_to_delete != 'y' and accept_to_delete != 'n':
        remove_contact(contact)
        return
    elif accept_to_delete == 'n':
        show_contact_menu(contact)
        return
    
    all_contacts = get_all_contacts()
    found_contact = []
    for item in all_contacts:
        if contact[2] == item[2]:
            found_contact = item
            break
    else:
        print(f"Этот контакт не найден в телефонной книге")
        show_menu()
        return
    all_contacts.remove(found_contact)
    with open(FILE_NAME, "w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(all_contacts)

    print(f'Контакт УДАЛЕН:\n{found_contact[0]}\t\t{found_contact[1]}\t\t{found_contact[2]}\n')
    show_contacts()
    show_menu()


def enter_int_value(description: str) -> int:
    """
    Support function for entering an integer value.
    
    Args: 
        description(str): description of the value to be entered.
    
    Returns:
        int: the entered integer value.
    """

    while True:
        try:
            value = int(input(description))
            return value
        except ValueError:
            print("Неверный формат. Введите число")


def enter_string_value(description: str) -> str:
    """
    Support function for entering an string value.
    
    Args: 
        description(str): description of the value to be entered.
    
    Returns:
        str: the entered string value.
    """

    while True:
        value = input(description)
        if value.strip() == "":
            print("Поле не может быть пустым. Попробуйте снова.")
        else:
            return value
        

run_phone_book()

