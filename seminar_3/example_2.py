# Требуется найти в массиве A[1..N] самый близкий по величине 
# элемент к заданному числу X. Пользователь в первой строке
# вводит натуральное число N – количество элементов в массиве. 
# В последующих строках записаны N целых чисел Ai. Последняя 
# строка содержит число X


lines = [int(input('enter numbers list: ')) for _ in range(int(input('total: ')))]
x = int(input('number: '))
max_num = max(lines)
min_num = min(lines)
if x < min_num:
    print(min_num)
elif x > max_num:
    print(max_num)
else:
    result = 1
    for i in range(len(lines)):
        diff = abs(lines[i] - x)
        if result == diff:
            print(lines[i])
            break
        # result += 1

    

        

    
       


