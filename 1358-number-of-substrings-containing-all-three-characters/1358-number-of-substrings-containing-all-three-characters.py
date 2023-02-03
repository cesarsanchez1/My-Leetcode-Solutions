class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        indx_a = -1
        indx_b = -1
        indx_c = -1

        count = 0

        for i, x in enumerate(s):
            if x == 'a':
                indx_a = i
                print(indx_a, x)
            elif x == 'b':
                indx_b = i
                print(indx_b, x)
            else:
                indx_c = i
                print(indx_c, x)
            if i > 1:
                count += min([indx_a, indx_b, indx_c]) + 1

        return count
            
            



            
            










        
