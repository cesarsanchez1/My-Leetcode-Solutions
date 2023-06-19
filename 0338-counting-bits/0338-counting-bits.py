class Solution:    
    def countBits(self, n: int) -> List[int]:
        def countZero(myStr):
            counter = 0
            for i in range(len(myStr)):
                if myStr[i] == '1':
                    counter+=1
            return counter
        
        arr = []
        
        for i in range(n+1):
            temp = bin(i)
            tempNum = countZero(temp[2:len(temp)])
            arr.append(tempNum)
        return arr
        