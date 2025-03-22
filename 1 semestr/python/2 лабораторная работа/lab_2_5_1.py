from os import walk

pattern = input()
count = 0

for dir, folder, i in walk('example'):
    
    for j in i:
        if pattern in j:
            count += 1

print(count)
