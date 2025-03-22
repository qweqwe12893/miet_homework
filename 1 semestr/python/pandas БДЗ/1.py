import pandas as pd


file = pd.read_csv('train.csv', encoding='utf-8', sep=',', na_values=[''])

# сводная таблица
# groupby() разделяет датафрейм по заданным критериям
# size() подсчитывает количество записей в каждой группе
# unstack() избавляется от подуровней died/survived, добявляя их к столбцам
result = file.groupby(['Pclass', 'Sex', 'Survived']).size().unstack(fill_value=0)

result.columns = ['Died', 'Survived']  # вместо 0 и 1
result = result.reset_index()  # сброс индексов чтобы были на одном уровне

print(result)

'''
С помощью модуля pandas выведите статистику погибших/выживших отдельно
для мужчин и женщин в каждом классе (Pclass).
'''