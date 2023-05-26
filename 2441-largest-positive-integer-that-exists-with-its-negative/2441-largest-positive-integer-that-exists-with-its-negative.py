class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        mySet = set(nums)
        largest = 0
        for i in range(len(nums)):
            if (nums[i]>0) and (nums[i]*-1) in mySet and (nums[i]>largest):
                largest = nums[i]
        if largest == 0:
            return -1
        return largest

        