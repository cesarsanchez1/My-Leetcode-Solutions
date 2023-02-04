class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        check = len(nums)/3
        freq = {}
        res = []
        bank = list(set(nums))
        
        for item in nums:
            if item in freq:
                freq[item] += 1
            else:
                freq[item] = 1
        
        for item in bank:
            if freq[item]>check:
                res.append(item)
        return res
        
        