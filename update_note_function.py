# функция обновления словаря
def update_note(note):
    # что будем обновлять
    if choice == "Имя" or choice == "имя":
        choice_update = "username"
    elif choice == "Заголовок" or choice == "заголовок":
        choice_update = "title"
    elif choice == "Описание" or choice == "описание":
        choice_update = "content"
    elif choice == "Статус" or choice == "статус":
        choice_update = "status"
    elif choice == "Дедлайн" or choice == "дедлайн":
        choice_update = "issue_date"

    # проверка статус это или дедлайн с последующим вводом и проверкой на ошибки (взято из файла multiple)
    if choice_update == "status":
        while (True) :
            status = input("Введите статус заметки (новая, в процессе, выполнена): ")
            if status == "новая" or status == "в процессе" or status == "выполнена" :
                note[choice_update] = status
                break
            else :
                print("Ошибка попробуйте ещё раз !")
    elif choice_update == "issue_date":
        while (True) :
            issue_date = input("Введите дедлайн (день-месяц-год): ")
            if len(issue_date) == 10 and issue_date[2] == "-" and issue_date[5] == "-" :
                day_issue_date, month_issue_date, year_issue_date = issue_date.split(sep="-", maxsplit=-1)
                if int(day_issue_date) > 31 or int(day_issue_date) < 1 :
                    print("Ошибка попробуйте ещё раз !")
                elif int(month_issue_date) > 12 or int(month_issue_date) < 1 :
                    print("Ошибка попробуйте ещё раз !")
                else :
                    note[choice_update] = issue_date
                    break
            else :
                print("Ошибка попробуйте ещё раз !")
    else:
        note[choice_update] = input("Введите новое значение: ")
    print("Заметка успешно обновлена:\n   Имя: ", note["username"], "\n   Заголовок: ", note["title"], "\n   Описание: ", note["content"],
          "\n   Статус: ", note["status"], "\n   Дата создания: ", note["created_date"], "\n   Дедлайн: ",
          note["issue_date"], sep="")

# Основное тело
# инициализируем словарь
note = {'username': 'Артём', 'title': 'Уборка', 'content': 'Помыть посуду', 'status': 'новая', 'created_date': '25-01-2025', 'issue_date': '25-01-2025'}

# Выводим словарь
print("Заметка:\n   Имя: ", note["username"], "\n   Заголовок: ", note["title"], "\n   Описание: ", note["content"], "\n   Статус: ", note["status"],  "\n   Дата создания: ", note["created_date"], "\n   Дедлайн: ", note["issue_date"], sep="")

# цикл выбора с проверкой на ошибки
while(True):
    choice = input("Какие данные вы хотите обновить? (Имя, Заголовок, Описание, Статус, Дедлайн), стоп для завершения: ")

    if choice == "Имя" or choice == "имя" or choice == "Заголовок" or choice == "заголовок" or choice == "Описание" or choice == "описание" or choice == "Статус" or choice == "статус" or choice == "Дедлайн" or choice == "дедлайн":
        update_note(note)
    elif choice == "стоп":
        break
    else:
        print("Ошибка попробуйте ещё раз!")