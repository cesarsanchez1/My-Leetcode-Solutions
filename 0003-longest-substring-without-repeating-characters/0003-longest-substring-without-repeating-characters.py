class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        head = 0
        res = 0
        for i in range(len(s)):
            while s[i] in charSet:
                charSet.remove(s[head])
                head += 1
            charSet.add(s[i])
            res = max(res, i+1-head)
        return res