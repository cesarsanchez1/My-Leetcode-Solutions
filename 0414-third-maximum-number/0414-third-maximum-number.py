class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        unique = list(set(nums))
        unique.sort()
        print(unique)
        size = len(unique)-1
        if len(unique)<3:
            return max(unique)
        return unique[size-2]
        