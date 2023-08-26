class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        a = []
        b = []
        c = []
        
        for item in nums:
            if item%2==0:
                a.append(item)
            else:
                b.append(item)
            
        counter1 = 0
        counter2 = 0
                
        for i in range(len(nums)):
            if i%2==0:
                c.append(a[counter1])
                counter1+=1
            else:
                c.append(b[counter2])
                counter2+=1
        return c
                
            