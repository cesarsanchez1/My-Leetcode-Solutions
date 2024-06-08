class Solution:
    def reverseVowels(self, s: str) -> str:
        
        vowelSet = set("aeiouAEIOU")
        vowelString = ""
        
        for item in s:
            if item in vowelSet:
                vowelString += item
        
        vowelString = vowelString[::-1]
        
        res = ""
        i = 0
        
        for item in s:
            if item in vowelSet:
                res += vowelString[i]
                i+=1
            else:
                res += item
        return res
                