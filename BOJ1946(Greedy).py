# 신입사원
import sys
input = sys.stdin.readline

T = int(input())

for i in range(T):
    total = 1

    N = int(input())
    S = [[] for _ in range(N)]
    
    for i in range(N):
        a,b = map(int,input().split())
        S[i] = [a,b]
    
    S.sort()
    Min = S[0][1]
    for i in range(1,N):
        if S[i][1] < Min:
            total += 1
            Min = S[i][1]
    print(total)