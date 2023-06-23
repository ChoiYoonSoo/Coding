n = int(input())
i = 1
number = str(n)
sum = 0

while(i<n):
    for value in range(len(str(i))):
        print(str(i)[value])
        sum += int(str(i)[value])
    total = i + sum
    if total == n:
        print(i)
        exit(1)
    i += 1
    total = 0
    sum = 0
print("0")