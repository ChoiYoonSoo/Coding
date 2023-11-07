import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(x):
    global cnt
    visited[x] = True
    nx = s[x]
    team.append(x) # 사이클이 있는 팀원을 추가
    
    if visited[nx] == True:
        if nx in team:
            cnt -= len(team[team.index(nx):]) # 현재 구성된 팀원 수 만큼 빼줌
    else:
        dfs(nx)
            

T = int(input())
for i in range(T):
    n = int(input())
    s = list(map(int,input().split()))
    s.insert(0,0)
    visited = [False] * (n+1)
    cnt = n
    
    for j in range(1,n+1):
        if visited[j] == False:
            team = []
            dfs(j)
            
    print(cnt)