class Solution:
    def reverseWords(self, s: str) -> str:
        wordArray = s.split()
        wordArray = wordArray[::-1]
        res = ""

        for item in wordArray:
            res+=item
            res+=" "
        return res[0:len(res)-1]
