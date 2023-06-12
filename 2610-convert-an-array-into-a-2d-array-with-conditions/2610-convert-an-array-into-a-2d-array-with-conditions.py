class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        freq = {}

        for item in nums:
            if item in freq:
                freq[item]+=1
            else:
                freq[item]=1

        unique = list(set(nums))

        arr1 = []
        res = []
        counter = 0
        
        while counter < len(nums):
            for item in unique:
                if freq[item]>0:
                    arr1.append(item)
                    freq[item]-=1
                    counter+=1
            res.append(arr1)
            arr1 = []
        
        return res
