class Solution:
    def minimumSum(self, num: int) -> int:
        arr = []
        temp = str(num)
        for item in temp:
            arr.append(int(item))
        
        arr.sort()
        temp1 = int(str(arr[0])+str(arr[2]))
        temp2 = int(str(arr[1])+str(arr[3]))
        return temp1+temp2        
        