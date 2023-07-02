class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        paragraph = paragraph.replace(',', ' ')
        paragraph = paragraph.replace('.', ' ')
        paragraph = paragraph.replace('!', ' ')
        paragraph = paragraph.replace('?', ' ')
        paragraph = paragraph.replace("'", ' ')
        paragraph = paragraph.replace(',', ' ')
        paragraph = paragraph.replace(';', ' ')

        wordArr = paragraph.split()
        bannedSet = set(banned)
        freq = {}
        res = 0
        currWord = ""

        for word in wordArr:
            lower = word.lower()
            if lower not in bannedSet:
                freq[lower] = freq.get(lower, 0) + 1
                if res < freq[lower]:
                    res = freq[lower]
                    currWord = lower

        return currWord






                    
                    
            
            
            
        