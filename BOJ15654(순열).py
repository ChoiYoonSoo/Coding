# N과 M (5)
# 순열 문제
N,M = map(int,input().split())
nums = list(map(int,input().split()))
nums.sort() # 사전 순으로 증가하는 순서로 출력하기 위한 정렬
answer = []

def back(cnt):
    if len(answer) == cnt: # answer의 길이가 M개를 고른 수열일 때 출력
        print(' '.join(map(str,answer)))
        return
    
    for i in nums: 
        if i not in answer: # nums의 값이 answer에 저장하지 않은 것만
            answer.append(i)
            back(cnt)
            answer.pop()
            
back(M)