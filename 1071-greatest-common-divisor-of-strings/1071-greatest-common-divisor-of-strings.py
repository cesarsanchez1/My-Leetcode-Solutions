class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if len(str1)<=len(str2):
            shortStr = str1
            longStr = str2
        else:
            shortStr = str2
            longStr = str1

        ogShort = shortStr
        ogLong = longStr
        
        origLen = len(shortStr)
        origDivisor = shortStr
        
        for i in range(len(str1)):
            shortStr = shortStr[0:origLen-i]
            if shortStr == "":
                break
            print(shortStr)
            dividend1 = len(longStr)/(len(shortStr))
            dividend2 = len(origDivisor)/(len(shortStr))
            #print("DIVIDEND: ", longStr, "/", shortStr, " = ", dividend1)
            if (dividend1.is_integer() == True) and (dividend2.is_integer() == True):
                #print("Can be Divided Evenly: ", longStr, "/", shortStr, " = ", dividend1)
                #print("Can be Divided Evenly: ", origDivisor, "/", shortStr, " = ", dividend2)
                temp1 = ""
                temp2 = ""
                for j in range(int(dividend1)):
                    temp1+=shortStr
                for k in range(int(dividend2)):
                    temp2+=shortStr
                if temp1==ogLong and temp2==ogShort:
                    return shortStr    
        return ""
            
            
        
        
        
        