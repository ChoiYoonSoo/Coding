# 특정 거리의 도시 찾기 (BFS)
import sys
input = sys.stdin.readline
from collections import deque

def bfs(x,k): # BFS 탐색
    visited[x] = True # 시작 정점에 대해 설정
    distance[x] = 0
    q.append(x)
    
    # 일반적인 BFS와 같음, 방문 하지 않았을 경우 방문 처리 및 그 위치까지의 거리를 +1 해준뒤 목표 거리 K와 현재 위치가 같으면 배열에 추가하여 출력
    while(q): 
        a = q.popleft()
        for i in graph[a]:
            if visited[i] != True:
                q.append(i)
                visited[i] = True
                distance[i] = distance[a] + 1 # 이전 까지의 거리에 1추가
                
                if distance[i] == k:
                    answer.append(i)
                    
    if len(answer) == 0:
        print(-1)
    else:
        answer.sort()
        for i in answer:
            print(i,end='\n')     

N,M,K,X = map(int,input().split())
graph = [[] for _ in range(N+1)]
visited = [False] * (N+1) # 방문했는지 저장
distance = [0] * (N+1) # 시작 정점으로부터 해당 도시까지 거리 저장
answer = []
q = deque()

for i in range(M): # 방향 그래프 생성
    a,b, = map(int,input().split())
    graph[a].append(b)

bfs(X,K)