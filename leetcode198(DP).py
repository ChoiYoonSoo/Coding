# 강탈할수 있는 최대 금액
class Solution:
    def rob(self, nums: List[int]) -> int:

        if len(nums) <= 1:
            return nums[0]

        dp = nums
        dp[1] = max(nums[0],nums[1])

        for i in range(2,len(dp)):
            dp[i] = max(dp[i-1],dp[i-2]+nums[i])

        return dp[-1]