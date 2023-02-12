class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        arr = []
        for item in matrix:
            arr.extend(item)
        arr.sort()
        return arr[k-1]
            
            
        