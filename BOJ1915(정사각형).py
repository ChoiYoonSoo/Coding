# 가장 큰 정사각형 크기 구하기 DP
n,m = map(int,input().split())
arr = [[0] * (m+1) for _ in range(n+1)]
dp = [[0] * (m+1) for _ in range(n+1)]

for i in range(1,n+1):
    arr[i][1:] = list(map(int,input()))
    
x = 0
for i in range(1,n+1):
    for j in range(1,m+1):
        if arr[i][j] != 0:
            dp[i][j] = min(dp[i-1][j],dp[i-1][j-1],dp[i][j-1]) + 1
            if x < dp[i][j]:
                x = dp[i][j]

print(x*x)