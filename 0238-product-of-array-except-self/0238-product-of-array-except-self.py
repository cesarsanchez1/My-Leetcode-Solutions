class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        leftSum = [1]*n
        rightSum = [1]*n
        res = [1]*n
        
        revNum = nums[::-1]
        for i in range(1, n):
            leftSum[i] = leftSum[i-1]*nums[i-1]
        for i in range(1, n):
            rightSum[i] = rightSum[i-1]*revNum[i-1]
        
        rightSum = rightSum[::-1]
        
        for i in range(n):
            res[i] = rightSum[i]*leftSum[i]
        return res
        
        
        
            
            
        