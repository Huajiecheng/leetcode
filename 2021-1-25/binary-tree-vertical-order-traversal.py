# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        count = defaultdict(list)
        q = deque([(0,root)])
        l, r = 0, 0
        while q:
            i,curr = q.popleft()
            if curr:
                count[i].append(curr.val)
                l = min(l,i)
                r = max(r,i)
                q.append((i-1,curr.left))
                q.append((i+1,curr.right))
        return [count[key] for key in range(l,r+1)] 
            
        