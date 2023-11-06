# N과 M (9)
# 순열 + 중복된 nums값의 처리
N,M = map(int,input().split())
nums = list(map(int,input().split()))
nums.sort()
answer = []
lst = set() # nums 배열이 중복된 값도 있기 때문에 set형으로 중복 방지
check = [] # 현재 값을 또 저장하면 안되기 때문에 저장 여부 check

def back(cnt):
    if len(answer) == cnt:
        if str(answer) not in lst: # 이미 lst에 존재하는 answer 인가
            lst.add(str(answer))
            print(' '.join(map(str,answer)))
        return
    
    for i in range(len(nums)):
        if i not in check: # 현재 nums의 값이 다시 사용되면 안되기 때문에 저장 여부 확인
            check.append(i)
            answer.append(nums[i])
            back(cnt)
            answer.pop()
            check.pop()
        
back(M)