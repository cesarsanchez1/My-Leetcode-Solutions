class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:

        num1 = ""
        num2 = ""
        num3 = ""

        for letter in firstWord:
            num1 += str(ord(letter)-ord('a'))
        
        for letter in secondWord:
            num2 += str(ord(letter)-ord('a'))
        
        for letter in targetWord:
            num3 += str(ord(letter)-ord('a'))

        temp = int(num1) + int(num2)

        if temp == int(num3):
            return True
        return False




