n = int(input())
tickets = dict()

for i in range(n):
    i = list(map(int, input().split()))
    tickets[(i[0], i[1])] = tickets.get((i[0], i[1]), []) + [i[2]]

for key, value in tickets.items():
    print(*key, '-', len(set(value)))
