# N개의 카드를 구매하기 위해 지불해야 하는 금액의 최대값
N = int(input())
card = list(map(int,input().split()))
card.insert(0,0)
dp = [0] * (N+1)

if N == 1:
    print(card[1])
    exit()
if N == 2:
    print(max(card[1]*2, card[2]))
    exit()
    
dp[1] = card[1]
dp[2] = max(card[1]*2,card[2])

if N == 3:
    print(max(card[1]*3, card[3], dp[1]+dp[2]))
    exit()
    
dp[3] = max(dp[1]*3,card[3],dp[1]+dp[2])
dp[4] = max(dp[1]*4,card[4],dp[2]+dp[2],dp[1]+dp[3])

for i in range(5,N+1):
    dp[i] = max(dp[i-1]+dp[1],dp[i-2]+dp[2],dp[i-3]+dp[3],dp[i-4]+dp[4],card[i])

print(dp[N])


# 이게답임.. 뭐가다른데 ㅆㅂ
# import sys
# input = sys.stdin.readline

# n = int(input())
# p = [0] + list(map(int, input().split()))
# dp = [0] * (n + 1) i까지의 아이템을 고려했을 때 얻을 수 있는 최대보상

# for i in range(1, n + 1) :
# 	for j in range(1, i + 1) :
# 		dp[i] = max(dp[i], dp[i-j] + p[j]) 현재까지의 최대 보상, i까지 j번째 아이템을 포함시켰을때 보상

# print(dp[n])