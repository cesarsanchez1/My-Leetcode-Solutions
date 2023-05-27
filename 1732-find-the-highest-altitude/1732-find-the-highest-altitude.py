class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        curr = 0
        altMax = 0
        for i in range(len(gain)):
            curr += gain[i]
            altMax = max(curr, altMax)
        return altMax
        