class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        counter = 0
        for i in range(len(words)):
            if len(pref) <= len(words[i]) and pref == words[i][0:len(pref)]:
                counter+=1
        return counter
        
        
        