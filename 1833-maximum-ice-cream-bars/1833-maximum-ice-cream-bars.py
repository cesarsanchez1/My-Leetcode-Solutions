class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        tot = 0
        counter = 0
        
        for cost in costs:
            tot += cost
            if tot <= coins:
                counter+=1
            else:
                return counter
                
        if counter == 0:
            return 0
        else:
            return counter
        
        