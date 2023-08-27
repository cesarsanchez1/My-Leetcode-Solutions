class Solution:
    def secondHighest(self, s: str) -> int:
        
        numSet = set("0123456789")
        numArr = [0]*10
        
        for item in s:
            if item in numSet:
                numArr[int(item)] += 1
                
        numArr = numArr[::-1]
        print(numArr)
        counter = 0
        
        for i in range(len(numArr)):
            if numArr[i] != 0:
                counter +=1 
            if counter == 2:
                return len(numArr)-1-i
            print(len(numArr)-1-i, ", Count: ", numArr[i])
        return -1
            
            
            
                
            