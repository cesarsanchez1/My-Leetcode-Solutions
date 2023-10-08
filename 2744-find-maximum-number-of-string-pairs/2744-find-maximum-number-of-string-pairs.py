class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        counter = 0
        for i in range(len(words)):
            for j in range(i+1, len(words)):
                if len(words[i]) == len(words[j]) and words[i] == words[j][::-1]:
                    counter+=1
        return counter