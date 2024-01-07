class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        nums.sort()
        res = []
        
        for i in range(len(nums)):
            if i%2 != 0:
                res.append(nums[i])
                res.append(nums[i-1])
                
        return res
            