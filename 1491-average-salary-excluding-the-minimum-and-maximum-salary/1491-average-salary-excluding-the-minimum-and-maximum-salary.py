class Solution:
    def average(self, salary: List[int]) -> float:
        
        minSal = min(salary)
        maxSal = max(salary)
        av = 0
        
        for item in salary:
            av+=item
        av-=(minSal+maxSal)

        return av/(len(salary)-2)
                
            