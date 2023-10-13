# 증가하는 부분 수열 중 가장 큰 합
N = int(input())
A = list(map(int,input().split()))
dp = [0] * (N+1)
dp[0] = A[0] 

if N == 1:
    print(A[0])
    exit()

for i in range(1,N):
    for j in range(i):
        if A[i] > A[j]:
            dp[i] = max(A[i]+dp[j],dp[i]) # 현재 값과 이전 dp에 저장되어있는 합의 값을 더한 값과 지금 현재 dp값을 비교
        else:
            dp[i] = max(dp[i],A[i]) # 나보다 더 큰 값을 만났을 때 현재 값과 이전 dp에 저장된 합을 비교
print(max(dp))