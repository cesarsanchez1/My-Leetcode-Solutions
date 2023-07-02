class Solution:
    def balancedStringSplit(self, s: str) -> int:
        count = 0
        balancedCount = 0

        for i in range(len(s)):
            if s[i] == 'L':
                count += 1
            else:
                count -= 1
            if count == 0:
                balancedCount += 1
        return balancedCount
        