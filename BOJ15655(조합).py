# N과 M (6)
# 조합 문제
N,M = map(int,input().split())
nums = list(map(int,input().split()))
nums.sort()
answer = []

def back(cnt,start):
    if len(answer) == cnt: # answer의 길이가 M개를 고른 수열일 때 출력
        print(' '.join(map(str,answer)))
        return
    
    for i in range(start,len(nums)): # 이전의 값의 중복을 방지하기 위해 start 인덱스 부터 반복
        answer.append(nums[i])
        back(cnt,i+1)
        answer.pop()

back(M,0)