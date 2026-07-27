from utils import enter_int_value, enter_string_value
from models.contact import Contact

class ConsoleView:
    """
    Class for displaying data in the console.
    """

    def show_main_menu(self):
        """
        Show the main menu.
        
        Args: 
            None
        
        Returns:
            None    
        """
        print('''
****************************************
*             Главное меню:            *
            ''')
        print('''
1. все контакты
2. создать контакт
3. найти контакт
4. выбрать контакт
5. удалить все контакты
            ''')

    def user_select_main_menu(self) -> int:
        is_valide_command = False
        while not is_valide_command:
            number = enter_int_value("\nВыберите опцию меню (введите число): ")
            if number in [1, 2, 3, 4, 5]:
                is_valide_command = True
            else:
                print(f"'{number}' - нет такого пункта меню. Выдерите корректный пункт меню (введите число).")

        return number
    
    def show_contacts(self, contacts: list[Contact]):
        """
        Show all contacts in the contacts list.
        
        Args: 
            None
        
        Returns:
            None    
        """

        print('''
*             Контакты:            *
            ''')
        index = 0
        for contact in contacts:
            if index == 0:
                print(f"{contact.name}\t\t{contact.phone}\t\t{contact.comment}\n")
            else:
                print(f"{index}. {contact.name}\t\t{contact.phone}\t\t{contact.comment}")
            index += 1

    def show_found_contacts(self):
        """
        Show found contacts in the contacts list.
        
        Args: 
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

    def show_found_contacts_menu(self, contacts: list):
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
        self.show_contacts(contacts)
        print('''
1. выбрать контакт
2. главное меню
            ''')

    def user_select_found_contacts_menu(self) -> int:
        """
        Selecting found contacts menu.
        
        Args: 
            None
        
        Returns:
            int (selected menu option)    
        """
        is_incorrect_number = True
        while is_incorrect_number:
            number = enter_int_value("\nВыберите опцию меню (введите число): ")
            if number in [1, 2]:
                is_incorrect_number = False
        return number
    
    def show_contact_menu(self, contact: Contact):
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
        print(f'{contact.name}\t\t{contact.phone}\t\t{contact.comment}')
        print('''
 1. изменить контакт
 2. удалить контакт
 3. главное меню
          ''')

    def user_select_contact_menu(self) -> int:
        """
        Selecting contact menu.
        
        Args: 
            None
        
        Returns:
            int (selected menu option)    
        """
        is_incorrect_number = True
        while is_incorrect_number:
            number = enter_int_value("\nВыберите опцию меню (введите число): ")
            if number in [1, 2, 3]:
                is_incorrect_number = False
        return number
            
    def enter_part_of_contact(self) -> str:
        """
        Find contacts in the contacts list by part of the name or phone number.
        
        Args: 
            None
        
        Returns:
            str (part of the name or phone number)    
        """
        part = enter_string_value("Введите часть имени или номера телефона для поиска: ")
        return part

    def select_contact(self, contacts: list) -> int:
        """
        Select contact from the found contacts list.
        
        Args: 
            contacts(list): found contacts data as a list of list.
        
        Returns:
            list (Contact) / None
        """

        if len(contacts) == 1: # Ignoring a header row.
            print('\n*** Нет найденных контактов ***\n')
            return 0

        is_incorrect_index = True
        while is_incorrect_index:
            selected_contact_index =  enter_int_value("Введите порядковый номер контакта: ")
            if selected_contact_index >= len(contacts) or selected_contact_index <= 0:
                print(f'Вы ввели {selected_contact_index}, в найденных контактах всего {len(contacts) - 1}. Попробуйте снова:')
            else:
                is_incorrect_index = False

        return selected_contact_index

    def show_removed_contact(self, contact: Contact, contacts: list[Contact]):
        """
        Show removed contact.
        
        Args: 
            contact(list): contact data as a list of strings.
        
        Returns:
            None    
        """
        if contact in contacts:
            print(f'\n*** Не удалось удалить контакт {contact.name}|{contact.phone}|{contact.comment} ***\n')
        else:
            print(f'\n*** Контакт {contact.name}|{contact.phone}|{contact.comment} удален ***\n')

    def enter_contact_data(self) -> list:
        """
        User entering a new contact data as a list of strings.
        
        Args: 
            None
        
        Returns:
            list[str]    
        """
        name = enter_string_value("Введите данные: \nимя - ")
        phone_number = enter_string_value("Номер телефона - ")
        comment = enter_string_value("Комментарий - ")
        return [name, phone_number, comment]