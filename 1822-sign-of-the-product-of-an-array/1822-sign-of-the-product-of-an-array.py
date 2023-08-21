class Solution:
    def arraySign(self, nums: List[int]) -> int:
        prod = 1
        
        for item in nums:
            prod*=item
        
        if prod == 0:
            return 0
        elif prod < 0:
            return -1
        else:
            return 1
            
        