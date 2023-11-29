class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        def isFound(check: str, x: str):
            for letter in check:
                if x == letter:
                    return True
            return False

        arr = []

        for i in range(len(words)):
            if isFound(words[i], x) == True:
                arr.append(i)
        return arr


