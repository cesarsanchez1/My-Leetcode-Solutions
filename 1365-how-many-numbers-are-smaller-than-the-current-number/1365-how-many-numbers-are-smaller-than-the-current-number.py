class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        arr = list(set(nums))
        arr.sort()
        arr = arr[::-1]
        freq = {}
        
        for item in nums:
            if item in freq:
                freq[item] += 1
            else:
                freq[item] = 1
                
        firstSum = 0
        
        for i in range(1,len(arr)):
            firstSum += freq[arr[i]]
        
        freq1 = {}
            
        for i in range(len(arr)):
            if i != 0:
                firstSum -= freq[arr[i]]
            freq1[arr[i]] = firstSum
            
        res = []
        
        for item in nums:
            res.append(freq1[item])
        return res
            
            
                
        