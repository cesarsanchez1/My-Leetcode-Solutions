class Solution:
    def vowelStrings(self, words: List[str], left: int, right: int) -> int:
        counter = 0
        vowelSet = set("aeiou")
        
        for i in range(left, right+1):
            if words[i][0] in vowelSet and words[i][-1] in vowelSet:
                counter+=1
                
        return counter
        