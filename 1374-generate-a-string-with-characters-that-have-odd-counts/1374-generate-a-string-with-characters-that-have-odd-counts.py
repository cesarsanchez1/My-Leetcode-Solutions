class Solution:
    def generateTheString(self, n: int) -> str:
        if n == 1:
            return 'a'
        
        # n = 3
        # abc
        # n = 5
        # abccc
        # n = 7
        # abccccc
        
        if n%2 == 0:
            a = ['a']*(n-1)
            aStr = ''.join(a)
            aStr += 'b'
            return aStr
        else:
            a = ['a']*(n-2)
            aStr = ''.join(a)
            aStr += 'b'
            aStr += 'c'
            return aStr
        