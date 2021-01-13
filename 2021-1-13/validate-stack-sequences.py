class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        p = 0
        for i in pushed:
            stack.append(i)
            while stack and stack[-1] == popped[p]:
                stack.pop()
                p += 1
        return p == len(popped)

        