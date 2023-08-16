N = int(input())
dp = [0] * (N+1)
children = list(map(int,input().split()))
m = 0

for i in range(N):
    idx = children[i]
    dp[idx] = dp[idx-1]+1
    m = max(m, dp[idx-1]+1)

print(N-m)