class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        freq = {}
        
        for item in nums:
            freq[item] = freq.get(item, 0) + 1
            if freq[item] > 1:
                return True
            
        return False