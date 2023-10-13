# 1,2를 사용하여 n을 만들수 있는 경우의수
class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0] * (n+1)
        if n == 1:
            return 1
        if n == 2:
            return 2
        dp[1] = 1
        dp[2] = 2
        
        for i in range(3,n+1):
            dp[i] = dp[i-1] + dp[i-2]
        
        return dp[n]