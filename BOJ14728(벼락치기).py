n,t = map(int,input().split())
test = [[0,0]]
dp = [[0] * (t+1) for _ in range(n+1)]

for i in range(n):
    test.append(list(map(int,input().split())))

for i in range(1,n+1):
    for j in range(1,t+1):
        k = test[i][0]
        s = test[i][1]
        
        if j < k:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j],dp[i-1][j-k]+s)

print(dp[n][t])