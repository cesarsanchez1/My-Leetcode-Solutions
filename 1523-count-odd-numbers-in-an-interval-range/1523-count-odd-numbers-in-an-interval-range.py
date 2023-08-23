class Solution:
    def countOdds(self, low: int, high: int) -> int:
       
        if low%2 != 0 and high%2 != 0 and (high==low):
            return 1
        if low%2 != 0 and high%2 != 0 and (high-low)==2:
            return (high-low)
        if low%2 != 0 and high%2 != 0 and (high-low)>2:
            return int((high-low)/2)+1
        
        if low%2 == 0 and high%2 == 0 and (high-low)==2:
            return 1
        if low%2 == 0 and high%2 == 0 and (high-low)>2:
            return int((high-low)/2)
        if low%2 == 0 and high%2 == 0 and (high==low):
            return 0


        if low%2 != 0 and high%2 == 0 and high-low == 1:
            return 1
        if low%2 != 0 and high%2 == 0 and high-low > 1:
            return (high-low)-int((high-low)/2)
        

        if low%2 == 0 and high%2 != 0 and high-low == 1:
            return 1
        if low%2 == 0 and high%2 != 0 and high-low > 1:
            return (high-low)-int((high-low)/2)
        

        return 0
        



