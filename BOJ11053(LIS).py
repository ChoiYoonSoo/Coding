# 가장 긴 증가하는 부분 수열 길이

n = int(input())
lst = list(map(int,input().split()))
dp = [0] * (n+1)
dp[0] = 1

for i in range(1,n):
    dp[i] = 1
    for j in range(i):
        if lst[i] > lst[j]:
            dp[i] = max(dp[i],dp[j]+1)

print(max(dp))