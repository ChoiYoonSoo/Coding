def dfs(remove):
    tree[remove] = -2
    for i in range(N):
        if tree[i] == remove:
            dfs(i)

N = int(input())
tree = list(map(int,input().split()))
remove = int(input())

dfs(remove)
leaf = 0

for i in range(N):
    if tree[i] != -2 and i not in tree:
        leaf += 1

print(leaf)