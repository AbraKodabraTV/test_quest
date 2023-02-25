from quest_functions import *
from json import *
from time import *
from random import *
import sys	#только для sys.exit()


func_list = {'help':help,									#список команд
	         '?':help,
			 'status':status,
			 'inventory':inventory,
			 'map':map,
			 'go to':goto,
			 'attack':attack,
			 'defend':defend,
			 'use item':useitem,
			 'run':run}


scrypt('''\nДля начала квеста введите start, 
для продолжения с контрольной точки введите continue, 
для выхода введите finish.\n''')


line_2 = ('''Доступные команды:

В любой ситуации:
	/help или /? - Список доступных в данный момент команд. 
	/inventory - Ваш инвентарь (доступные предметы).

В Мельбурне:
	/status - Ваш статус. 
	(Во время битвы статус могут посмотреть учёный и воин.)
	/map - Показать карту Мельбурна.
	/go to - Отправиться в локацию из появившегося списка.

Во время битвы:
	/attack - Атаковать предметом в правой руке.
	/defend - Защищаться предметом в левой руке.
	/use item - Использовать предмет из инвентаря.
	/run - Сбежать от врага (шанс сбежать зависит от класса).


В других ситуациях команды могут быть другими.
Их также можно будет увидеть с помощью /help.
Ваше путешествие начинается в городе Мельбурн, столице Летавии.

Что вы будете делать?
''')


print()
while True:
	check2()
	ent = input('/')

	if ent == 'continue' and name == '':
		scrypt('Сохранений не найдено.\n')
		continue

	elif ent=='finish':
		sys.exit()

	elif ent == 'start':
		
		name = input('\nВведите имя: ')
		while name == '' or len(name)>38:
			name = name_ch(name)
			name = input('\nВведите имя: ')
		save_dict['name'] = name

		new_start(name)
		cl = class_ch(input('/'))

		while cl == '':
			cl = class_ch(input('/'))
		save_dict['cl'] = cl
		
		with open('save.json','w') as save: 
			start_numbers(save_dict['name'], 
		 				  save_dict['cl'], 
						  save)
		
		scrypt('\nСоздаётся будущее. Пожалуйста, подождите.\n')

		for i in range(6):
			print('.', end='   ')
			sleep(1)

		print('\n')
		scrypt(line_2)
		save_dict['situation'] = 'Мельбурн'

		check2()

		break

	elif ent == 'continue' and name != '':
		status()
		help()

		break


while True:
	print()
	enter = input('/')

	if enter == 'finish':
		break
	
	if enter == '':
		continue

	if enter not in func_list:
		print()
		scrypt('Эта команда недоступна или неизвестна.\n')

	else:
		func_list[enter]()
		check()

with open('save.json', 'w') as save:
    dump(save_dict, save, indent=4)

scrypt('Прогресс сохранён.')
