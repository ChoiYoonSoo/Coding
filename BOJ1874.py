cnt = 1
check = True
stack = []
answer = []

N = int(input())
for i in range(N):
    n = int(input())

    while cnt <= n:
        stack.append(cnt)
        answer.append('+')
        cnt += 1

    if stack[-1] == n:
        stack.pop()
        answer.append('-')
    else:
        check = False
        break


if check == False:
    print("NO")
else:
    for i in answer:
        print(i)
