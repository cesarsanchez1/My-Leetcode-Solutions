class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        cur = 0
        res = 0
        for i in range(len(gain)):
            cur+=gain[i]
            res = max(cur, res)
        return res
            
        