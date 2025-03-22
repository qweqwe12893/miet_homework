s, x = input().split()
buffer = ''
step = len(x)

while x.lower() in s.lower():
    i = 0
    while i < len(s):
        block = s[i:i+step]
        if block.lower() != x.lower():
            buffer += s[i]
        else:
            i += step-1
        i += 1
    s = buffer
    buffer = ''

print(s)
