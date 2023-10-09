class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        reversedWords = {}
        maxPairs = 0
        
        for word in words:
            reverse = word[::-1]
            
            if reverse in reversedWords and reversedWords[reverse]>0:
                maxPairs += 1
                reversedWords[reverse] -= 1
            else:
                reversedWords[word] = reversedWords.get(word, 0) + 1
            
        return maxPairs
            