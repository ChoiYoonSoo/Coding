N = int(input())
answer = []


def back(cnt):
    if cnt == len(answer):
        print(" ".join(map(str, answer)))
        return

    for i in range(1, N+1):
        if i not in answer:
            answer.append(i)
            back(cnt)
            answer.pop()


back(N)
