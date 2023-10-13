# 거래에서 얻을 수 있는 최대 이익 구하기
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = [0] * (len(prices))

        if len(prices) <= 1:
            return 0

        if len(prices) == 2:
            if prices[1] < prices[0]:
                return 0
            else:
                return prices[1] - prices[0]

        dp[1] = prices[1] - prices[0]
        
        for i in range(2,len(prices)):
            dp[i] = max(prices[i]-prices[i-2],prices[i]-prices[i-1])
            prices[i-1] = min(prices[i-2],prices[i-1])
        
        dp.sort()
        if dp[-1] <= 0:
            return 0

        return dp[-1]