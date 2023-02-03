from model import get_columns
from view import add_contact
from model import find_contact, read_data, add_column, write_data, izm_contact, del_contact


def user_interface():
    data = read_data()
    columns = get_columns(data)
    flag = True
    while flag:
        print("\n***** ДОБРО ПОЖАЛОВАТЬ В БАЗУ ДАННЫХ! *****\n\nВыберите пункт меню для продолжения:")
        while True:
            print("1 - Найти школьника")
            print("2 - Добавить школьника")
            print("3 - Показать список всех школьников")
            print("4 - Изменить данные в записи о школьнике")
            print("5 - Удалить запись о школьнике")
            print("6 - Выход")
            choice = input()
            if choice not in ["1", "2", "3", "4", "5", "6"]:
                print("!!Выбран неверный пункт меню!! \n Попробуйте ещё раз")
                continue
            if choice == "1":
                find_contact(data)
                break
            elif choice == "2":
                add_contact(data, columns)
                break
            elif choice == "3":
                print(columns)
                print(data)
            elif choice == "4":
                 izm_contact(data)
            elif choice == "5":
                del_contact(data)
                break
            else:
                flag = False
                write_data(data, columns)
                break