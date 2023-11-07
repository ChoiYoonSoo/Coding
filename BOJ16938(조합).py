N,L,R,X = map(int,input().split())
A = list(map(int,input().split()))
answer = []
global count
count = 0

def back(start,cnt):
    global count
    
    if len(answer) == cnt:
        if sum(answer) >= L and sum(answer) <= R and (max(answer)-min(answer)) >= X:
            count += 1
            return
    
    for i in range(start,N):
        answer.append(A[i])
        back(i+1,cnt)
        answer.pop()

for i in range(2,N+1):
    back(0,i)
    
print(count)