class Solution:
    def trap(self, height: List[int]) -> int:
        
        # start by initializing two pointers at the beginning and end of the heights array    
        left = 0
        right = len(height)-1

        # initialize two variables leftMax and rightMax to store the highest 
        # height encountered as we traverse from L to R and R to L
        leftMax = 0
        rightMax = 0
        
        # initialize a variable total water 
        totalWater = 0
        
        while left <= right:
            if height[left] <= height[right]:
                if height[left] > leftMax:
                    leftMax =  height[left]
                else:
                    totalWater += leftMax - height[left]
                left += 1
            else:
                if height[right] > rightMax:
                    rightMax =  height[right]
                else:
                    totalWater += rightMax - height[right]
                right -= 1
        return totalWater
                
                
        
        
        