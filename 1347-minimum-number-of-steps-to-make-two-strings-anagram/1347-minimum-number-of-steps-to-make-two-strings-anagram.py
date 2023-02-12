class Solution:
    def minSteps(self, s: str, t: str) -> int:
        count1 = [0]*26
        res = 0
        
        for item in s:
            count1[ord(item)-ord('a')]+=1
            
        for item in t:
            count1[ord(item)-ord('a')]-=1
            
        for item in count1:
            if item != 0:
                res += abs(item)
            
        return int(res/2)
        
            
        
        
            
        
        