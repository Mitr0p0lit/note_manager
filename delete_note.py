
# создаём список с данными
list_of_notes = ["Алексей", "Список продуктов", "Купить продукты на неделю", "Мария", "Учёба", "Подготовиться к экзамену"]

# бесконечный цикл
while(True):

    # переменная для отображения кол-ва пользователей
    number_user = 1

    # вывод списка
    if list_of_notes[0] != "":
        print(number_user, ".", " Имя: ", list_of_notes[0], "\n   Заголовок: ", list_of_notes[1], "\n   Описание: ", list_of_notes[2], sep="")
        number_user += 1
    if list_of_notes[3] != "":
        print(number_user, ".", " Имя: ", list_of_notes[3], "\n   Заголовок: ", list_of_notes[4], "\n   Описание: ", list_of_notes[5], sep="")

    # выбор действия
    print("[1]. Введите имя пользователя или заголовок для удаления заметки\n[2]. Стоп или 0 для завершения программы")
    action = input("Выбор: ")

    # непосредственно действие со список (удаление или завершение)
    if action == list_of_notes[0] or action == list_of_notes[1]:
        list_of_notes[0] = ""
    elif action == list_of_notes[3] or action == list_of_notes[4]:
        list_of_notes[3] = ""
    elif action == "стоп" or action == "Стоп" or action == 0:
        print("Программа завершена, досвидание :)")
        break
    else:
        print("Заметок с таким именем пользователя или заголовком не найдено, попробуйте ещё раз")