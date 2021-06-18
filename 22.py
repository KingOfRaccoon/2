for x in range(1, 10001):
    cope = x
    a, b = 0, 0
    while x > 0:
        a = a + 1
        b = b + (x % 8)
        x = x // 8
    if a == 3 and b == 12:
        print(cope)