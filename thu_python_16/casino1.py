import random
import colorama
from colorama import Fore, Back, Style
colorama.init()

print(Fore.GREEN+'$$$ КАЗИНО $$$')

while True:
	number_player = input('Введите число (от 1 до 10): ')
	number_random = random.randint(1, 5)
	number_player = int(number_player)
	
	if number_player == number_random:
		print(Fore.YELLOW + '$$$ WIN $$$')
	else:
		print(Fore.RED +'Game over')

