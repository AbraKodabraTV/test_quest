from time import *
from random import *
import sys	#только для sys.exit()

name = ''	#имя игрока
cl = ''		#класс игрока (маг, воин, учёный, рабочий, кастомный)
pet = 'None'#питомец игрока
hp = 0		#очки здоровья
ap = 0		#очки силы
dp = 0		#очки защиты
lp = 0		#очки удачи
kp = 0		#очки кармы
money = 0	#деньги
mana = 0	#очки маны
pp = 0		#количество свободного места в инвентаре (place points)

situation = ''		#место происходящего


def scrypt(line):											#анимация текста
	for x in line:
		print(x, end='')
		sleep(0.01)

def help():													#команда help
	global cl 
	scrypt('''Доступные команды:
/help или /? - Список доступных в данный момент команд.
/inventory - Ваш инвентарь (доступные предметы).
''')
	if situation == 'битва' and cl in ['учёный','воин']:
		scrypt('''/status - Посмотреть статус.
/attack - Атаковать предметом в правой руке.
/defend - Защищаться предметом в левой руке.
/use item - Использовать предмет из инвентаря.
/run - Сбежать от врага (шанс сбежать зависит от класса).
''')
	elif situation == 'битва':
		scrypt('''/attack - Атаковать предметом в правой руке.
/defend - Защищаться предметом в левой руке.
/use item - Использовать предмет из инвентаря.
/run - Сбежать от врага (шанс сбежать зависит от класса).
''')
	elif situation == 'Мельбурн':
		scrypt('''/status - Посмотреть статус.
/map - Показать карту Мельбурна.
/go to [location] - Отправиться в выбранную локацию.
''')
	scrypt('''/finish - Закончить игру.

''')

class numbs:
	def num_stat(x,y):
		return str(x) + ' '*(y - len(str(x)))

def status():												#команда status
	global name
	global cl
	global hp
	global ap
	global dp
	global money
	global mana
	global situation
	global pet
	n = numbs.num_stat(name, 39)
	cl1 = numbs.num_stat(cl, 16)
	hp1 = numbs.num_stat(hp, 16)
	ap1 = numbs.num_stat(ap, 16)
	dp1 = numbs.num_stat(dp, 16)
	mon = numbs.num_stat(money, 16)
	man = numbs.num_stat(mana, 16)
	loc = numbs.num_stat(situation, 35)
	p = numbs.num_stat(pet, 40)


	wiz = f'''|                                    .-==--.     |
|   class: {cl1}        :*###+--=-    |
|   hp:    {hp1}       =#####.   :    |
|   power: {ap1}      .######:        |
|   def:   {dp1} .::..*#######+-:..   |
|   coins: {mon}+####%%%%#*#*#%####*: |
|   mana:  {man}=######%%%#######+-.  |
'''

	warrior = f'''|                                     +          |
|   class: {cl1}         .:*:.        |
|   hp:    {hp1}           @          |
|   power: {ap1}           @          |
|   def:   {dp1}           $          |
|   coins: {mon}           $          |
|                                     $          |
'''

	scientist = f'''|                                    .-==--.     |
|   class: {cl1}        :*###+--=-    |
|   hp:    {hp1}       =#####.   :    |
|   power: {ap1}      .######:        |
|   def:   {dp1} .::..*#######+-:..   |
|   coins: {mon}+####%%%%#*#*#%####*: |
|                          =######%%%#######+-.  |
'''

	worker = f'''|                                    .-==--.     |
|   class: {cl1}        :*###+--=-    |
|   hp:    {hp1}       =#####.   :    |
|   power: {ap1}      .######:        |
|   def:   {dp1} .::..*#######+-:..   |
|   coins: {mon}+####%%%%#*#*#%####*: |
|                          =######%%%#######+-.  |
'''

	custom_cl = f'''|                                    .-==--.     |
|   class: {cl1}        :*###+--=-    |
|   hp:    {hp1}       =#####.   :    |
|   power: {ap1}      .######:        |
|   def:   {dp1} .::..*#######+-:..   |
|   coins: {mon}+####%%%%#*#*#%####*: |
|                          =######%%%#######+-.  |
'''

	class_list = {'маг':wiz,'воин':warrior,'учёный':scientist,'рабочий':worker}                                                  
															#список классов

	if cl in class_list:
		stat_display = f'''
 ________________________________________________
/                                                \\
|   name: {n}|
|                                                |
''' + class_list[cl] + f'''|                                                |
|                                                |
|   location: {loc}|
|                                                |
|   pet: {p}|
|                                                |
\\________________________________________________/
'''
	else:
		stat_display = f'''
 ________________________________________________
/                                                \\
|   name: {n}|
|                                                |
''' + custom_cl + f'''|                                                |
|                                                |
|   location: {loc}|
|                                                |
|   pet: {p}|
|                                                |
\\________________________________________________/
'''

	print(stat_display)

def inventory():											#команда inventory
	print('inventory')

def map():													#команда map
	print('map')

def goto():													#команда goto
	print('go to')

def attack():												#команда attack
	print('attack')

def defend():												#команда defend
	print('defend')

def useitem():												#команда useitem
	print('use item')

def run():													#команда run
	print('run')


func_list = {'help':help, '?':help,'status':status,'inventory':inventory,
'map':map,'go to':goto,'attack':attack,'defend':defend,'use item':useitem,
'run':run}													#список команд


def class_ch(a):											#выбор класса
	if len(a)>16:
		scrypt('''Длина названия класса не должна превышать 16.\n''')
		return ''
	if a.lower() == 'маг':
		scrypt('''\nВы выбрали класс Маг!
Ваше будущее наполнено волшебством!\n''')
	elif a.lower() == 'воин':
		scrypt('''\nВы выбрали класс Воин!
Ваше будущее наполнено подвигами!\n''')
	elif a.lower() in ['учёный','ученый']:
		scrypt('''\nВы выбрали класс Учёный!
Ваше будущее наполнено загадками!\n''')
	elif a.lower() == 'рабочий':
		scrypt('''\nВы выбрали класс Рабочий!
Ваше будущее наполнено житейскими радостями!\n''')
	elif a == '':
		scrypt('Выберите класс\n')
	else:
		scrypt(f'''\nВы выбрали класс {a[0].upper() + a[1:]}!
Ваше будущее наполнено приключениями!\n''')

	return a.lower()



scrypt('\nДля начала квеста введите start, для выхода введите finish\n')

ent = input('/')

while ent not in ['start','finish']:
	ent = input('/')

if ent=='finish':
	sys.exit()

name = input('\nВведите имя: ')
while name == '' or len(name)>38:
	if len(name)>38:
		scrypt('Длина имени не должна превышать 38.\n')
	
	if name == '':
		scrypt('Пустая строка не может являться именем.\n')

	name = input('\nВведите имя: ')


line_1 = f'''
Здравствуйте, {name}, и добро пожаловать в наш прекрасный город Мельбурн!
Перед началом путешествия вам досталась редкая возможность выбрать своё будущее!
Сейчас не время отключать мозг, этот выбор определит всё дальнейшее прохождение!
На выбор есть:

/маг
/воин
/учёный
/рабочий
/[любой другой класс]

'''
scrypt(line_1)

while cl == '':
	cl = class_ch(input('/'))

scrypt('\nСоздаётся будущее. Пожалуйста, подождите.\n')
for i in range(6):
	print('.', end='   ')
	sleep(1)
print('\n')


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
scrypt(line_2)

situation = 'Мельбурн'

while True:
	print('')
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
