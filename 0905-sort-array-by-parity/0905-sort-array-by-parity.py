class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        a = []
        b = []
        
        for item in nums:
            if item%2==0:
                a.append(item)
            else:
                b.append(item)
        a.extend(b)
        return a