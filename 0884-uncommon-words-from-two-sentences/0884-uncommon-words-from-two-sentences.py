class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        wordArr1 = s1.split()
        wordArr2 = s2.split()
        set1 = set(wordArr1)
        set2 = set(wordArr2)

        freq1 = {}
        freq2 = {}
        res = []

        for item in wordArr1:
            freq1[item] = freq1.get(item, 0) + 1
        
        for item in wordArr2:
            freq2[item] = freq2.get(item, 0) + 1
        
        for item in wordArr1:
            if item not in set2 and freq1[item]==1:
                res.append(item)
        
        for item in wordArr2:
            if item not in set1 and freq2[item]==1:
                res.append(item)
                
        return res
            



        