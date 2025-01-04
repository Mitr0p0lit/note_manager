status = {1: "выполнено", 2: "в процессе", 3: "отложено", 4: "не определён"}
x = 4
print("Текущий статус заметки:", status[x])
while(True):
      print("1. Обновить статус")
      print("0. Завершить работу")
      y = int(input("Ваш выбор: "))
      if y == 1:
            while(True):
                  print("Выберите новый статус заметки:")
                  for i in range(4):
                        i += 1
                        print(i, status[i])
                  x = int(input("Ваш выбор: "))
                  if x < 1 or x > 4:
                        print("Ошибка !")
                        print("Попробуйте ещё раз")
                  else:
                        print("Статус заметки успешно обновлён на:", status[x])
                        break
      if y == 0:
            break
      if y != 1 or 0:
            print("Ошибка !")
            print("Попробуйте ещё раз")