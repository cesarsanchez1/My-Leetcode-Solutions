class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        freq = {}
        
        for item in nums:
            freq[item] = freq.get(item, 0) + 1
            
        unique = list(set(nums))
        
        first = 0
        second = 0
        
        for item in unique:
            if freq[item]%2==0:
                first += int(freq[item]/2)
            elif freq[item]==1:
                second += 1
            else:
                first += int((freq[item]-1)/2)
                second += 1
            
        return [first, second]
            