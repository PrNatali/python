# Напишите программу, которая на вход принимает два числа A и B,
# и возводит число А в целую степень Bс помощью рекурсии.

def exp (num, x):
    if x == 0:
        return 1
    elif x == 1:
        return num
    else:
        return num * exp(num, x - 1)
print (exp(int(input("number: ")), int(input("exp: "))))
