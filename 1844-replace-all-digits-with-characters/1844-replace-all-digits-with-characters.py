class Solution:
    def replaceDigits(self, s: str) -> str:
        
        res = []
        def shift(letter: str, x: int):
            a = chr(ord(letter)+x)
            return a
        
        res.append(s[0])
        
        for i in range(1, len(s)):
            if i%2!=0:
                res.append(shift(s[i-1], int(s[i])))
            else:
                res.append(s[i])
                
        return ''.join(res)
            
        