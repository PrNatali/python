# Требуется вычислить, сколько раз встречается некоторое число 
# X в массиве A[1..N]. Пользователь в первой строке вводит
# натуральное число N – количество элементов в массиве. 
# В последующих строках записаны N целых чисел Ai. 
# Последняя строка содержит число X

lines = [input('enter the numbers: ') for _ in range(int(input("enter the size: ")))]
count_value = input('enter the value: ')
print(lines.count(count_value))