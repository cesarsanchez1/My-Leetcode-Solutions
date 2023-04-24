class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        freq = {}
        for item in nums:
            if item in freq:
                freq[item] += 1
            else:
                freq[item] = 1
            if freq[item] > 1:
                return item