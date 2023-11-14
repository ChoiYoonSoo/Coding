from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
q = deque()

for i in range(N):
    line = list(input().split())
    if "push" in line[0]:
        q.append(line[1])
    elif line[0] == "front":
        if q:
            print(q[0])
        else:
            print("-1")
    elif line[0] == "back":
        if q:
            print(q[-1])
        else:
            print("-1")
    elif line[0] == "pop":
        if q:
            print(q.popleft())
        else:
            print("-1")
    elif line[0] == "size":
        print(len(q))
    elif line[0] == "empty":
        if q:
            print("0")
        else:
            print("1")
