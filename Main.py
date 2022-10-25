from os.path import exists
from CSV_creating import creating
from File_writing import writing_scv
from File_writing import writing_txt
from User_interface import get_info as info
import import_data as im
from tabulate import tabulate

command = int(input('Введите команду:\n1.Найти контакт:\n2.Показать весь список:\n3.Добавить контакт:\n'))
if command == 1:
    to_find = input('Введите имя, фамилию, номер, либо коментарий: ')
    my_list = im.search_data(im.read_csv(),to_find)
    head = im.read_csv()[0]

    print(tabulate(my_list, headers=head, tablefmt='pipe'))
elif command == 2:
    my_list = im.read_csv()
    head = im.read_csv()[0]
    my_list.pop(0)
    print(tabulate(my_list, headers=head, tablefmt='pipe'))
elif command == 3:
    path = 'Phonebook.csv'
    valid = exists(path)
    if not valid:
        creating()

    writing_scv(info())
    writing_txt(info())
