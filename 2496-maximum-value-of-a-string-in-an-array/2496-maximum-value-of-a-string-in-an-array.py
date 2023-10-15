class Solution:
    def maximumValue(self, strs: List[str]) -> int:
        
        def checkType(check: str) -> str:
            alphaSet = set("qwertyuiopasdfghjklzxcvbnm")
            numSet = set("1234567890")
            letterPresent = False
            numPresent = False

            for letter in check:
                if letter in alphaSet:
                    letterPresent = True
                if letter in numSet:
                    numPresent = True
            
            if letterPresent == True and numPresent == True:
                return "alphaNumeric"
            elif letterPresent == False and numPresent == True:
                return "numeric"
            else:
                return "alpha"
            return "none"
        
        largest = 0
        
        for word in strs:
            if checkType(word) == "alphaNumeric" or checkType(word) == "alpha":
                largest = max(largest, len(word))
            else:
                largest = max(largest, int(word))
        
        return largest
            
                
            