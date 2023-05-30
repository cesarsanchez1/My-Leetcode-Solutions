class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        #FIRST FIND THE NUMBER OF VOWEL LETTERS IN THE FIRST K LETTERS
        vowelSet = set(['a','e','i','o','u'])
        counter = 0
        for i in range(k):
            if s[i] in vowelSet:
                counter+=1
        maxCount = counter
        for i in range(k, len(s)):
            if s[i] in vowelSet:
                counter+=1
            if s[i-k] in vowelSet:
                counter-=1
            maxCount = max(maxCount, counter)
        return maxCount
                