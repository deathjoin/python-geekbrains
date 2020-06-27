# Задание6. Работа с файлами
# Создать модуль music_serialize.py.
# В этом модуле определить словарь для вашей любимой музыкальной группы, например:
# С помощью модулей json и pickle сериализовать данный словарь в json и в байты, вывести результаты в терминал.
# Записать результаты в файлы group.json, group.pickle соответственно.
# В файле group.json указать кодировку utf-8.

import json
import pickle

my_favourite_group = {
    'name': 'Г.М.О.',
    'tracks': [
        'Последний месяц осени',
        'Шапито'
    ],
    'albums': [
        {'name': 'Делать панк-рок', 'year': 2016},
        {'name': 'Шапито', 'year': 2014}
    ]
}

json_group = json.dumps(my_favourite_group, ensure_ascii=False)
pickle_group = pickle.dumps(my_favourite_group)

print(f'JSON Group: {json_group}')
print(f'Pickle Group: {pickle_group}')

with open('group.json', 'w', encoding='utf8') as f:
    json.dump(my_favourite_group, f, ensure_ascii=False)

with open('group.pickle', 'wb') as f:
    pickle.dump(my_favourite_group, f)
