import math
print('Введите коэффициенты квадратного уравнения: ')
a = float(input('a = '))
b = float(input('b = '))
c = float(input('c = '))
if a != 0:
    Discr = b**2-4*a*c
    if Discr > 0:
        x1 = (-b+math.sqrt(Discr))/(2*a)
        x2 = (-b-math.sqrt(Discr))/(2*a)
        print("x1 = %.2f\nx2 = %.2f" % (x1, x2))
    elif Discr == 0:
        x = (-b)/(2*a)
        print('x1=x2 = ', x)
    elif Discr < 0:
        print('Нет вещественных корней')
elif a == 0:
    x = (-c)/b
    print('x = ', x)
elif (a == 0) and (b == 0) and (c != 0):
    print('Неверное уравнение')
elif (a == 0) and (b == 0) and (c == 0):
    print('Все коэффициенты равны нулю')
else:
    print('Ошибка')
