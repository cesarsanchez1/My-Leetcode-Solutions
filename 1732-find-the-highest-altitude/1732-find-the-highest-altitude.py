class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        
        runSum = 0
        res = 0
        
        for item in gain:
            runSum += item
            res = max(res, runSum)
        return res
                