class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # To find the single element in an array where every element 
        # appears twice except for one, you can use the XOR (exclusive OR) 
        # operation. XORing a number with itself results in zero, so when you XOR 
        # all the numbers in the array together, the duplicate elements cancel each 
        # other out, leaving only the single element.
        
        res = 0
        
        for num in nums:
            res ^= num
        return res