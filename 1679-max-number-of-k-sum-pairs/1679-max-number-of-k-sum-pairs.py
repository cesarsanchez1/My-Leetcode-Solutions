class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        counter = 0
        freq = {}
        for item in nums:
            diff = k-item
            if diff in freq and freq[diff] > 0:
                counter += 1
                freq[diff] -= 1
            else:
                freq[item] = freq.get(item,0) +1
        return counter