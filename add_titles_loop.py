headlines = [] # Создаём список

# Создаём цикл с вводом заголовка от пользователя
while True:
    headline = input("Введите заголовок (или оставьте пустым для завершения): ")
    if headline == "" or headline == "стоп": # проверяем на завершение
         break
    headlines.append(headline) # если программа не завершена то добавляем заголовок в список

print("\nЗаголовки заметки:") # выводим заголовки пользователя
for headline in headlines:
    print(f"-{headline}")