class Solution:        
    def letterCombinations(self, digits: str) -> List[str]:
        phone = {'2': ['a', 'b', 'c'],
                 '3': ['d', 'e', 'f'],
                 '4': ['g', 'h', 'i'],
                 '5': ['j', 'k', 'l'],
                 '6': ['m', 'n', 'o'],
                 '7': ['p', 'q', 'r', 's'],
                 '8': ['t', 'u', 'v'],
                 '9': ['w', 'x', 'y', 'z']}
        def dfs(prev,new):
            if not new:
                result.append(prev)
            else:
                for i in phone[new[0]]:
                    dfs(prev+i,new[1:])
                    
        result = []
        if digits:
            dfs("",digits)
        return result
        
        