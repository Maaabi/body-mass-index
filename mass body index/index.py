from colorama import init
from colorama import Fore, Back, Style

init()

print(Fore.WHITE)

print('Привет, Пользователь, это программа для расчёта индекса массы тела')
weight = float(input('Введите ваш вес :'))
height =  float(input('Введите ваш рост :'))
m2 = ((height / 100) * (height / 100))
index = weight / m2
print(Fore.BLACK)
if index < 16:
    print(Back.BLUE)
    print("У вас значительный дефицит массы тела")
if index >= 16 and index < 18.5:
    print(Back.BLUE)
    print("У вас дефицит массы тела")
if index >= 18.5 and index < 25:
    print(Back.GREEN)
    print("У вас нормальный вес")
if index >= 25 and index < 30:
    print(Back.YELLOW)
    print("У вас лишний вес")
if index >= 30 and index < 35:
    print(Back.RED)
    print("У вас ожирение первой степени")
if index >= 35 and index < 40:
    print(Back.RED)
    print("У вас ожирение второй степени")
if index > 40:
    print(Back.RED)
    print("У вас ожирение третьей степени")
    
print(index)
input()
