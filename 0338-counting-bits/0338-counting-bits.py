class Solution:
    def countBits(self, n: int) -> List[int]:
        
        def countOnes(check: str):
            counter = 0
            for i in range(len(check)):
                if check[i]=='1':
                    counter += 1
            return counter
        
        res = []
        
        for i in range(n+1):
            binNum = str(bin(i))
            res.append(countOnes(binNum[2:]))
            
        return res
            
        