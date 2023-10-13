class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        n = len(matrix)
        arr = []

        for i in range(1,len(matrix)+1):
            arr.append(i)
        
        numSet = set(arr)

        for row in range(n):
            emptySet1 = set()
            emptySet2 = set()

            for column in range(n):
                if matrix[row][column] not in emptySet1:
                    emptySet1.add(matrix[row][column])
                else:
                    return False
                if matrix[column][row] not in emptySet2:
                    emptySet2.add(matrix[column][row])
                else:
                    return False

            if emptySet1 != numSet or emptySet2 != numSet:
                return False
        return True

