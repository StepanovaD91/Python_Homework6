#Задача 32: 
# Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума)

a = list(map(int, input('Введите массив: ').split()))

mini = int(input('Min: '))
maxi = int(input('Max: '))
print(*[i for i in range(len(a)) if mini <= a[i] <= maxi])