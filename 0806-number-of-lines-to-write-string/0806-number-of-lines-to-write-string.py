class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        count = 0
        lines = 1

        for letter in s:
            count += widths[ord(letter)-ord('a')]
            if count > 100:
                lines += 1
                count = widths[ord(letter)-ord('a')]
        
        if lines == 0:
            return [1, count]

        return [lines, count]
            

