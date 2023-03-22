class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        size = len(arr)
        count = 1
        tot = 0

        while count <= len(arr):
            for i in range(size):
                tot += sum(arr[i:i+count])
            count += 2
            size -= 2

        return tot