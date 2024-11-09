class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        arr1 = [0]*26
        arr2 = [0]*26
        
        for item in s:
            arr1[ord(item)-ord('a')]+=1
        
        for item in t:
            arr2[ord(item)-ord('a')]+=1
        
        return arr1 == arr2