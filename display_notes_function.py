
# лёгкая проверка заметок на их заполненность
def check_notes(note_1, note_2, note_3):

    # кол-во заполненых заметок
    number_of_notes = 0

    # так как словарей всего 3, лучше сделать через if
    if note_1["username"] != "":
        number_of_notes += 1
        username = note_1["username"]
        title = note_1["title"]
        content = note_1["content"]
        status = note_1["status"]
        created_date = note_1["created_date"]
        issue_date = note_1["issue_date"]
        display_print(number_of_notes, username, title, content, status, created_date, issue_date)
    if note_2["username"] != "":
        number_of_notes += 1
        username = note_2["username"]
        title = note_2["title"]
        content = note_2["content"]
        status = note_2["status"]
        created_date = note_2["created_date"]
        issue_date = note_2["issue_date"]
        display_print(number_of_notes, username, title, content, status, created_date, issue_date)
    if note_3["username"] != "":
        number_of_notes += 1
        username = note_3["username"]
        title = note_3["title"]
        content = note_3["content"]
        status = note_3["status"]
        created_date = note_3["created_date"]
        issue_date = note_3["issue_date"]
        display_print(number_of_notes, username, title, content, status, created_date, issue_date)
    if number_of_notes == 0:
        print("У вас нет сохранённых заметок.")


# Вывод
# можно было сделать всё в одну строку, но мне кажется так удобнее
def display_print(number_of_notes, username, title, content, status, created_date, issue_date):
    if number_of_notes == 1:
        print("Список заметок:")
        print("------------------------------")
    print("Заметка №", number_of_notes,":", sep="")
    print("Имя пользователя:", username)
    print("Заголовок:", title)
    print("Описание:", content)
    print("Статус:", status)
    print("Дата создания:", created_date)
    print("Дедлайн:", issue_date)
    print("------------------------------")

# заметки
note_1 = {'username': 'Алексей', 'title': 'Список покупок', 'content': 'Купить продукты на неделю', 'status': 'новая', 'created_date': '27-11-2024', 'issue_date': '30-11-2024'}
note_2 = {'username': 'Мария', 'title': 'Учеба', 'content': 'Подготовиться к экзамену', 'status': 'в процессе', 'created_date': '25-11-2024', 'issue_date': '01-12-2024'}
note_3 = {'username': '', 'title': '', 'content': '', 'status': '', 'created_date': '', 'issue_date': ''}

check_notes(note_1, note_2, note_3)