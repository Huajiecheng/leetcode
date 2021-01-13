class Solution: 
    def reverseParentheses(self, s: str) -> str:
        result = [""]
        for i in s:
            if i == '(':
                result.append("")
            elif i == ')':
                temp = result.pop()[::-1]
                result[-1] += temp
            else:
                result[-1] += i
        return result[0]
                
        