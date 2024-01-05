N = int(input())
people = []
answer = []
for i in range(N):
    people.append(list(map(int, input().split())))

for i in range(N):
    equals = 1
    for j in range(N):
        if people[i][0] < people[j][0] and people[i][1] < people[j][1]:
            equals += 1
    answer.append(equals)

print(*answer)
