import pandas as pd


file = pd.read_csv('train.csv', encoding='utf-8', sep=',', na_values=[''])

# сводная таблица
# size() подсчитывает количество записей в каждой группе
# unstack() избавляется от подуровней died/survived, добявляя их к столбцам
destination_dependence = file.groupby(['Embarked', 'Survived']).size().unstack() 

print(destination_dependence)
# вычисление процента выживших для каждого порта
                                          # выжившие / общее кол-во
destination_dependence['Выжившие (%)'] = (destination_dependence[1] / (destination_dependence[0] + destination_dependence[1])) * 100

# C - Cherbourg, Q - Queenstown, S - Southampton
print(destination_dependence[['Выжившие (%)']])

# порт влияет на выживаемость, больше всего выжило пассажиров, едущих в шембург


'''
Определите, влияет ли порт посадки на выживаемость.
'''