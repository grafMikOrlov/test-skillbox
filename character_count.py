import string
from collections import Counter

test_str = "MacBook Pro с M2 перегревается и тротлит сильнее, чем более старая модель. Блогер Вадим Юрьев выяснил " \
           "что 13-дюймовая модель ноутбука серьёзно теряет в производительности под нагрузкой и нагревается аж " \
           "до 108°C с максимальной скоростью вращения кулеров"

# избавляемся от всех пробелов и от символов новой строки
test_str = test_str.translate({ord(stroka): None for stroka in string.whitespace})

# используя collection.Counter() для получения количество каждого элемента в строке
res = Counter(test_str)

# сумма всех значений в счетчике
summa = sum(res.values())

for val in res:
    print(f'{val} - {round(res[val] / summa * 100, 2)}%')

