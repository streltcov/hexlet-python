########################################################################################################################
#
# № 2 - Синтаксис
#
# src/solution.py
#
# В этой практике вам нужно реализовать две функции:
#
#     функцию make_user, которая должна принимать два параметра — имя пользователя и возраст (число). Вернуть функция
#     должна словарь с ключами 'name' и 'age', по которым должны быть сохранены соответствующие значения
#     функцию format_user, которая, будучи применена к результату вызова make_user (помним — это словарь), должна
#     вернуть строку вида 'Phil, 25'
#
# Пример:
#
# >>> phil = make_user('Phil', 25)
# >>> type(phil)
# <class 'dict'>
# >>> format_user(phil)
# 'Phil, 25'
#
# SOLUTION:

# BEGIN (write your solution here)


def make_user(name, age):
    return {'name': name, 'age': age}


def format_user(user):
    return str(user.get('name')) + ', ' + str(user.get('age'))

# END

#
########################################################################################################################
#
# № 3 - Изменение данных в словаре
#
# src/solution.py
#
# Цель упражнения — функция count_all. Эта функция должна принимать на вход iterable источник и возвращать словарь,
# ключами которого являются элементы источника, а значения отражают количество повторов элемента в коллекции-источнике
# Вот пара примеров, демонстрирующих то, как функция должна работать:
#
# >>> count_all(["cat", "dog", "cat"])
# {"cat": 2, "dog": 1}
# >>> count_all("hello")
# {'h': 1, 'e': 1, 'l': 2, 'o': 1}
# >>> count_all("*" * 20)
# {'*': 20}
#
# SOLUTION:

# BEGIN (write your solution here)


def count_all(items):
    result = {}
    for item in items:
        if item not in result:
            result[item] = 1
        else:
            result[item] = result[item] + 1
    return result

# END

#
########################################################################################################################
#
# № 4 - Инициализация новых значений и defaultdics
#
# src/solution.py
#
# Цель упражнения — функция collect_indexes. Эта функция должна принимать на вход коллекцию (некий iterator/iterable)
# и возвращать словарь (или подобная ему коллекция!), где ключом будет элемент коллекции, а значением для ключа
# — список индексов коллекции, по которым встречается этот элемент
# Пример
#
# >>> d = collect_indexes("hello")
# >>> d["h"]
# [0]
# >>> d["e"]
# [1]
# >>> d["l"]
# [2, 3]
#
# SOLUTION:

# BEGIN (write your solution here)

# Rev. v.1


def collect_indexes(items):
    result = {}
    for index, item in enumerate(items):
        if item in result:
            result[item].append(index)
        else:
            result[item] = [index]
    return result

# END

# Rev v.2


# BEGIN (write your solution here)

from collections import defaultdict


def collect_indexes(items):
    result = defaultdict(list)
    for index, item in enumerate(items):
        result[item].append(index)
    return result

# END

#
########################################################################################################################
