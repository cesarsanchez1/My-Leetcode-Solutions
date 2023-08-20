class Solution:
    def addDigits(self, num: int) -> int:
        if len(str(num))==1:
            return num
        numStr = str(num)
        currSum = 0

        while len(numStr) != 1:
            for item in numStr:
                currSum += int(item)

            numStr = str(currSum)

            if len(numStr) == 1:
                return currSum
            currSum = 0
        
        return 0