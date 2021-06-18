for s in range(1, 10001):
    cope = s
    n = 0
    while s - n > 0:
        s = s - 10
        n = n + 15
    if n == 165:
        print(cope)