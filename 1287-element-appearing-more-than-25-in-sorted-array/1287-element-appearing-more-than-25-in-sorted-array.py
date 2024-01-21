class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        
        freq = {}
        unique = list(set(arr))
        counter = 0
        
        for item in arr:
            freq[item] = freq.get(item, 0) + 1
            if freq[item] > len(arr)/4:
                return item
            
        return 0