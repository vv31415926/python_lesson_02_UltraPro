'''
Выполнить задание уровня pro
Написать программу “Угадай число”. Программа должна с помощью наводящих вопросов отгадать число.
'''

# https://github.com/vv31415926/python_lesson_02_Pro

# Угадай число
import random

num = random.randint( 1,1000000 )
print('Игрок это не замечает: задумано '+str(num) )

print( 'Отгадайте заданное компьютером целое положительное число. (Отказ угадать:0)')
count=1
while True:
    s = input( 'Попытка {}:'.format(count) )
    if s.isdigit() == False:
        print( 'Ошибка ввода. Ввести надо целое положительное число')
        continue
    n = int( s )
    if n == 0:
        print( 'Вы не захотели угадать число... Прощайте!')
        break
    if n > num:
        print( 'Много')
    elif n < num:
        print( 'Мало')
    else:
        print( 'Задуманное число {} угадано за {} попыток!'.format( n,count ))
        break
    count += 1
