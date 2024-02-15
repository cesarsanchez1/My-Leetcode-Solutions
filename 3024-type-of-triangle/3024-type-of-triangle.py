class Solution:
    def triangleType(self, nums: List[int]) -> str:
        
        sideSet = set(nums)

        if (nums[0]+nums[1] <= nums[2]) or (nums[1]+nums[2] <= nums[0]) or (nums[0]+nums[2] <= nums[1]):
            return "none"

        if len(sideSet) == 1:
            return "equilateral"
        elif len(sideSet) == 2:
            return "isosceles"
        elif len(sideSet) == 3:
            return "scalene"
        else:
            return "none"