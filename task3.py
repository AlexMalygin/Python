# Вывести на экран числа от -N до N
print('Введите число N: ');
n = int(input())
a = range(-n,n+1)
for i in a:
    print(i)