# Требуется определить, можно ли от шоколадки размером n × m
# долек отломить k долек, если разрешается сделать один разлом
# по прямой между дольками (то есть разломить шоколадку на два
# прямоугольника).

print('enter chokolate size and piece')
m, n, k = int(input()), int(input()), int(input())
if k % m == 0 or k % n == 0:
    print('yes')
else: print('no')