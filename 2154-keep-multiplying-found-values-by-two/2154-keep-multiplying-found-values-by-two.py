class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        unique = set(nums)
        largest = max(nums)
        if original not in unique:
            return original
        while original<=largest:
            if original in unique:
                original*=2
            else:
                break
        return original
        