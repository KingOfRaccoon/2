with open("27-B.txt") as file:
    data = file.readlines()
    size = int(data.pop(0))
    summary = 0
    temps = []
    for i in data:
        temp = [int(x) for x in i.split()]
        summary += max(temp)
        temps.append(temp)
    print(summary)
    if summary % 2 != 0:
        temps.sort(key=lambda x: abs(x[0] - x[1]))
        dif = 0
        for i in temps:
            if abs(i[0] - i[1]) % 2 != 0:
                print(i, abs(i[0] - i[1]))
                dif = abs(i[0] - i[1])
            if dif != 0:
                break
        print(summary - dif)
