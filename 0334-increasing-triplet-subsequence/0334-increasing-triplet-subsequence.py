class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        smallest = float('inf')    
        secondSmallest = float('inf')        
        for item in nums:
            if item <= smallest:
                smallest = item
            elif item <= secondSmallest:
                secondSmallest = item
            else:
                return True
        return False