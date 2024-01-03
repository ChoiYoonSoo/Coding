T = int(input())
for i in range(T):
    queue = []
    cnt = 0
    N, M = map(int, input().split())
    queue = list(map(int, input().split()))

    while True:
        if queue[0] == max(queue):
            queue.pop(0)
            cnt += 1
            if M == 0:
                break
            else:
                M -= 1
        else:
            if M == 0:
                M = len(queue)-1
            else:
                M -= 1
            queue.append(queue[0])
            queue.pop(0)

    print(cnt)
