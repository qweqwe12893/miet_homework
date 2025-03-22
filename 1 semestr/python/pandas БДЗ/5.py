'''
Заполните все отсутствующие в train.csv значения медианой (по столбцу).
'''
import pandas as pd

file = pd.read_csv('train.csv', encoding='utf-8', sep=',', na_values=[''])

filled_train = file.copy()

# median(numeric_only=True) вычисляет медиану только для числовых столбцов
# fillna заполняет все значения NaN в числовых столбцах медианными значениями
filled_train = filled_train.fillna(filled_train.median(numeric_only=True))

# ffill() заполняет NaN значениями из предыдущих строк
# bfill() заполняет NaN значениями из следующих строк
filled_train = filled_train.ffill().bfill()

# новый файл
filled_train.to_csv('filled_train.csv', index=False)
