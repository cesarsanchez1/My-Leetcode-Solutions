class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if (len(word1)!=len(word2)) or (set(word1)!=set(word2)):
            return False
        
        freq1 = {}
        freq2 = {}

        for item in word1:
            if item in freq1:
                freq1[item]+=1
            else:
                freq1[item]=1

        for item in word2:
            if item in freq2:
                freq2[item]+=1
            else:
                freq2[item]=1

        count1 = 0
        for item in word1:
            count1 += freq1[item]

        count2 = 0
        for item in word2:
            count2 += freq2[item]
        
        if count1==count2 and set(word1)==set(word2):
            return True
        return False

            
        