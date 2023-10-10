class Solution:
    def sumBase(self, n: int, k: int) -> int:
        result = ""
        ans = 0

        while n > 0:
            remainder = n % k
            result = str(remainder) + result
            n = int(n/k)

        for item in result:
            ans += int(item)
        
        return ans

        
