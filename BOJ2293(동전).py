n,k = map(int,input().split())
prices = []

# 2차원으로 풀었는데 메모리 초과됨 1차원으로 해야댐
# dp = [[0] * (k+1) for _ in range(n+1)]
# for i in range(n):
#     prices.append(int(input()))

# for i in range(k+1):
#     dp[0][i] = 0
# for i in range(n+1):
#     dp[i][0] = 1

# for i in range(1,n+1):
#     for j in range(1,k+1):
#         if j < prices[i-1]:
#             dp[i][j] = dp[i-1][j]
#         else:
#             dp[i][j] = dp[i-1][j] + dp[i][j-prices[i-1]]
     
# print(dp[-1][-1])

# 1차원 코드
for i in range(n):
    prices.append(int(input()))
prices.sort()

DP = [0] * (k + 1)
DP[0] = 1
for c in prices:
    for i in range(c, k + 1):
        DP[i] += DP[i - c] # 현재 코인 사용개수에 코인값을 빼면 현재 코인사용개수를 하나 더했을 때의 값을 알 수 있음
print(DP[k])