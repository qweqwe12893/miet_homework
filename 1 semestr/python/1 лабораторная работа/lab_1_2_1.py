array = input()[1:-1]
array = [list(map(int, array.split(',')))]
k = 0


def decrement(arr):
    for j in range(len(arr)):
        arr[j] -= 1
    return arr


#  transforms [2, 0, 2] into [ [2], [2] ]
def one_into_few(arr):
    newArray = [[]]
    for i in arr:
        if i == 0 and newArray[-1] != []:
            newArray.append([])
        elif i != 0:
            newArray[-1].append(i)
    return newArray if newArray[-1] != [] else newArray[:-1]


while array:

    newArray = []
    for i in array:
        while not 0 in i:
            i = decrement(i)
            k += 1
        i = one_into_few(i)
        for subarray in i:
            newArray.append(subarray)

    array = newArray

print(k)
