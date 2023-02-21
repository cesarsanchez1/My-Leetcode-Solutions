class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()
        size = len(nums)
        prod1 = nums[size-1]*nums[size-2]*nums[size-3]
        prod2 = nums[0]*nums[1]*nums[2]
        prod3 = nums[0]*nums[1]*nums[size-1]
        return max(prod1, prod2, prod3)
        