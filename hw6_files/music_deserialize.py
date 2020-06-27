# Задание6. Работа с файлами
# Создать модуль music_deserialize.py.
# В этом модуле открыть файлы group.json и group.pickle, прочитать из них информацию.
# И получить объект: словарь из предыдущего задания.

import pickle
import json

with open('group.json', 'r', encoding='utf8') as f:
    json_group = json.load(f)

with open('group.pickle', 'rb') as f:
    pickle_group = pickle.load(f)


print(json_group)
print(pickle_group)
