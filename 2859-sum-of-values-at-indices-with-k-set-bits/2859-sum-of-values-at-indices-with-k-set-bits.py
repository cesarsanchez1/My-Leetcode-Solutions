class Solution:
    def sumIndicesWithKSetBits(self, nums: List[int], k: int) -> int:
        
        def countOnes(num: str):
            counter = 0
            for item in num:
                if item == "1":
                    counter += 1
            return counter
    
        res = 0
            
        for i in range(len(nums)):
            temp = bin(i)
            print(temp[2:])
            if countOnes(temp[2:]) == k:
                res += nums[i]
        
        return res
                
            
            