# 1
def str_formatter(name, age, city):
    return '{}, {} год(а), проживает в городе {}'.format(name, age, city)


print('Задание №1:')
print(str_formatter('Vasya', 21, 'Testoviy'))


# 2
def my_max(one, two, three):
    return max({one, two, three})


print('Задание №2:')
print(my_max(1, 5, 2))


# 3-4
player = {'name': '', 'health': 100, 'damage': 50, 'armor': 1.2}
enemy = {'name': '', 'health': 100, 'damage': 50, 'armor': 1.2}

player['name'] = input('Введите имя игрока: ')
enemy['name'] = input('Введите имя противника: ')


def attack(person1, person2):
    person2['health'] -= calc_damage(person1['damage'], person2['armor'])


def calc_damage(damage, armor):
    return damage / armor


print('Задание №3:')
attack(player, enemy)
print(enemy['health'])