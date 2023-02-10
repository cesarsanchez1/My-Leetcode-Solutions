class Solution:
    def sortSentence(self, s: str) -> str:
        freq = {}
        s += " "
        temp = ""
        index = 0
        myMax = 0
        
        for letter in s:
            if letter == " ":
                index = int(temp[len(temp)-1])
                freq[index] = temp[0:len(temp)-1]
                myMax = max(myMax, index)
                temp = ""
            if letter != " ":
                temp += letter
        
        res = ""
        for i in range(1, myMax+1):
            res += freq[i]
            if i < myMax:
                res += " "
        return res
            
            
        