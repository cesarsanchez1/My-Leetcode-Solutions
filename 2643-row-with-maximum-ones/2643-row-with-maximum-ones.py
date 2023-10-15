class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        freq = {}
        maxFreq = 0
        res = []
        
        for i in range(len(mat)):
            oneCount = 0
            for j in range(len(mat[0])):
                if mat[i][j] == 1:
                    oneCount += 1
                    
            freq[i] = oneCount
        
        for i in range(len(mat)):
            if maxFreq < freq[i]:
                res = []
                maxFreq = freq[i]
                res.append(i)
            elif maxFreq == freq[i]:
                res.append(i)
        
        return [res[0], maxFreq]
                
                
            
            
        
        