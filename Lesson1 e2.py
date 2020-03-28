#Задача2

seconds = int(input('Введите число секунд '))
hour = seconds // 3600
minute = (seconds-hour*3600) // 60
second = seconds % 60
print(hour,'час',minute,'мин',second,'сек') #мне так проще смотреть ответ
print(f"{hour}:{minute}:{second}")     #очевидная попытка попасть в формат
print("%02d:%02d:%02d" % (hour, minute, second))  #подсмотренное на форумах решение
