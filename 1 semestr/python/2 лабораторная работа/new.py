import csv


f = open('players.csv', newline="")
f.readline()
reader = csv.reader(f, delimiter=';')


data = []  # список из кортежей вида (имя, кол-во побед, доп. показатель)

for i in reader:
    data.append([i[0], int(i[1]), int(i[2])])

data = sorted(data, key = lambda x: (x[1], x[2]), reverse=True)




res = open('results.csv', 'w', newline='')
writer = csv.writer(res, delimiter=';')
writer.writerow(['Спортсмен', 'Место'])


mesto = 0
prev = (-1, -1)  # победы и доп. баллы предыдущего участника
for i in data:
    if prev != (i[1], i[2]):
        mesto += 1
    writer.writerow([i[0], str(mesto)])

    prev = (i[1], i[2])
