class Solution:
    def findGCD(self, nums: List[int]) -> int:
        maxNum = max(nums)
        minNum = min(nums)

        for i in range(minNum, 0, -1):
            if maxNum%i==0 and minNum%i==0:
                return i
        return 0