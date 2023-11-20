# 거스름돈
N = int(input())
nums = [500,100,50,10,5,1]
money = 1000 - N
count = 0
idx = 0
while money > 0:
    count += money // nums[idx]
    money = money % nums[idx]
    idx += 1

print(count)