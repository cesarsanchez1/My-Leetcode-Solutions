class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        window_start = 0
        result = 0
        n = len(s)
        count = [0]*3
        
        for window_end in range(n):
            count[ord(s[window_end])-ord('a')]+=1
            while all(count):
                count[ord(s[window_start])-ord('a')]-=1
                result += (n-window_end)
                window_start+=1
            
        return result
                
                
            
        