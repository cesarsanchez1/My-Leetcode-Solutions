class Solution:
    def compress(self, chars: List[str]) -> int:
        chars.append("ASIJMAISCKJNJ")
        stack = []
        res = ""

        j = 0

        for letter in chars:
            if stack and letter != stack[-1]:
                res += stack[-1]
                chars[j] = stack[-1]
                j+=1
                if 10 > len(stack) > 1:
                    chars[j] = str(len(stack))
                    j+=1
                if len(stack) >= 10:
                    size = len(str(len(stack)))
                    temp = str(len(stack))
                    for i in range(size):
                        chars[j] = temp[i]
                        j+=1
                    
                stack = []
            stack.append(letter)
        #del chars[-1]
        
        return j


