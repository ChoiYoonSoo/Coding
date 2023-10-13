# n가지의 동전을 사용해서 K원을 만드는 동전의 최소 개수
n,k = map(int,input().split())
coin = []
dp = [100001] * (k+1)

for i in range(n):
    coin.append(int(input()))

coin.sort()
dp[0] = 0

for i in coin:
    for j in range(i,k+1):
        dp[j] = min(dp[j],dp[j-i]+1) # 현재 코인 값에서 구할 코인 사용개수를 빼면 그 코인에서 현재 코인개수를 더하면 알 수 있기 때문에 +1까지 해줌

if dp[k] == 100001:
    print(-1)
else:
    print(dp[k])