def getOct(num):
    string = oct(num)[2:]
    return string[-1] == '3'

def getThree(num):
    string = ""
    while num > 0:
        string = str(num % 3) + string
        num = num // 3
    return string[-1] == '0'

sum_num = 0
min_num = 0
sums = []
for i in range(1024, 616521 + 1):
    if getOct(i) and getThree(i):
        # sum_num += i
        # if min_num == 0:
        #     min_num = i
        sums.append(i)
print(sum(sums), min(sums))
print(sums)