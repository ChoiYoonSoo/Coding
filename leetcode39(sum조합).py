class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        answer = []
        lst = []

        def back(start):
            if sum(lst) > target:
                return

            if sum(lst) == target:
                answer.append(lst.copy())
                return
            
            for i in range(start,len(candidates)):
                lst.append(candidates[i])
                back(i)
                lst.pop()

        back(0)
        
        return answer