class Solution:             
    def calculate(self, s: str) -> int:
        prev, curr, result, op = 0, 0, 0, '+'
        for i in s + '+':
            if i == ' ':
                continue
            if i.isdigit():
                curr = 10*curr + int(i)
                continue                
            if op == '+':
                result += prev
                prev = curr                
            elif op == '-':
                result += prev
                prev = -curr
            elif op == '*':
                prev = prev*curr
            elif op == '/':
                prev = int(prev/curr)
            curr = 0
            op = i
        return result + prev

        
    
                
                
            
        