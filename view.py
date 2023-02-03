from model import write_contact


def add_contact(data, columns):
    print("Заполните данные нового школьника:")
    flag = True
    while flag:
        user = {}
        for column in columns:
            user[column] = input(column + ": ")
        confirm = input(
            "\nНаберите 1 для сохранения информации или нажмите любую клавишу для возврата в меню: ")
        if confirm == "1":
            write_contact(user, data)
        flag = False