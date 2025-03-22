def intersection(*args: list) -> list:
    count = dict()

    for mnozestvo in args:
        for num in mnozestvo:
            count[num] = count.get(num, 0) + 1

    res = []
    for key, value in count.items():
        if value == len(args):
            res.append(key)

    return sorted(res)


print(intersection([3, 2, 1], [2, 3, 6], [2, 3, 4, 5]))
