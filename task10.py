# Найти расстояние между двумя точками пространства
import math
x1=int(input('Введите Координату x1 '))
x2=int(input('Введите Координату x2 '))
y1=int(input('Введите Координату y1 '))
y2=int(input('Введите Координату y1 '))
z1=int(input('Введите Координату z1'))
z2=int(input('Введите Координату z2 '))
print('координаты точки в пространстве')
print(x1,x2,y1,y2,z1,z2)
distance = math.sqrt((x2-x1)*(x2-x1)+(y2-y1)*(y2-y1)+(z2-z1)*(z2-z1))
print('расстояние между точками')
print(distance)