class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        freq = {}
        
        for word in strs:
            temp = [0]*26
            for letter in word:
                temp[ord('a')-ord(letter)]+=1
            
            tupleTemp = tuple(temp)
            
            if tupleTemp in freq:
                freq[tupleTemp].append(word)
            else:
                freq[tupleTemp] = [word]
                
        result = []
        for item in freq.values():
            result.append(item)
        
        return result
            
            
            
                