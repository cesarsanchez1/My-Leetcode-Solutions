class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        freq = {}
        
        for i, item in enumerate(nums):
            complement = target-item
            
            if complement in freq:
                return [freq[complement], i]
            freq[item] = i
        return -1