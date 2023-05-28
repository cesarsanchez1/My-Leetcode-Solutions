class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        count = 0
        num_freq = {}

        for num in nums:
            if k - num in num_freq and num_freq[k - num] > 0:
                count += 1
                num_freq[k - num] -= 1
            else:
                num_freq[num] = num_freq.get(num, 0) + 1

        return count