import sys
sys.setrecursionlimit(10 ** 6)

def dfs_recursive(room, start,visited, money):
    visited.append(start)
    
    if room[start][0] == 'L':
        if room[start][1] > money:
            money = room[start][1]

    elif room[start][0] == 'T':
        if room[start][1] > money:
            visited.pop()
            return
        else:
            money -= room[start][1]
            
    for i in range(0, len(room[start][2])):
        if room[start][2][i] != 0 and room[start][2][i] not in visited:
            dfs_recursive(room,room[start][2][i],visited,money)

while(True):
    n = int(input())
    if n == 0:
        break
    
    room = dict()
    money = 0
    visited = []

    for i in range(n):
        miro = input().split()
        room[i+1] = [miro[0], int(miro[1]), [int(x) for x in " ".join(miro[2:-1]).split(" ")]]
   
    dfs_recursive(room,1,visited,money)
    
    if n in visited:
        print("Yes")
    else:
        print("No")
    
    