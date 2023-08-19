class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        numStr = str(num)
        reversed1 = int(numStr[::-1])
        numStrRev = str(reversed1)
        reversed2 = int(numStrRev[::-1])

        if num == reversed2:
            return True
        return False