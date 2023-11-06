# N과 M (8)
# 중복 조합 문제
N,M = map(int,input().split())
nums = list(map(int,input().split()))
nums.sort()
answer = []

def back(cnt,start):
    if len(answer) == cnt: # answer의 길이가 M개를 고른 수열일 때 출력
        print(' '.join(map(str,answer)))
        return
    
    for i in range(start,len(nums)): # 조합 문제와 달리 중복을 허용하기 때문에 저장 여부를 묻지 않음
        answer.append(nums[i])
        back(cnt,i) # 중복 허용이기 때문에 i값을 그대로 가져감
        answer.pop()
        
back(M,0)