class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        sArr = sentence.split()

        vowelSet = set("aeiouAEIOU")

        newSent = []
        temp = ""

        for i in range(len(sArr)):
            tempA = ['a']*(i+1)
            addA = ''.join(tempA)
            if sArr[i][0] in vowelSet:
                temp = sArr[i] + "ma" + addA
            else:
                temp = sArr[i][1:] + sArr[i][0] + "ma" + addA
            newSent.append(temp)

        return ' '.join(newSent)
            


            