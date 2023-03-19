def show_data() -> str:
    '''Эта функция показывает содержимое справочника'''
    with open(file_name, 'r', encoding='utf-8') as file:
        book = file.read().split('\n')
    return book


def new_data() -> str:
    '''Добавляет новую информацию в справочник'''
    info = input('Введите данные: ')
    with open(file_name, 'a', encoding='utf-8') as file:
        file.write(f'\n{info}')


def search_data() -> str:
    '''Поиск информации в справочнике'''
    info = input('Введите данные: ')
    with open(file_name, 'r', encoding='utf-8') as file:
        book = file.read().split('\n')
        for i in book:
            if info in i:
                print(i)
        if info not in i:
            print('Информация не найдена')


def delete_data():
    '''Поиск информации в справочнике и удаление'''
    info = input('Введите данные: ')
    temp = []
    temp2 = 0
    temp3 = 0
    with open(file_name, 'r', encoding='utf-8') as file:
        book = file.read().split('\n')
    file.close()
    for i in book:
        if info in i:
            temp.append(book.index(i))
            temp3 = temp[0]
            temp2 = i
    if len(temp) > 1:
        info = input('Найдено несколько пользователей:\
                    \n вернитесь в режим №4 и уточните данные\
                    \n Нажмите Enter чтобы вернуться в меню ')
    elif len(temp) == 0:
        print('Данные не найдены')
    else:
        while True:
            mode = input(f'Найден пользователь с данными:\
                        \n {temp2}\
                        \n Удалить данные пользователя? да/нет\
                        \n : ')
            if mode == "да":
                book.pop(temp3)
                with open(file_name, 'w', encoding='utf-8') as file:
                    print(*book, file=file, sep="\n")
                    break
            elif mode == "нет":
                break


def edit_data():
    '''Поиск информации в справочнике и коректировка значений'''
    info = input('Введите данные: ')
    temp = []
    temp2 = 0
    temp3 = 0
    with open(file_name, 'r', encoding='utf-8') as file:
        book = file.read().split('\n')
    file.close()
    for i in book:
        if info in i:
            temp.append(book.index(i))
            temp3 = temp[0]
            temp2 = i
    if len(temp) > 1:
        info = input('Найдено несколько пользователей:\
                    \n вернитесь в режим №5 и уточните данные\
                    \n Нажмите Enter, чтобы вернуться в меню ')
    elif len(temp) == 0:
        print('Данные не найдены')
    else:
        temp2 = input(f'Найден пользователь с данными:\
                    \n {temp2}\
                    \n Скорректируйте данные \
                    \n : ')
        book[temp3] = temp2
        with open(file_name, 'w', encoding='utf-8') as file:
            print(*book, file=file, sep="\n")


file_name = 'data.txt'

while True:
    mode = input('Выберите режим работы справочника:\
                \n 1 - Показать содержимое\
                \n 2 - Добавить информацию\
                \n 3 - Найти значение\
                \n 4 - Удалить искомое значение\
                \n 5 - Редактировать искомое значение\
                \n 0 - Выйти из режима\
                \n Режим: ')
    if mode == '1':
        print(show_data())
    elif mode == '2':
        new_data()
    elif mode == '3':
        search_data()
    elif mode == '4':
        delete_data()
    elif mode == '5':
        edit_data()
    elif mode == "0":
        break
    else:
        print('No mode')
