class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        myMin = min(nums)
        myMax = max(nums)

        for item in nums:
            if item != myMin and item!=myMax:
                return item
        return -1