class Solution:
    def reverseVowels(self, s: str) -> str:    
        vowelSet = {'a','e','i','o','u', 'A','E','I','O','U'}
        vow = ""
        for i in range(len(s)):
            if s[i] in vowelSet:
                vow += s[i]
        vow = vow[::-1]
        res = ""
        j = 0
        for i in range(len(s)):
            if s[i] not in vowelSet:
                res+=s[i]
            else:
                res+=vow[j]
                j+=1
        return res
                
        