# 파스칼 트라이앵글 DP
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        dp = [[1] for _ in range(numRows)]
        
        for i in range (numRows):
            for j in range(1,i+1):
                if j == i:
                    dp[i].append(1)
                else:
                    dp[i].append(dp[i-1][j-1] + dp[i-1][j])
        
        return dp