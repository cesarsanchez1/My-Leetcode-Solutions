class Solution:
    def makeGood(self, s: str) -> str:
        alphaLower = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM"
        alphaUpper = "QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm"
        freq = {}
        for i in range(52):
            freq[alphaLower[i]] = alphaUpper[i]
        
        stack = []
        
        for letter in s:
            if stack and (stack[-1]==freq[letter]):
                stack.pop()
            else:
                stack.append(letter)
        res = ""
        for item in stack:
            res+=item
        return res
        