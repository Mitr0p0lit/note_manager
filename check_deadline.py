import datetime

# Запрашиваем у пользователя ввод дедлайна
user_input = input("Введите дедлайн заметки в формате 'день-месяц-год': ")

# Проверяем, состоит ли ввод из 10
if len(user_input) == 10:
    # Если формат правильный, преобразуем строку в объект даты
    issue_date = datetime.datetime.strptime(user_input, "%d-%m-%Y").date()
else:
    print("Неверный формат даты. Пожалуйста, используйте формат 'день-месяц-год'.")
    exit()
# Получаем текущую дату
current_date = datetime.date.today()
print("Текущая дата:", current_date)

# Сравниваем дедлайн с текущей датой
if issue_date < current_date:
    print("Дедлайн истёк! Пожалуйста, обратите на это внимание.")
elif issue_date == current_date:
    print("Сегодня последний день для выполнения задачи!")
else:
    days_left = (issue_date - current_date).days
    print(f"Дедлайн ещё не истёк. Осталось {days_left} дней до истечения срока.")