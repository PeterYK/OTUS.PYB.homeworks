# exceptions.py  (лучше создать отдельный файл)

class PhoneBookError(Exception):
    """Базовое исключение для всего приложения"""
    pass


class ContactNotFoundError(PhoneBookError):
    """Контакт не найден"""
    def __init__(self, name: str):
        self.name = name
        super().__init__(f"Контакт '{name}' не найден")


class ContactsFileNotFoundError(PhoneBookError):
    """Ошибка чтения файла"""
    def __init__(self, file_name: str):
        self.file_name = file_name
        super().__init__(f"Файл '{file_name}' не найден")


class DataNotSavedError(PhoneBookError):
    """Не удалось сохранить данные в файл"""
    def __init__(self, file_name: str):
        self.file_name = file_name
        super().__init__(f"Не удалось сохранить данные или создать файл '{file_name}'")