class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        counter = 0
        for item in s:
            if item == letter:
                counter += 1
        return int((counter/len(s))*100)
        