class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []

        components = path.split('/')

        print(components)

        for component in components:
            if component == '' or component == '.':
                continue
            elif component == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(component)

        res = "/"
        for item in stack:
            res += item
            res += "/"
        
        if res == "/":
            return res
        return res[0:len(res)-1]
        