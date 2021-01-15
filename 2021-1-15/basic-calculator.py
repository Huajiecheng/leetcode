class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        i = 0
        curr = 0
        for i in '('+ s +')':
            if i.isdigit():
                curr = 10 * curr +int(i)
            elif i == '(':
                stack += [0,'+']
                curr = 0
            elif i != ' ':
                op, prev = stack.pop(), stack.pop()
                if op == '+':
                    curr = prev + curr
                else:
                    curr = prev - curr
                if i == ')':
                    continue
                stack += [curr,i]
                curr = 0                
        return curr
                
            
                
                
        