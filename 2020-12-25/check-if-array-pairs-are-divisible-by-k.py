class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        remainder = [0]* k
        result = 0
        for item in arr:
            remainder[item%k] += 1
        for i in range(0,int(k/2)+1):
            if i == 0 or 2*i == k:
                if remainder[i]%2 != 0:
                    return False                    
            else:
                if remainder[i] != remainder[k-i]:
                    return False
        return True