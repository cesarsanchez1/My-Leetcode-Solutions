class Solution:
    def alternateDigitSum(self, n: int) -> int:
        numStr = str(n)
        numList = []
        
        for item in numStr:
            numList.append(int(item))
        
        maxDigit = max(numList)
        index = 0
        
        for i in range(len(numList)):
            if numList[i] == maxDigit:
                index = i
                break
        
        mult = 1
        res = 0
        
        for i in range(len(numList)):
            res += (numList[i]*mult)
            mult*=-1
        
        return res
            
        
        