N = int(input())
rope = []
w = 0
k = 1

for i in range(N):
    rope.append(int(input()))

rope.sort(reverse=True)
w = rope[0]

for i in range(1,len(rope)):
    result = rope[i] * (k+1)
    if w < result:
        w = result
    k+=1

print(w)