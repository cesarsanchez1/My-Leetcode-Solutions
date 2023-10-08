class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        size = len(arr)
        i = 0
        while i < (len(arr)-1):
            current = arr[i]
            remArr = arr[i+1:]
            if current == 0:
                arr[i+2:] = remArr
                arr[i+1] = 0
                i+=1
            if i >= (len(arr)-1):
                break
            i+=1
        del arr[size:len(arr)]
            