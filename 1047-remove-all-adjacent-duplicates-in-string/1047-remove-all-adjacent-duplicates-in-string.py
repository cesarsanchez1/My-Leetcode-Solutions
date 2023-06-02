class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        # stack: a      (else executes)
        # stack: a b    (else executes)
        # stack: a      (IF executes, pops b off)
        # stack: a      (IF executes, pops b off)
        # stack:        (IF executes, pops a off)
        # stack: c      (else executes)
        # stack: c a    (else executes)
        
        for letter in s:
            if stack and stack[-1]==letter:
                stack.pop()
            else:
                stack.append(letter)
        
        res = ""
        for item in stack:
            res+=item
        return res