class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        freq = {}
        highest = max(nums)
        unique = set(nums)

        for item in nums:
            if item in freq:
                freq[item]+=1
            else:
                freq[item]=1
        
        if freq[highest]>1:
            return (highest-1)*(highest-1)
        
        secondHighest = highest
        smallest = min(nums)

        while secondHighest >= smallest:
            secondHighest-=1
            if secondHighest in unique:
                return (secondHighest-1)*(highest-1)
        return 0




            

        