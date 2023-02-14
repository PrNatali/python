#Найдите сумму цифр трехзначного числа.
n = int(input('enter the number: '))
total = 0
while n > 0:
    last_dig = n % 10
    total += last_dig
    n //= 10
print(total)
