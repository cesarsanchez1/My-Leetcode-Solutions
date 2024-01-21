class Solution:
    def removeDuplicates(self, s: str) -> str:
        
        stack = []
        
        for letter in s:
            stack.append(letter)
            
            if len(stack)>=2:
                if stack[-1] == stack[-2]:
                    stack.pop()
                    stack.pop()
                    
        return ''.join(stack)
                    
            