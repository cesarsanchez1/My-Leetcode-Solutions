class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        currSub = sum(nums[0:k])
        maxAv = (currSub/k)
        for i in range(1, len(nums)-k+1):
            currSub = currSub - nums[i-1]
            currSub = currSub + nums[i+k-1]
            maxAv = max(maxAv, currSub/k)
        return maxAv