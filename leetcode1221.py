class Solution:
    def balancedStringSplit(self, s: str) -> int:
        balance = 0
        cnt = 0
        for i in range(len(s)):
            if s[i] == 'R':
                balance += 1
            elif s[i] == 'L':
                balance -= 1
            if balance == 0:
                cnt += 1
        return cnt