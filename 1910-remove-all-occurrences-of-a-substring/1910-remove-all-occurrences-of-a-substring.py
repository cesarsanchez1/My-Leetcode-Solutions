class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:

        stack = []
        partSize = len(part)
        listPart = list(part)

        for i in range(len(s)):
            stack.append(s[i])
            if stack and len(stack) >= partSize and stack[-partSize:] == listPart:
                for i in range(partSize):
                    stack.pop()

        return ''.join(stack)

