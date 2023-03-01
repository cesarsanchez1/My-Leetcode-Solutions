class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        freq = {}
        res = set()
        for item in nums:
            if item in freq:
                freq[item]+=1
            else:
                freq[item]=1
            if freq[item]==2:
                res.add(item)
            if freq[item]>2:
                res.remove(item)
        return list(res)
            
        


