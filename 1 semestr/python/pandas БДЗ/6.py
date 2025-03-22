'''
На основе статистики попытайтесь предсказать выживаемость для пассажиров из
файла test.csv.
'''
import pandas as pd

file = pd.read_csv('test.csv', encoding='utf-8', sep=',', na_values=[''])
dat = file.copy()

def survival_prediction(row):
    if (row['Sex'] == 'female') and (row['Pclass'] == 1 or row['Pclass'] == 2):
        return 1
    if (row['Embarked'] == 'C'):
        return 1
    if (row['Sex'] == 'male') and (row['Pclass'] == 1):
        return 1
    else:
        return 0
    
dat['Предполагаемое выживание'] = dat.apply(survival_prediction, axis=1)

dat.to_csv('test_6.csv', index=False)