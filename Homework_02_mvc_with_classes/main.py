from controller.controller import ViewController
from models.phonebook import PhoneBook
from views.view import ConsoleView

book = PhoneBook()
view = ConsoleView()
vc = ViewController(book, view)
vc.run()