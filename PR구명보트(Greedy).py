# 정답 코드
def solution(people, limit):
    answer = 0
    people.sort()
    front = 0
    end = len(people)-1
    
    while front <= end:
        if people[front] + people[end] <= limit:
            front += 1
            end -= 1
            answer += 1
            
        elif people[front] + people[end] > limit:
            end -= 1
            answer += 1
    
    return answer


# 시간초과 코드
# def solution(people, limit):
#     answer = 0
#     people.sort()
    
#     while people:
#         if len(people) == 1:
#             answer += 1
#             break
            
#         x = people.pop()
        
#         for i in range(len(people)):
#             if x + people[i] <= limit:
#                 del people[i]
#                 break
        
#         answer += 1
    
#     return answer