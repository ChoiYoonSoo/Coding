N,M = map(int,input().split()) # 사람의 수, 파티의 수 입력
number = set(map(int,input().split()[1:])) # 진실을 아는 사람 번호
party = [] # 각 파티의 집합
cnt = 0

for i in range(M): # 각 파티에 참가하는 사람의 집합
    party.append(set(map(int,input().split()[1:])))

for i in range(M): # 파티의 수 만큼 반복
    for x in party: # 각 파티의 참가하는 사람 중 진실을 아는 사람이 포함되어 있는지 비교
        if x.isdisjoint(number) == False:
            number = number.union(x)

for i in range(M): # 각 파티의 참가하는 사람 중 진실을 아는 사람이 없는 경우 cnt 증가
    if party[i].isdisjoint(number) == True:
        cnt += 1

print(cnt)