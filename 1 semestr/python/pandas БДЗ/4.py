import pandas as pd

file = pd.read_csv('train.csv', encoding='utf-8', sep=',', na_values=[''])

# Извлечение имен из столбца Name (по части после титула)
d_copy = file.copy()

#str.extract извлекает подстроки из строкового столбца по регулярному выражению
# \s - пробельный символ
d_copy['FirstName'] = d_copy['Name'].str.extract(r',\s(?:Mr\.|Mrs\.|Miss\.|Master\.|Dr\.|Rev\.|Col\.|Major\.|Mlle\.|Ms\.|Mme\.|Capt\.|Countess\.|Don\.|Sir\.|Lady\.)\s(\w+)')

# извлечение фамилий до запятой
d_copy['LastName'] = d_copy['Name'].str.extract(r'^(\w+),')

# 10 самых популярных имен и фамилий
top_10_first_names = d_copy['FirstName'].value_counts().head(10)
top_10_last_names = d_copy['LastName'].value_counts().head(10)

print(top_10_first_names)
print()
print(top_10_last_names)

'''
4.1. Выведите топ 10 популярных имён.
4.2. Выведите топ 10 популярных фамилий.
'''