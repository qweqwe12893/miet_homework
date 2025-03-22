import pandas as pd


file = pd.read_csv('train.csv', encoding='utf-8', sep=',', na_values=[''])

# оставляет только int и float
num = file.select_dtypes(include='number')

num = num.groupby([file['Sex'], file['Survived']]).mean()
num = num.drop(columns='Survived')  # удаляет столбец с именем 'Survived' тк по нему сортируем
num = num.drop(columns='PassengerId')  # нет смысла искать среднее у id

num.columns = ['Класс билета', 'Возраст пассажира', 'Братья-сестры', 'Родители-дети', 'Тариф']

print(num)


'''
помощью модуля pandas выведите статистику по всем числовым полям,
отдельно для мужчин и женщин.
'''