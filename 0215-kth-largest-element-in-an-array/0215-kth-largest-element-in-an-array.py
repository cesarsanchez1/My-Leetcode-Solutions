class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        highest = max(nums)
        
        uniqueNums = set(nums)
        
        freq = {}
        
        for item in nums:
            if item in freq:
                freq[item] += 1
            else:
                freq[item] = 1
        
        check = highest
        
        while -(10**4) <= check <= (10**4):
            if check in uniqueNums:
                occurences = freq[check]
                if k <= occurences:
                    return check
                k = k-occurences
            check -= 1
        
        
            
            
            

        