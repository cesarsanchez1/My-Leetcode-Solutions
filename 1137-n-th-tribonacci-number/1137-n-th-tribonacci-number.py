class Solution:
    def tribonacci(self, n: int) -> int:
        arr = [0,1,1]

        if n == 0:
            return 0
        if n == 1 or n ==2:
            return 1

        scope = n - 3 + 1

        for i in range(scope):
            temp = arr[0+i] + arr[1+i] + arr[2+i]
            arr.append(temp)
        
        return arr[-1]

