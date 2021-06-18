with open("24.txt") as file:
    data = file.read()
    counter = 0
    print(len(data))
    for i in range(len(data)-3):
        if str(data[i]+data[i+1]+data[i+2]) == "XYZ" or str(data[i]+data[i+1]+data[i+2]) == "ZYX":
            counter += 1
    print(counter)