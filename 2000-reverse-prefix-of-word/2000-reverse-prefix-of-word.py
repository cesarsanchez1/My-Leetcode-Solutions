class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        if ch not in word:
            return word
        
        index = 0
        
        for i in range(len(word)):
            if ch == word[i]:
                index = i
                break
        
        temp = word[0:index+1]
        temp = temp[::-1] + word[index+1:len(word)]
        return temp