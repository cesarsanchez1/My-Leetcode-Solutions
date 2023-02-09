class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        unique = list(set(nums))

        freq = {}

        for item in nums:
            if item in freq:
                freq[item] += 1
            else:
                freq[item] = 1

        for item in unique:
            occurrences = freq[item]
            if occurrences%2!=0:
                return False
        return True


