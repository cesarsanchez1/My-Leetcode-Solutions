class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        
        smallest = float('inf')
        secondSmallest = float('inf')
        
        for num in nums:
            if num <= smallest:
                smallest = num
            elif num <= secondSmallest:
                secondSmallest = num
            else:
                return True
        return False
                