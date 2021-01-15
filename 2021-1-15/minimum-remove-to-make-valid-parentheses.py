class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        s_list = list(s)
        stack = []
        for i,v in enumerate(s_list):
            if v == '(':
                stack.append(i)
            elif v == ')':
                if stack:
                    stack.pop()
                else:
                    s_list[i] = ''
        while stack:
            s_list[stack.pop()] = ''
        return "".join(s_list)
                
            
        