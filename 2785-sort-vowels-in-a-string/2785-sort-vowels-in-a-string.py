class Solution:
    def sortVowels(self, s: str) -> str:
        vowelSet = set("aeiouAEIOU")
        vowels = ""
        freq = {}
        arr = []

        for item in s:
            
            if item in vowelSet:
                arr.append(ord(item))
                freq[ord(item)] = item
                vowels+=item
        arr.sort()

        res = ""

        for item in arr:
            res += freq[item]

        ans = ""
        j = 0

        for i in range(len(s)):
            if s[i] not in vowelSet:
                ans+=s[i]
            else:
                ans+=res[j]
                j+=1
        return ans



        