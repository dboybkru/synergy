import pandas as pd
from datetime import datetime
import statistics

# Загрузка данных из CSV файла
df = pd.read_csv('e:/ufo.csv', sep=',')

# Преобразование времени к формату datetime
df['Time'] = pd.to_datetime(df['Time'])

# Задание 1: В каком году отмечается наибольшее количество случаев наблюдения НЛО в США?
df['Year'] = df['Time'].dt.year
year_with_most_sightings = df['Year'].value_counts().idxmax()
print(f"Год с наибольшим количеством случаев наблюдения НЛО: {year_with_most_sightings}")

# Задание 2: Найдите средний интервал времени (в днях) между двумя последовательными случаями наблюдения НЛО в штате Невада (NV).
nevada_sightings = df[df['State'] == 'NV']
nevada_sightings = nevada_sightings.sort_values(by='Time')

# Вычисляем интервалы между последовательными датами
intervals = nevada_sightings['Time'].diff().dropna().dt.days

# Находим среднее значение интервалов
average_interval = intervals.mean()
print(f"Средний интервал времени между наблюдениями НЛО в Неваде: {average_interval} дней")