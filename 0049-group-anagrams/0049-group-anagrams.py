class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        arr = []
        res = []
        
        dictionary = {}
        tupleSet = set()
        
        for word in strs:
            temp = [0]*26   
            
            for letter in word:
                temp[ord(letter)-ord('a')]+=1
            
            tupleTemp = tuple(temp)
            tupleSet.add(tupleTemp)
            
            if tupleTemp in dictionary:
                dictionary[tupleTemp].append(word)
            else:
                dictionary[tupleTemp] = [word]
                
            arr.append(tupleTemp)
        
        for item in tupleSet:
            res.append(dictionary[item])
            
        return res
        
                