class Solution:
    def frequencySort(self, s: str) -> str:
        freq = {}
        maxFreq = 0
        
        for item in s:
            if item in freq:
                freq[item] += 1
            else:   
                freq[item] = 1
            maxFreq = max(maxFreq, freq[item])
            
        uniqueChars = list(set(s))
        arr = [[]]*(maxFreq+1)
        
        for item in uniqueChars:
            count = freq[item]
            letters = [item]*count
            b = ''.join(letters)
            if arr[count] == []:
                arr[count] = [b]
            else:
                arr[count].append(b)
 
        res = ""
    
        check = []
        
        for item in arr:
            if item != []:
                check.append(item)
        
        for i in range(len(check)-1, -1,-1):
            for word in check[i]:
                res += word
        return res
            
        
                
            
        
             
            
    
        


