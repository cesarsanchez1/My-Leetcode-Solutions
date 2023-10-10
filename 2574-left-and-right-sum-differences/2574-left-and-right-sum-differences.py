class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        left = [0]
        leftSum = 0
        
        for i in range(len(nums)-1):
            leftSum += nums[i]
            left.append(leftSum)
            
        nums = nums[::-1]
        
        right = [0]
        rightSum = 0
        
        for i in range(len(nums)-1):
            rightSum += nums[i]
            right.append(rightSum)
        
        right = right[::-1]
        res = []
        
        for i in range(len(nums)):
            res.append(abs(left[i]-right[i]))
        return res
            
        
        
        