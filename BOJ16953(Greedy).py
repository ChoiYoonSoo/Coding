A,B = map(int,input().split())
x = str(B)
cnt = 1

while(True):
    if B < A:
        print("-1")
        break
    if B == A:
        print(cnt)
        break
    if B % 2 != 0 and x[-1] == "1":
        x = x[:-1]
        B = int(x)
    elif B % 2 == 0:
        B = B // 2
        x = str(B)
    else:
        print("-1")
        break
    cnt += 1