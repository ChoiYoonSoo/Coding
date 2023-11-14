N, M = map(int, input().split())
cnt = []
board = []

for i in range(N):
    board.append(input())

for i in range(N-7):
    for j in range(M-7):
        white = 0
        black = 0
        for k in range(i, i+8):
            for l in range(j, j+8):
                if (k+l) % 2 == 0:
                    if board[k][l] != 'W':
                        white += 1
                    else:
                        black += 1
                else:
                    if board[k][l] != 'W':
                        black += 1
                    else:
                        white += 1

        cnt.append(white)
        cnt.append(black)

print(min(cnt))
