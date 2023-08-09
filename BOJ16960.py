def isPossible(index):
    flag = True
    for value in switch[index]:
        cnt[value] -= 1
        if cnt[value] <= 0:
            flag = False

    for value in switch[index]:
        cnt[value] += 1
    return flag

            
N,M = map(int,input().split())
switch = [[] for _ in range(N + 1)]
numSet = [0] * (M + 1)
cnt = [0] * (M + 1)

for i in range(N):
    switch[i] = list(map(int,input().split()[1:]))
    for value in switch[i]:
        cnt[value] += 1

for i in range(N):
    if isPossible(i):
        print("1")
        exit()
        
print("0")