class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True

        isInc = False
        isDec = False
        
        for i in range(len(nums)-1):
            if nums[i] <= nums[i+1]:
                isInc = True
            else:
                isInc = False
                break
        
        for i in range(len(nums)-1):
            if nums[i] >= nums[i+1]:
                isDec = True
            else:
                isDec = False
                break
        
        if isInc == True or isDec == True:
            return True
        return False
            
                
            
                