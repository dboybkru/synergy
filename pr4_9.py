# Сортируем список ratings по убыванию рейтинга и названию кафе
ratings = [
    ('Old York', 3.3),
    ('New Age', 4.6),
    ('Old Gold', 3.3),
    ('General Foods', 4.8),
    ('Belissimo', 4.5),
    ('CakeAndCoffee', 4.2),
    ('CakeOClock', 4.2),
    ('CakeTime', 4.1),
    ('WokToWork', 4.9),
    ('WokAndRice', 4.9),
    ('Old Wine Cellar', 3.3),
    ('Nice Cakes', 3.9),
]

ratings.sort(key=lambda x: (-x[1], x[0]))  # сортировка по убыванию рейтинга и по названию кафе

# Создаем словарь cafes, где ключами являются названия кафе, а
# значениями - их рейтинг
from collections import OrderedDict

cafes = OrderedDict(ratings)

# Выводим отсортированный список и словарь
print("Отсортированный список:")
print(ratings)

print("\nСловарь:")
print(cafes)