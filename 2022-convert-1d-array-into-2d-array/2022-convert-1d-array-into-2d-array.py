class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:

        if m*n != len(original):
            return []

        index = 0
        res = []

        for i in range(m):
            temp = []
            for j in range(n):
                temp.append(original[index])
                index+=1
            res.append(temp)
        return res






        



        