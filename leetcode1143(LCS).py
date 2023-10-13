# 두 문자열의 길이가 얼만큼 포함되어 있는지
# 최장 공통 부분 수열

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m = len(text1)
        n = len(text2)
        num = [[0] * (1001) for _ in range(1001)]

        for i in range(1,m+1):
            for j in range(1,n+1):
                if text1[i-1] == text2[j-1]:
                    num[i][j] = num[i-1][j-1] + 1
                else:
                    num[i][j] = max(num[i-1][j],num[i][j-1])
        
        return num[m][n]