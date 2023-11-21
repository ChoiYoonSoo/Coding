S = int(input())
i = 1
total = 0
ans = 0

while total <= S:
    total += i
    i += 1
    ans += 1

print(ans-1)