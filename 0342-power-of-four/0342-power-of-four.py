class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n <= 0:
            return False
        a = math.log(n)
        b = math.log(4)
        return (a/b).is_integer()
            