# Петя, Катя и Сережа делают из бумаги журавликов. 
# Вместе они сделали S журавликов. Сколько журавликов 
# сделал каждый ребенок, если известно, что Петя и Сережа 
# сделали одинаковое количество журавликов, а Катя сделала
#  в два раза больше журавликов, чем Петя и Сережа вместе?

total = int(input('amount enter: '))
for i in range(total):
    kate = (i + i) * 2
    if kate + i + i == total:
        print(f'{i} {kate} {i}')