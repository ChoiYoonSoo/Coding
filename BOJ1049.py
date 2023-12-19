N, M = map(int, input().split())
price = []
for i in range(M):
    a, b = map(int, input().split())
    price.append([a, b])

if N <= 6:
    MinPack = MinNode = 1001
    for i in range(M):
        if price[i][0] < MinPack:
            MinPack = price[i][0]
        if price[i][1] < MinNode:
            MinNode = price[i][1]

    if MinNode * N > MinPack:
        print(MinPack)
    else:
        print(MinNode * N)

else:
    MinPack = MinNode = 1001
    total = 0

    for i in range(M):
        if price[i][0] < MinPack:
            MinPack = price[i][0]
        if price[i][1] < MinNode:
            MinNode = price[i][1]

    while N > 0:
        if MinNode * 6 < MinPack:
            if N >= 6:
                N -= 6
                total += MinNode * 6
            else:
                N -= 1
                total += MinNode
        else:
            if N >= 6:
                N -= 6
                total += MinPack
            else:
                if MinNode * N < MinPack:
                    total = total + (MinNode * N)
                    N = 0
                else:
                    N = 0
                    total += MinPack

    print(total)
