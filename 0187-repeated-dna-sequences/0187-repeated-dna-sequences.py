class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        if len(s) < 10:
            return []
            
        currSequence = ""
        for i in range(10):
            currSequence += s[i]

        mySet = set()
        mySet.add(currSequence)

        res = []

        for i in range(10, len(s)):
            currSequence = currSequence[1:len(currSequence)]
            currSequence+=s[i]

            if currSequence in mySet:
                res.append(currSequence)
            mySet.add(currSequence)
        
        return list(set(res))

        