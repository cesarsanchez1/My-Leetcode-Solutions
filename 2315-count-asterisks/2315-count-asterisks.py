class Solution:
    def countAsterisks(self, s: str) -> int:
        stack = []
        counter = 0

        for i in range(len(s)):
            if s[i] == '|':
                stack.append(s[i])

            if not stack and s[i] == '*':
                counter += 1
            
            if stack == ['|', '|']:
                stack = []

        return counter

