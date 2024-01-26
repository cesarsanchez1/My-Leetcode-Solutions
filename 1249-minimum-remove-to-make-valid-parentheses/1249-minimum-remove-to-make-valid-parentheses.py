class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        
        stack = []
        indexSet = set()
        res = ""
        
        for i, char in enumerate(s):
            if char == "(":
                stack.append(i)
            if not stack and char == ")":
                indexSet.add(i)
            if stack and char == ")":
                stack.pop()
        
        stackSet = set(stack)
        
        for i, char in enumerate(s):
            if i not in stackSet and i not in indexSet:
                res += char
                
        return res
            
            
                