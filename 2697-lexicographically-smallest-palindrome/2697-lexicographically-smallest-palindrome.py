class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:
        s_arr = list(s)
        size = len(s)//2

        for i in range(size):
            j = len(s)-1-i
            if s_arr[i] != s_arr[j]:
                s_arr[i] = s_arr[j] = min(s_arr[i], s_arr[j]) 
        return ''.join(s_arr)

