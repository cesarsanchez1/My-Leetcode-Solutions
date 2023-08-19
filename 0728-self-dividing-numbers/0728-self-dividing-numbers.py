class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        
        res = []
        
        for i in range(left, right+1):
            check = str(i)
            isDiv = True
            
            for digit in check:
                if int(digit)==0 or i%int(digit) != 0:
                    isDiv = False
                    break
                
            if isDiv == True:
                res.append(i)

        return res