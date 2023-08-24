class Solution:
    def similarPairs(self, words: List[str]) -> int:
        freq = {}
        
        for word in words:
            freq[word] = set(word)
        
        counter = 0
        
        for i in range(len(words)):
            word1 = words[i]
            for j in range(i+1, len(words)):
                word2 = words[j]
                if freq[word1] == freq[word2]:
                    counter += 1
        return counter
                    
                
                
                