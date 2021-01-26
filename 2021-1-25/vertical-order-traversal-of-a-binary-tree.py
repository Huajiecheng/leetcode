# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        count = defaultdict(list)
        q = deque([(0,0,root)])
        l, r = 0, 0
        while q:
            n = len(q)
            for _ in range(n):
                i,j,curr = q.popleft()
                count[i].append((j,curr.val))
                l = min(l,i)
                r = max(r,i)
                if curr.left:
                    q.append((i-1,j+1,curr.left))
                if curr.right:
                    q.append((i+1,j+1,curr.right))
        result = []
        for key in range(l,r+1):
            result.append([v for i,v in sorted(count[key])])           
        return result
        