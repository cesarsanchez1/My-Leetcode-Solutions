class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        freq = {}
        maxFreq = 0 
        for item in nums:
            if item in freq:
                freq[item]+=1
            else:
                freq[item]=1
            maxFreq = max(maxFreq, freq[item])
        
        uniqueVals = list(set(nums))
        
        print(uniqueVals)
            
        arr = [[]]*(maxFreq+1) 
        
        for item in uniqueVals:
            tempArr = [item]*freq[item]
            if arr[freq[item]] == []:
                arr[freq[item]] = tempArr
            else:
                arr[freq[item]].extend(tempArr)
        res = []
        for item in arr:
            item.sort()
            item = item[::-1]
            res.extend(item)
            
        return res
            
        
        
        