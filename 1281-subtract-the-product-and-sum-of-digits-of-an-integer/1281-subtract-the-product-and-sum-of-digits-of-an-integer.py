class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        strNum = str(n)
        prod = 1
        sum = 0
        for item in strNum:
            prod*=int(item)
            sum+=int(item)
        return prod-sum
        