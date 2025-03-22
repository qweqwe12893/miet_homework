def reducer(num: tuple) -> tuple:
    m, n = num

    if m >= n:
        print("Числитель должен быть меньше знаменателя")
        return (0, 0)

    elif m <= 0 or n <= 0:
        print("Числитель и знаменатель должны быть положительными числами")
        return (0, 0)
    
    elif type(m) != int or type(n) != int:
        print("Числитель и знаменатель должны быть целыми числами")
        return (0, 0)

    for i in range(2, n//2+1):
        while m%i == 0 and n % i == 0:
            m = m // i
            n = n // i
    
    return (m, n)

print(reducer((6, 20)))