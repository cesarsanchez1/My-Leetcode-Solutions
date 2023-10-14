class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        arr = list(s)
        alpha = set("qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM")
        
        left = 0
        right = len(s)-1
        
        while left < right:
            while left < right and arr[left] in alpha and arr[right] not in alpha:
                right-=1
            while left < right and arr[left] not in alpha and arr[right] in alpha:
                left+=1
            if left < right and arr[left] in alpha and arr[right] in alpha:
                temp = arr[left]
                arr[left] = arr[right]
                arr[right] = temp
            
            right-=1
            left+=1
        
        return ''.join(arr)
            
            
            