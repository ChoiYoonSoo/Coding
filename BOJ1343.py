board = input()
count = 0
answer = []
for i in range(len(board)):
    if board[i] != '.':
        count += 1
    else:
        if count % 4 == 0:
            while count > 0:
                count -= 1
                answer.append('A')
        elif count % 2 == 0:
            while count > 0:
                if count > 2:
                    count -= 4
                    answer.append('AAAA')
                else:
                    count -= 2
                    answer.append('BB')
        else:
            print('-1')
            exit()
        answer.append('.')
if count != 0:
    if count % 4 == 0:
        while count > 0:
            count -= 1
            answer.append('A')
    elif count % 2 == 0:
        while count > 0:
            if count > 2:
                count -= 4
                answer.append('AAAA')
            else:
                count -= 2
                answer.append('BB')
    else:
        print('-1')
        exit()
print(''.join(answer))
