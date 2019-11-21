# Simple calc v2

from colorama import init
from colorama import Fore, Back, Style

# use Colorama to make Termcolor work on Windows too
init()

print(Fore.WHITE)

print(Back.MAGENTA)

print('Переключите клавиатуру на \'Eng\'')

print( Fore.BLACK ) # делаем ШРИФТ чёрным

print( Back.GREEN ) # делаем ФОН зелёным (последующего выводв текста)

what = input('Выберите действие ( +, -, *, / ) и нажмите ENTER: ')

print( Back.CYAN )  # делаем ФОН голубым (последующего выводв текста)

a = float(input('Введите первое число и нажмите ENTER: '))
b = float(input('Введите второе число и нажмите ENTER: '))

print( Back.YELLOW)  # делаем ФОН жёлтым (последующего выводв текста)

if what == '+':
	c = a + b
	print('Результат: ' + str(c))
elif what == '-':
	c = a - b
	print('Результат: ' + str(c))
elif what == '*':
	c = a * b
	print('Результат: ' + str(c))
elif what == '/':
	c = a / b
	print('Результат: ' + str(c))
else:
	print('Выбрана неверная операция')

print(Fore.WHITE)
print(Back.MAGENTA)

print(' Для окончания нажмите ENTER\n\n')

print(' Для повторных вычислений снова запустите файл')

input()

