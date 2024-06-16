class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        
        right = 0
        zeroCount = 0 
        left = 0
        res = 0
        
        while right < len(nums):
            if nums[right] == 0:
                zeroCount += 1
            
            while zeroCount > k:
                if nums[left] == 0:
                    zeroCount-=1
                left+=1
            res = max(res, right-left+1)
            right+=1
        
        return res
                
        
        