f = open('players.csv')
f.readline()



data = []

for i in f.readlines():
    i = i.strip().split(';')
    data.append([i[0], int(i[1]), int(i[2])])

data = sorted(data, key = lambda x: (x[1], x[2]), reverse=True)



res = open('results.results.csv', 'w')
res.write('Спортсмен;Место\n')
mesto = 1

for i in data:
    res.write(i[0] + ';' + str(mesto) + '\n')
    mesto += 1
