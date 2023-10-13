# 주어진 금액을 만드는 모든 방법 출력
T = int(input())
coin = []

for i in range(T):
    N = int(input())
    coin = list(map(int,input().split()))
    price = int(input())
    
    dp = [0] * (price+1)
    dp[0] = 1
    
    for i in coin:
        for j in range(i,price+1):
            dp[j] += dp[j-i]
    
    print(dp[-1])