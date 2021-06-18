def f(n):
    if n <= 3:
        return 2*n + 3
    elif n > 3:
        return f(n-1) + 5*f(n-2)
print(f(10))