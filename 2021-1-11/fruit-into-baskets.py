class Solution:
    def totalFruit(self, tree: List[int]) -> int:
        count = defaultdict(int)
        left = 0
        for i, v in enumerate(tree):
            count[v] += 1
            if len(count) > 2:
                if count[tree[left]] == 1:
                    del count[tree[left]]
                else:
                    count[tree[left]] -= 1
                left += 1
        return i - left + 1
                
            
        