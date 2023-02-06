# Требуется вывести все целые степени двойки (т.е. числа вида 2k), 
# не превосходящие числа N.

n = int(input())
x = 2
result = 0
for i in range(n +1):
    result = x ** i
    if result >= n:
        break
    print(result)


