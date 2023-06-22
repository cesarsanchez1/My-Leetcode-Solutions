class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        
        items1.sort()
        items2.sort()
        
        freq = {}
        
        for item in items1:
            if item[0] in freq:
                freq[item[0]]+=item[1]
            else:
                freq[item[0]]=item[1]
                
        for item in items2:
            if item[0] in freq:
                freq[item[0]]+=item[1]
            else:
                freq[item[0]]=item[1]
        
        res = []
        
        for i in freq:
            res.append([i, freq[i]])

        res.sort()
        
        return res
            
                
        
