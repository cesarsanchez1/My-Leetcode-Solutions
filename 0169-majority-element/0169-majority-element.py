class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        freq = {}
        
        for item in nums:
            freq[item] = freq.get(item, 0) + 1
            if freq[item] > (len(nums)/2):
                return item
        return 0