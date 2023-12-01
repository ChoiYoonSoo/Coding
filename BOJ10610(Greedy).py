# 30의 배수
# 숫자에 0이 포함되어 있어야하고 숫자들의 합의 3의 배수여야함.
N = input()
N = sorted(N,reverse=True)
total = 0

if '0' not in N:
    print("-1")

else:
    for i in N:
        total += int(i)
    if total % 3 != 0:
        print("-1")
    else:
        print(''.join(N))