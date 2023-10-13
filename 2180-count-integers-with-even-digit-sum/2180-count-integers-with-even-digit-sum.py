class Solution:
    def countEven(self, num: int) -> int:
        start = 1
        counter = 0
        
        while start <= num:
            check = str(start)
            digitSum = 0
            for digit in check:
                digitSum += int(digit)
            
            if digitSum%2==0:
                counter+=1
                
            start += 1
            
        return counter