T = int(input())
for i in range(T):
    k = int(input())
    n = int(input())
    answer = [[1] for i in range(k+1)]

    for j in range(2, n+1):
        answer[0].append(j)

    for a in range(1, k+1):
        for b in range(1, n):
            answer[a].append(answer[a-1][b] + answer[a][b-1])
    print(answer[k][n-1])
