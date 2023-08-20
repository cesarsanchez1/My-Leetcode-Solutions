class Solution:
    def pivotInteger(self, n: int) -> int:
        left = 0
        right = 0

        freq1 = {}
        freq2 = {}

        for i in range(1, n+1):
            left += i
            freq1[i] = left
        
        for i in range(n, 0, -1):
            right += i
            freq2[i] = right
        
        for i in range(1, n+1):
            if freq1[i] == freq2[i]:
                return i

        return -1  