class Solution:
    def divisibilityArray(self, word: str, m: int) -> List[int]:
        prefix = 0
        arr = [0]*len(word)

        for i in range(len(word)):
            prefix = (prefix * 10 + int(word[i]))%m
            if prefix==0:
                arr[i] = 1
        return arr
        