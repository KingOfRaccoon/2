with open("26.txt") as file:
    data = [int(x) for x in file.read().split()]
    size = data.pop(0)
    print(data)
    print(len(data))
    data.sort()
    print(sum(data[:10]))
