class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        result = ""
        i = 0
        while i < len(s):
            if s[i].isdigit():
                stack.append("")
                while s[i] != '[':
                    stack[-1] += s[i]
                    i += 1
                stack.append("")
            elif s[i] == ']':
                e_s = stack.pop()
                n = int(stack.pop()) 
                if stack:
                    stack[-1] += e_s*n
                else:
                    result += e_s*n
            else:
                if not stack:
                    result += s[i]
                else:
                    stack[-1] += s[i]
            i += 1
        return result
                
        