'''
С помощью библиотеки matplotlib отобразите гистограмму зависимости возраста
(в годах) от выживаемости.
'''
import pandas as pd
import matplotlib.pyplot as plt

file = pd.read_csv('test.csv', encoding='utf-8', sep=',', na_values=[''])

plt.hist(file[file['Survived'] == 1]['Age'].dropna(), color='green', alpha=0.5, label='выжившие')
plt.hist(file[file['Survived'] == 0]['Age'].dropna(), color='red', label='не выжившие', alpha=0.5,)

plt.title('Зависимость выживаемости от возраста')
plt.xlabel('Возраст')
plt.ylabel('Частота')
plt.legend()
plt.show()