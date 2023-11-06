# N과 M (7)
# 중복 순열 문제
N,M = map(int,input().split())
nums = list(map(int,input().split()))
nums.sort()
answer = []

def back(cnt):
    if len(answer) == cnt: # answer의 길이가 M개를 고른 수열일 때 출력
        print(' '.join(map(str,answer)))
        return
    
    for i in nums: # 순열 문제와 달리 중복을 허용하기 때문에 저장 여부를 묻지 않음
        answer.append(i)
        back(cnt)
        answer.pop()

back(M)