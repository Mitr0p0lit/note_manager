print("Добро пожаловать в Менеджер заметок! Вы можете добавить новую заметку.")
username = input("Введите имя пользователя: ")
title = input("Введите заголовок заметки: ")
content = input("Введите описание заметки: ")
while(True):
    status = input("Введите статус заметки (новая, в процессе, выполнено): ")
    if status == "новая" or status == "в процессе" or status == "выполнено":
        break
while(True):
    created_date = input("Введите дату создания (день-месяц-год): ")
    if len(created_date) == 10 and created_date[2] == "-" and created_date[5] == "-":
        day_created_date, month_created_date, year_created_date = created_date.split(sep="-", maxsplit=-1)
        if int(day_created_date) > 31 or int(day_created_date) < 1 :
            print("Ошибка попробуйте ещё раз !")
        elif int(month_created_date) > 12 or int(month_created_date) < 1 :
            print("Ошибка попробуйте ещё раз !")
        else:
            break
    else:
        print("Ошибка попробуйте ещё раз !")
while(True):
    issue_date = input("Введите дедлайн (день-месяц-год): ")
    if len(issue_date) == 10 and issue_date[2] == "-" and issue_date[5] == "-":
        day_issue_date, month_issue_date, year_issue_date = issue_date.split(sep="-", maxsplit=-1)
        if int(day_issue_date) > 31 or int(day_issue_date) < 1 :
            print("Ошибка попробуйте ещё раз !")
        elif int(month_issue_date) > 12 or int(month_issue_date) < 1 :
            print("Ошибка попробуйте ещё раз !")
        else:
            break
    else:
        print("Ошибка попробуйте ещё раз !")
while(True):
    addnote = input("Хотите добавить ещё одну заметку? (да/нет): ")
    if addnote == "да":
        username = input("Введите имя пользователя: ")
        title = input("Введите заголовок заметки: ")
        content = input("Введите описание заметки: ")
        while (True) :
            status = input("Введите статус заметки (новая, в процессе, выполнено): ")

            if status == "новая" or status == "в процессе" or status == "выполнено" :
                break
        while (True) :
            created_date = input("Введите дату создания (день-месяц-год): ")
            if len(created_date) == 10 and created_date[2] == "-" and created_date[5] == "-" :
                day_created_date, month_created_date, year_created_date = created_date.split(sep="-", maxsplit=-1)
                if int(day_created_date) > 31 or int(day_created_date) < 1 :
                    print("Ошибка попробуйте ещё раз !")
                elif int(month_created_date) > 12 or int(month_created_date) < 1 :
                    print("Ошибка попробуйте ещё раз !")
                else :
                    break
            else :
                print("Ошибка попробуйте ещё раз !")
        while (True) :
            issue_date = input("Введите дедлайн (день-месяц-год): ")
            if len(issue_date) == 10 and issue_date[2] == "-" and issue_date[5] == "-" :
                day_issue_date, month_issue_date, year_issue_date = issue_date.split(sep="-", maxsplit=-1)
                if int(day_issue_date) > 31 or int(day_issue_date) < 1 :
                    print("Ошибка попробуйте ещё раз !")
                elif int(month_issue_date) > 12 or int(month_issue_date) < 1 :
                    print("Ошибка попробуйте ещё раз !")
                else :
                    break
            else :
                print("Ошибка попробуйте ещё раз !")
    elif addnote == "нет":
        break
    else:
        print("Ошибка попробуйте ещё раз !")
