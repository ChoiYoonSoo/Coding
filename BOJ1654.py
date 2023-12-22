# 랜선 자르기
import sys
input = sys.stdin.readline

K, N = map(int, input().split())
lan = []
for i in range(K):
    lan.append(int(input()))

lan.sort()
start = 1
end = lan[-1]

while start <= end:
    total = 0
    mid = (start+end) // 2
    for i in range(len(lan)):
        total += lan[i] // mid
    if total < N:
        end = mid - 1
    elif total >= N:
        start = mid + 1

print(end)
