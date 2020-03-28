# Задача5

income = float(input('Напишите значение выручки фирмы, руб: '))
costs = float(input('Напишите значение издержек фирмы, руб: '))
profit = income / costs
if income > costs:
    print(f'Выручка больше издержек. Рентабельность составила {profit:.2f}')
    employees = int(input("Введите количество сотрудников фирмы "))
    print(f'Прибыль фирмы в расчете на одного сотрудника составила {income / employees:.2f}')
elif income == costs:
    print('Выручка равна издержкам')
else:
    income('Издержки больше выручки')

