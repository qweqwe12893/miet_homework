from datetime import date


today = date.today()
chet  = date(2000, 9, 1)


def nearest_date(*args: date) -> date:

    args = list(args)
    for i in range(len(args)):
        buffer = []
        for dt in args[i].split('.'):
            buffer.append(int(dt))
        args[i] = date(*reversed(buffer))
        buffer = []


    mindelta = abs(today - args[0])
    flag = args[0] > today

    for i in args[1:]:
        if abs(i - today) < mindelta:
            mindelta = abs(i - today)
            flag = i > today
        elif (abs(i - today) == mindelta) and flag:
            flag = False

    mindelta = mindelta if flag else -1 * mindelta
    res = today + mindelta 

    return f"{str(res.day).zfill(2)}.{str(res.month).zfill(2)}.{res.year}"


print(nearest_date("01.01.2050", "12.04.2011", "31.12.1970"))

