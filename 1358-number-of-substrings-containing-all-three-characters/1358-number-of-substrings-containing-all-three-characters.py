class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        n = len(s)
        counts = [0] * 3  # Counters for a, b, c
        window_start = 0
        substr_count = 0

        for window_end in range(n):
            # Expand the window
            counts[ord(s[window_end]) - ord('a')] += 1

            # Shrink the window until it no longer contains all characters
            while all(counts):
                # Count the valid substrings
                substr_count += n-window_end
                # Shrink the window
                counts[ord(s[window_start]) - ord('a')] -= 1
                window_start += 1

        return substr_count
                
                



                
                










        
