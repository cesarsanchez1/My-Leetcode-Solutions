class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0
        right = 0
        maxOnes = 0
        zeroCount = 0
        while right < len(nums):
            if nums[right]==0:
                zeroCount+=1
            while zeroCount>k:
                if nums[left]==0:
                    zeroCount-=1
                left+=1           
            maxOnes = max(maxOnes, right-left+1)
            right+=1
        return maxOnes