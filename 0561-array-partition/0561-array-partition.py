class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        size = len(nums)
        n = int(size/2) 
        res = 0

        for i in range(n):
            res+=nums[i*2]
        return res
        

        
        