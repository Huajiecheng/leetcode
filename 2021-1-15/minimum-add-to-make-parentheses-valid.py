class Solution:
    def minAddToMakeValid(self, S: str) -> int:
        stack = []
        for i in S:
            if i == ')' and stack and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(i)                
        return len(stack)
        