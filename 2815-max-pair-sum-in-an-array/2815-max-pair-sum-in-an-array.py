class Solution:
    def maxSum(self, nums: List[int]) -> int:
        
        freq = {}
        keyList = []
        keySet = set()
        
        for num in nums:
            numStr = str(num)
            maxDigit = float('-Inf')
            
            for digit in numStr:
                if int(digit) > maxDigit:
                    maxDigit = int(digit)
                    
            if maxDigit not in keySet:
                keyList.append(maxDigit)
                keySet.add(maxDigit)
                    
            if maxDigit in freq:
                freq[maxDigit].append(num)
            else:
                freq[maxDigit] = [num]
        
        print("keyList: ", keyList)
        print("")
        
        currHighest = float('-Inf')
        
        for item in keyList:
            tempArr = freq[item]
            if len(freq[item]) >= 2:
                tempArr.sort()
                currHighest = max(currHighest, sum(tempArr[len(tempArr)-2:]))
        
        if currHighest == float('-Inf'):
            return -1
        return currHighest
        
            