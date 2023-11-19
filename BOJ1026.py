#보물
N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
S = 0
A.sort()
idx = 0
while(B):
    S += A[idx] * max(B)
    B.remove(max(B))
    idx += 1

print(S)