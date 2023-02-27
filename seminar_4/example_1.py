# Даны два неупорядоченных набора целых чисел (может быть, 
# с повторениями). Выдать без повторений в порядке возрастания
#  все те числа, которые
# встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого
#  множества. m - кол-во элементов второго множества.
#   Затем пользователь вводит сами элементы множеств

from random import randint
list_1 = {randint(1, 11) for _ in range(int(input('enter the count: ')))}
list_2 = {randint(1, 11) for _ in range(int(input('enter the count2: ')))}
print(list_1, list_2, sep='\n')
print(list_1.intersection(list_2))


