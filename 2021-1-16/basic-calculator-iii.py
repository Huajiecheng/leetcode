class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        curr = 0
        for i in '('+s+')':
            if i.isdigit():
                curr = 10*curr + int(i)
            elif i == '(':
                stack += [0,0,'+']
            elif i != ' ':
                op, prev = stack.pop(), stack.pop()
                if op == '+':
                    stack[-1] += prev
                    prev = curr                
                elif op == '-':
                    stack[-1] += prev
                    prev = -curr 
                elif op == '*':
                    prev = prev*curr
                elif op == '/':
                    prev = int(prev/curr)
                else:
                    stack[-1] += 1
                if i == ')':
                    stack[-1] += prev
                    curr = stack.pop()
                    continue
                stack += [prev,i]
                curr = 0
        return curr
                    
                
        