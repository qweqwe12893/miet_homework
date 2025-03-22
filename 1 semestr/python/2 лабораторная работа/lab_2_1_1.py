from random import randint, shuffle
from ipaddress import ip_address


f = open('ip.log', 'w')

res = []
start = 0

for i in range(10_000):

    # 4294967295 - max ip adress value
    # 4294967295 // 10_000 == 429496
    address = randint(start, start + 429495)
    address = ip_address(address)

    res.append(str(address))
    start += 429496


shuffle(res)

for i in res:
    f.write(i + '\n')
