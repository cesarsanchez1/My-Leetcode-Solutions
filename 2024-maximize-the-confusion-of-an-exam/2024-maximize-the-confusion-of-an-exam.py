class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        left = 0
        trueCount = 0
        N = len(answerKey)
        firstMax = 0

        for right in range(N):
            if answerKey[right]=='T':
                trueCount+=1
            
            while trueCount > k:
                if answerKey[left]=='T':
                    trueCount-=1
                left+=1
            firstMax = max(firstMax, right-left+1)
        
        left = 0
        falseCount = 0
        secondMax = 0

        for right in range(N):
            if answerKey[right]=='F':
                falseCount+=1
            
            while falseCount > k:
                if answerKey[left]=='F':
                    falseCount-=1
                left+=1
            secondMax = max(secondMax, right-left+1)

        res = max(firstMax, secondMax)
        return res
        
            
