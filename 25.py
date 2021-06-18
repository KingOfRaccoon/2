def check(num):
    summary = sum([int(x) for x in str(num)])
    return num % summary == 0

sums = []
for i in range(1024, 28921 + 1):
    if check(i):
        sums.append(i)
print(sum(sums))
print(len(sums))