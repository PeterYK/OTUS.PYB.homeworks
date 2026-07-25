
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