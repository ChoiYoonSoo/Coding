N,K = map(int, input().split())
number = [[0 for i in range(201)] for _ in range(201)]

for i in range(201):
    number[1][i] = 1
    number[2][i] = i + 1
    
for i in range(3,201):
    for x in range(201):
        number[i][x] = number[i-1][x] + number[i][x-1]

print(number[K][N] % 1000000000)