# 문자열 최소횟수로 뒤집어서 같은 문자로 만들기
S = input()
Z = []
O = []
cntZ = 1
cntO = 1

for i in range(len(S)):
    if S[i] == '0':
        Z.append(i)
    else:
        O.append(i)

for i in range(len(Z)-1):
    if Z[i+1]-Z[i] != 1:
        cntZ += 1

for i in range(len(O)-1):
    if O[i+1]-O[i] != 1:
        cntO += 1
if len(Z) < 1 or len(O) < 1:
    print("0")
elif len(Z) == 1 or len(O) == 1:
    print("1")
else:
    print(min(cntZ,cntO))