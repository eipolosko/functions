def sum(a,b,operation):
    return a+b

def razn(a, b, operation):
    return a - b

def proiz(a, b, operation):
    return a * b

def chastnoe(a, b, operation):
    try:
        print('Частное равно  ',a/b)
    except ZeroDivisionError:
        print('На ноль делить нельзя')

a=float(input('Введите первое число   '))
operation=input('Введите знак  ')
b=float(input('Введите второе число '))
exit=1
while exit!=0:
    if operation=='+':
        print('Сумма равна  ',sum(a, b, operation))
    if operation=='-':
        print('Разность равна  ',razn(a, b, operation))
    if operation=='*':
        print('Произведение равно  ',proiz(a, b, operation))
    if operation=='/':
        chastnoe(a, b, operation)
    print('Хотите продолжить?\n 1-ДА\n 0-НЕТ    ')
    exit=int(input())
    if exit==0:
        break
    a=float(input('Введите первое число   '))
    operation=input('Введите знак  ')
    b=float(input('Введите второе число   '))




