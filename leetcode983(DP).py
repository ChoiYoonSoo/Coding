# 여행에 필요한 최소 금액 반환
class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        dp = [0 for _ in range(days[-1]+1)]
        x = 0

        for i in range(1,len(dp)):
            if i != days[x]:
                dp[i] = dp[i-1]
            else:
                x += 1
                dp[i] = min(dp[max(0,i-1)] + costs[0],dp[max(0,i-7)] + costs[1],dp[max(0,i-30)] + costs[2])

        return dp[-1]
