n = int(input())
cnt = 0
while n > 0:
    if n % 5 == 0:
        cnt += n // 5
        n = n % 5
        break
    else:
        cnt += 1
        n = n - 2

if n == 0:
    print(cnt)
else:
    print(-1)
