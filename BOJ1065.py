X = input()
if len(X) <= 2:
    print(int(X))
else:
    count = 99
    for i in range(100, int(X)+1):
        diff = int(str(i)[1]) - int(str(i)[0])
        x = 0
        for j in range(1, len(str(i))-1):
            if int(str(i)[j]) + diff != int(str(i)[j+1]):
                x += 1
        if x == 0:
            count += 1
    print(count)
