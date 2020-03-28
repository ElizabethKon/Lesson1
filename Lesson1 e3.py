#Задача 3 [Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn]

n = int(input('Введите целое число n '))
str_n = str(n)
str_nn = str_n + str_n
str_nnn = str_nn + str_n

number1 = int(str_n)
number2 = int(str_nn)
number3 = int(str_nnn)

sum = number1 + number2 + number3

#print(str_n)
#print(str_nn)
#print(str_nnn)
print(f'Сумма чисел (n + nn + nnn) равна {sum}')
