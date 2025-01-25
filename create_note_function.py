import datetime

current_date = datetime.date.today()
formatted_date = current_date.strftime("%d-%m-%Y")

dictionary_of_notes = {}

# Взято из файла multiple_notes отчасти
print("Добро пожаловать в Менеджер заметок!")

username = input("Введите имя пользователя: ")
title = input("Введите заголовок заметки: ")
content = input("Введите описание заметки: ")
while(True):
    status = input("Введите статус заметки (новая, в процессе, выполнено): ")
    if status == "новая" or status == "в процессе" or status == "выполнено":
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

        dictionary_of_notes["username"] = username
        dictionary_of_notes["title"] = title
        dictionary_of_notes["content"] = content
        dictionary_of_notes["status"] = status
        dictionary_of_notes["created_date"] = formatted_date
        dictionary_of_notes["issue_date"] = issue_date
        print(dictionary_of_notes)
        break

    else:
        print("Ошибка попробуйте ещё раз !")