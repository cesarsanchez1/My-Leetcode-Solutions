class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        freq = {}
        highest = 0
        maxFreq = []
        
        for item in nums:
            if item%2==0:
                freq[item] = freq.get(item, 0) + 1
                if highest < freq[item]:
                    maxFreq = []
                    highest = freq[item]
                    maxFreq.append(item)
                elif highest == freq[item]:
                    maxFreq.append(item)

        maxFreq.sort()
        
        if maxFreq == []:
            return -1
        return maxFreq[0]
                    
                
        
                