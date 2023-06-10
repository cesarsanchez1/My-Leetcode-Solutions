class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        product = 1
        n = len(nums)
        left = 0
        right = 0
        counter = 0
        
        for right in range(len(nums)):
            product*=nums[right]
            while product >= k and left <= right:
                product = product/nums[left]
                left+=1
            counter += (right-left+1)
        return counter