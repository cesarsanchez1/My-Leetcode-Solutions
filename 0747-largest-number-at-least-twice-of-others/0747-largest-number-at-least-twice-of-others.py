class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        largest = max(nums)
        index = 0
        for i in range(len(nums)):
            if nums[i]!=largest:
                curr = nums[i]*2
                if curr > largest:
                    return -1
            else:
                index = i
        return index
            
        