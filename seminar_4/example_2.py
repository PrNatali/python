# В фермерском хозяйстве в Карелии выращивают чернику. 
# Она растет на круглой грядке, причем кусты высажены 
# только по окружности.....

from random import randint

berries = [randint(1, 11) for _ in range(int(input('bush total: ')))]
print(*berries)
max = berries[-1] + berries[-2] + berries[0]
current = 0
for i in range (len(berries)-1):
    current = berries[i-1] + berries[i] + berries[i+1]
    if current > max:
        max = current
print(max)
