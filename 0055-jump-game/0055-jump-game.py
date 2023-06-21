class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal = nums[len(nums)-1]
        
        for i in range(len(nums)-1, -1, -1):
            if goal <= nums[i]+i:
                goal = i
        if goal == 0:
            return True
        return False
                
        