N = int(input())
count = 0

while N >= 0:
    if N % 5 == 0:
        count += N // 5
        print(count)
        break
    N -= 3
    count += 1
else:
    print(-1)

# N = int(input())
# count = 0

# while(True):
#     if N == 0:
#         print(count)
#         break
#     if N % 5 == 0:
#         count += 1
#         N -= 5
        
#     elif N % 3 == 0:
#         count += 1
#         N -= 3
#     elif N > 5:
#         count += 1
#         N -= 5
#     else:
#         print(-1)
#         break