# Найти максимальное из пяти чисел
massiv = [1,5,63,42,6]
max = massiv[0]
for i in massiv:
    if i>max:
        max=i
print('наибольшее число: ', max)