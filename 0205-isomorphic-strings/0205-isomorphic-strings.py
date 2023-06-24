class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        freq1 = {}
        freq2 = {}
        
        for s_char, t_char in zip(s, t):
            
            if s_char in freq1:
                if freq1[s_char] != t_char:
                    return False
                
            if t_char in freq2:
                if freq2[t_char] != s_char:
                    return False
            
            freq1[s_char] = t_char
            freq2[t_char] = s_char
            
        return True