class Solution:
    def sortTheStudents(self, score: List[List[int]], k: int) -> List[List[int]]:    
        score.sort(key = lambda i: i[k])
        return score[::-1]
            
        