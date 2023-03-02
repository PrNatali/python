# Определить индексы элементов массива (списка), 
# значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного 
#  максимума)

mas = list(map(int, input("enter the numbers: ").split()))
a = int(input('first: '))
b = int(input('second: '))
print([i for i in range(len(mas)) if a < mas[i] < b])