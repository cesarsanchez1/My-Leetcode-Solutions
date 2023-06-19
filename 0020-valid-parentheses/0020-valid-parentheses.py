class Solution:
    def isValid(self, s: str) -> bool:
        
        closeToOpen = {"}":"{", ")":"(", "]":"["}
        
        stack = []
        
        for letter in s:
            if (letter in closeToOpen):
                if stack and closeToOpen[letter] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(letter)
        
        if stack == []:
            return True
        return False
                
        