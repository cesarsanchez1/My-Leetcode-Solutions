class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = ""
        for i in range(len(word1)):
            res+=word1[i]
            for j in range(len(word2)):
                res += word2[j]
                word2 = word2[j+1:len(word2)]
                break
        if len(word2)>0:
            res+=word2
        return res