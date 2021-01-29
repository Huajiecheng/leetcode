# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, K: int) -> List[int]:
        parent = {}
        def dfs(curr,p):
            if not curr:
                return
            parent[curr] = p
            dfs(curr.left,curr)
            dfs(curr.right,curr)
        dfs(root,None)
        
        q = deque([target])
        distance = 0
        visited = set([target])
        while q:
            if distance == K:
                return [curr.val for curr in q]
            l = len(q)
            for _ in range(l):
                curr = q.popleft()
                for n in (curr.left, curr.right, parent[curr]):
                    if n and n not in visited:
                        visited.add(n)
                        q.append(n)
            distance += 1
        return []
        
            