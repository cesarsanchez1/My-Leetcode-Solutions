class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        a = []
        b = []

        for i in range(len(nums)):
            if i%2!=0:
                a.append(nums[i])
            else:
                b.append(nums[i])
                
        a.sort()
        a = a[::-1]
        b.sort()

        counter1 = 0
        counter2 = 0
        res = []

        for i in range(len(nums)):
            if i%2!=0:
                res.append(a[counter1])
                counter1 += 1
            else:
                res.append(b[counter2])
                counter2 += 1
        return res



