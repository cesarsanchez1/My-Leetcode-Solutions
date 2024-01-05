class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        
        if s[0] == '0':
            ones = 0
            zeroes = 1
        if s[0] == '1':
            ones = 1
            zeroes = 0

        maxOnes = ones
        maxZeroes = zeroes

        for i in range(1, len(s)):
            if s[i] == '1':
                ones += 1
            if s[i] != '1':
                ones = 0
            maxOnes = max(maxOnes, ones)

            if s[i] == '0':
                zeroes += 1
            if s[i] != '0':
                zeroes = 0
            maxZeroes = max(maxZeroes, zeroes)
        
        if maxOnes > maxZeroes:
            return True
        return False

        
