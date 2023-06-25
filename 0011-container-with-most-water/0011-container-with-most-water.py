class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        left = 0
        right = len(height)-1
        
        totalWater = 0
        
        area = 0
        
        
        while left < right:
            smallest = min(height[left], height[right])
    
            area = max(area, smallest*(right-left))
            
            if height[left] >= height[right]:
                right-=1
            else:
                left+=1
            
        return area
            
        