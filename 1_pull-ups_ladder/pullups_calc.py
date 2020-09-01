print('WELCOME to \'THE ULTIMATE PULL-UPS LADDER WORKOUT\'!')


# choosing the way to do pull-ups ladder
def ladder_technique():
	choice = None
	while choice not in ['1', '2']:
		choice = (input('''\nPlease, select a ladder technique to do the workout. Press:
1 - for one-way ladder (e.g. 1-2-3)
2 - for two-way ladder (e.g. 1-2-3-3-2-1): '''))
	return choice


# calc and print for a one-way ladder
def one_way_ladder(n):
    if n == 0:
        print(f'\nZero pull-ups means no pull-ups!!!')
        return
    elif n == 1:
        print(f'\nSet #{n} -- {n} pull-up')
        print('-' * len(f'Set #{n} -- {n} pull-up'))
        print(f'You\'ll complete {n} pull-up!')
        return
    max_len = len(f'Set #{n} -- {n} pull-ups')  # aux variable for output print alignment
    result = 0
    i = 1
    while i <= n:
        if i <= 1:
            print(f'\nSet #{i} -- {i} pull-up', ' ' * (max_len - len(f'Set #{i} -- {i} pull-up')) + ' *' * i, sep=' ')
            result += i
            i += 1        
        print(f'Set #{i} -- {i} pull-ups', ' ' * (max_len - len(f'Set #{i} -- {i} pull-ups')) + ' *' * i, sep=' ' )
        result += i
        i += 1
    print('-' * len(f'Set #{i} -- {i} pull-ups'))
    print(f'You\'ll complete {result} pull-ups!')


# calc and print for a two-way ladder
def two_way_ladder(n):
    max_len = len(f'Set #{n + 1} -- {n} pull-ups')  # aux variable for output print alignment
    if n == 0:
        print(f'\nZero pull-ups means no pull-ups!!!')
        return
    elif n == 1:
        print(f'\nSet #{n} -- {n} pull-up')
        print(f'Set #{n + 1} -- {n} pull-up')
        print('-' * len(f'Set #{n} -- {n} pull-up'))
        print(f'You\'ll complete {n + 1} pull-ups!')
        return
    result = 0
    i = 1
    while i <= n:
        if i <= 1:
            print(f'\nSet #{i} -- {i} pull-up', ' ' * (max_len - len(f'Set #{i} -- {i} pull-up') + 1) + ' *' * i, sep=' ')
            result += i
            i += 1        
        print(f'Set #{i} -- {i} pull-ups', ' ' * (max_len - len(f'Set #{i} -- {i} pull-up')) + ' *' * i, sep=' ')
        result += i
        i += 1
    k = i
    while i > 1:
        i -= 1
        if i > 1:
            print(f'Set #{k} -- {i} pull-ups', ' ' * (max_len - len(f'Set #{k} -- {i} pull-up')) + ' *' * i, sep=' ')
            result += i
            k += 1
            continue
        print(f'Set #{k} -- {i} pull-up', ' ' * (max_len - len(f'Set #{k} -- {i} pull-up') + 1) + ' *' * i, sep=' ')
        result += i
    print('-' * max_len)
    print(f'You\'ll complete {result} pull-ups!')


# running the script based on the user choice
def run_the_script(user_input):
    if user_input == '1':
    	print('\nWelcome to a one-way ladder workout!')
    	max_num = int(input('Enter the max number of pull-ups you want to do: '))
    	one_way_ladder(max_num)
    else:
    	print('\nWelcome to a two-ways ladder workout!')
    	max_num = int(input('Enter the max number of pull-ups you want to do: '))
    	two_way_ladder(max_num)


run_the_script(ladder_technique())