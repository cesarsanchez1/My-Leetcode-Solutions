class Solution:
    def maxPower(self, s: str) -> int:
        if len(s) == 1:
            return 1
        counter = 1
        res = 0

        for i in range(1, len(s)):
            if s[i] == s[i-1]:
                counter += 1
            if s[i] != s[i-1]:
                counter = 1
            res = max(counter, res)

        return res



