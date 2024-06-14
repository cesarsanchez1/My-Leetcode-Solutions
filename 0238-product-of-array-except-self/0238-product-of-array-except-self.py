class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        size = len(nums)
        
        arr1 = [1]*size
        arr2 = [1]*size
        
        for i in range(1,size):
            arr1[i] = arr1[i-1]*nums[i-1]
        
        revNums = nums[::-1]
        
        for i in range(1,size):
            arr2[i] = arr2[i-1]*revNums[i-1]
            
        arr2 = arr2[::-1]
    
        for i in range(size):
            arr1[i] = arr1[i]*arr2[i]
            
        return arr1
        
        
        
        
        