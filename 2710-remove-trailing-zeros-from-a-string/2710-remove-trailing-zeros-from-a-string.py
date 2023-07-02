class Solution:
    def removeTrailingZeros(self, num: str) -> str:
        
        counter = 0

        for i in range(len(num)-1,-1,-1):
            if num[i] == '0':
                counter += 1
            else:
                break

        return num[0:len(num)-counter]
