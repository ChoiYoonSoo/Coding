# 해당 문자열이 포함되어 있는지
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        m = len(t)
        n = len(s)
        num = [[0] * (101) for _ in range(10001)]

        for i in range(1,m+1):
            for j in range(1,n+1):
                if t[i-1] == s[j-1]:
                    num[i][j] = num[i-1][j-1] + 1
                else:
                    num[i][j] = max(num[i-1][j],num[i][j-1])
        
        if n == num[m][n]:
            return True
        else:
            return False