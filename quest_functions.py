from time import *
from json import *
from random import *


with open('save.json') as save:
	save = load(save)
	name = save['name']	#имя игрока
	cl = save['cl']		#класс игрока (маг, воин, учёный, рабочий, кастомный)
	pet = save['pet']	#питомец игрока
	hp = save['hp']		#очки здоровья
	ap = save['ap']		#очки силы
	dp = save['dp']		#очки защиты
	lp = save['lp']		#очки удачи
	kp = save['kp']		#очки кармы
	money = save['money']	#деньги
	mana = save['mana']	#очки маны
	mana_on = save['mana_on']		#возможно ли использовать ману
	pp = save['pp']		#количество свободного места в инвентаре (place points)
	situation = save['situation']		#место происходящего


save_dict = {'name':name, 
					'cl':cl, 
					'pet':pet, 
					'hp':hp, 
					'ap':ap, 
					'dp':dp, 
					'lp':lp, 
					'kp':kp, 
					'money':money, 
					'mana':mana, 
					'mana_on':mana_on, 
					'pp':pp, 
					'situation':situation}


def check():
	global name,cl,pet,hp,ap,dp,lp,kp,money,mana,mana_on,pp,situation
	name = save_dict['name']
	cl = save_dict['cl']
	pet = save_dict['pet']
	hp = save_dict['hp']
	ap = save_dict['ap']
	dp = save_dict['dp']
	lp = save_dict['lp']
	kp = save_dict['kp']
	money = save_dict['money']
	mana = save_dict['mana']
	mana_on = save_dict['mana_on']
	pp = save_dict['pp']
	situation = save_dict['situation']

'''
def check():
	global name,cl,pet,hp,ap,dp,lp,kp,money,mana,mana_on,pp,situation
	with open('save.json') as save:
		save = load(save)
		name = save['name']	#имя игрока
		cl = save['cl']		#класс игрока (маг, воин, учёный, рабочий, кастомный)
		pet = save['pet']	#питомец игрока
		hp = save['hp']		#очки здоровья
		ap = save['ap']		#очки силы
		dp = save['dp']		#очки защиты
		lp = save['lp']		#очки удачи
		kp = save['kp']		#очки кармы
		money = save['money']	#деньги
		mana = save['mana']	#очки маны
		mana_on = save['mana_on']		#возможно ли использовать ману
		pp = save['pp']		#количество свободного места в инвентаре (place points)
		situation = save['situation']		#место происходящего
'''
def check2():
	global save_dict
	with open('save.json') as save:
		save = load(save)
		save_dict = {'name':save['name'], 
					'cl':save['cl'], 
					'pet':save['pet'], 
					'hp':save['hp'], 
					'ap':save['ap'], 
					'dp':save['dp'], 
					'lp':save['lp'], 
					'kp':save['kp'], 
					'money':save['money'], 
					'mana':save['mana'], 
					'mana_on':save['mana_on'], 
					'pp':save['pp'], 
					'situation':save['situation']}

def scrypt(line):											#анимация текста
	for x in line:
		print(x, end='')
		#sleep(0.01)


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


def start_numbers(name, cl, file):
	dump({"name": name, 
          "cl": cl, 
		  "pet": "None", 
		  "hp": 12 if cl in ['воин','рабочий'] else 10, 
		  "ap": 0, 
		  "dp": 0, 
		  "lp": randint(1,15), 
		  "kp": 0, 
		  "money": 0, 
		  "mana": 30 if cl == 'маг' else 20, 
		  "mana_on": False, 
		  "pp": 0, 
          "situation": ""},file, indent=4)


def name_ch(a):												#выбор имени
	if len(a)>38:
		scrypt('Длина имени не должна превышать 38.\n')
	
	if a == '':
		scrypt('Пустая строка не может являться именем.\n')
		
	return a


def new_start(a):
	line_1 = f'''
Здравствуйте, {a}, и добро пожаловать в наш прекрасный город Мельбурн!
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
	check()
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
|   ''' + (f'mana:  {man}' if mana_on else ' '*23) + '''           $          |
'''

	scientist = f'''|                                 -@%*@-         |
|   class: {cl1}        %+ %=         |
|   hp:    {hp1}        %+ %+         |
|   power: {ap1}       *%. :@-        |
|   def:   {dp1}      *@=---+@=       |
|   coins: {mon}     *@@@@@@@@@+      |
|   ''' + (f'mana:  {man}' if mana_on else ' '*23) + '''    *@@@@@@@@@@@+     |
'''

	worker = f'''|                                 :=++=.         |
|   class: {cl1}          .=%%=+      |
|   hp:    {hp1}           .%@%%:     |
|   power: {ap1}         .+*.. =@.    |
|   def:   {dp1}       .+#:     +=    |
|   coins: {mon}     .+#:       :.    |
|   ''' + (f'mana:  {man}' if mana_on else ' '*23) + '''    +#:               |
'''

	custom_cl = f'''|                                  .-===:        |
|   class: {cl1}       -=--*##*       |
|   hp:    {hp1}      .++==*##%:      |
|   power: {ap1}      :++++#*+#-      |
|   def:   {dp1}      .+==+##*#.      |
|   coins: {mon}       *#*+##**       |
|   ''' + (f'mana:  {man}' if mana_on else ' '*23) + '''       .+**#*=.       |
'''

	class_list = {'маг':wiz,'воин':warrior,'ученый':scientist,'учёный':scientist,'рабочий':worker}                                                  
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
	global save_dict
	print('map')
	save_dict['hp'] = hp + 1



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