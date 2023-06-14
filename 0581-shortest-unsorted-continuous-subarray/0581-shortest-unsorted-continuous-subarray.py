class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        copy = nums[:]
        copy.sort()

        if copy == nums:
            return 0
        
        for i in range(len(nums)):
            copy[i] = nums[i]-copy[i]
        
        left = 0
        
        for i in range(len(copy)):
            if copy[i] == 0:
                left+=1
            else:
                break
        
        right = len(copy)-1
                
        for i in range(len(copy)-1,-1,-1):
            if copy[i] == 0:
                right-=1
            else:
                break
        
        return right-left+1

    
                