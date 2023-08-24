class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowedSet = set(allowed)
        counter = 0

        for word in words:
            wordSet = set(word)

            if wordSet.issubset(allowedSet):
                counter += 1

        return counter